---
myst:
  html_meta:
    description: "Build and run containerized Java applications on Ubuntu using OpenJDK ROCK images."
---

(use-rock)=
# Run containerized Java applications with ROCK images

ROCK images are minimal, hardened Ubuntu images that include only the files and dependencies needed by the runtime. Unlike standard container images, chiselled JRE images omit the package manager (`apt`), documentation, and often a shell. Stripping these unused components reduces the image footprint (from ~360 MB for `ubuntu` with `default-jre-headless` to ~154 MB for `ubuntu/jre:21-24.04_stable`), eliminates common vulnerability vectors, and shrinks the security audit surface.

Because the ROCK containers do not have a guaranteed shell, standard shell-based entrypoint scripts and supervision tools cannot run. ROCK images embed [Pebble](https://documentation.ubuntu.com/pebble/) as PID 1 to supervise services, manage lifecycles, and run health checks directly against application endpoints.


## The chiselled JDK and JRE repositories

The Ubuntu namespace has two distinct images for each supported Java release:

- `ubuntu/jdk` – OpenJDK build environment with compiler tools (`javac`) and standard shells (`bash`, `sh`). Use this image for local compilation, debugging, and multi-stage container build stages.
- `ubuntu/jre` – hardened OpenJDK runtime containing only headless execution modules and Pebble. It contains no compiler (on Java 21 and earlier), no package manager, and no shell. Use this image as the deployment base.

Available tags follow the channel-style convention `<java-version>-<ubuntu-version>_<risk>` (for example, `ubuntu/jdk:21-24.04_stable`, `ubuntu/jre:25-26.04_stable`). Pin all three fields in production builds: the Ubuntu version fixes the `glibc` and system library baseline, while the risk channel (`stable`, `candidate`, `edge`) controls the security update cadence. See [`ubuntu/jdk` on Docker Hub](https://hub.docker.com/r/ubuntu/jdk) and [`ubuntu/jre` on Docker Hub](https://hub.docker.com/r/ubuntu/jre) for published tags.

The remainder of this tutorial uses OpenJDK 21 on Ubuntu 24.04.


## Running a single file with the JDK ROCK

For quick prototyping or running ad-hoc scripts without installing a local Java toolchain, you can [execute `.java` source files directly](https://openjdk.org/jeps/330) using the JDK container.

1. Create a sample file, for example at `~/hello-world/HelloWorld.java`:

    ```java
    class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, World");
        }
    }
    ```

2. Run the source file directly:

    ```{terminal}
    :user: dev
    :host: ubuntu
    :dir: ~/hello-world

    docker run -v $PWD:/work --rm ubuntu/jdk:21-24.04_stable exec -w /work java HelloWorld.java

    Hello, World
    ```

    The `ENTRYPOINT` of a ROCK image is `/usr/bin/pebble enter`, therefore arguments passed to `docker run` are received by Pebble. The `exec` subcommand instructs Pebble to launch a one-shot process, and `-w /work` sets the working directory to the mounted volume so `java` finds `HelloWorld.java`.


## Running classes with JRE ROCK

In this workflow, the JDK container serves as a disposable compilation toolchain, producing class files that run inside the hardened JRE container.

1. Compile the source file using the JDK image:

    ```{terminal}
    :user: dev
    :host: ubuntu
    :dir: ~/hello-world

    docker run --user $(id -u):$(id -g) -v $PWD:/work --rm ubuntu/jdk:21-24.04_stable exec -w /work javac HelloWorld.java
    ```

    ROCK images run as the non-root `_daemon_` user (UID 584792) by default. Pass `--user $(id -u):$(id -g)`, to ensure that the `javac` process has the permission to write `HelloWorld.class` to the host directory mounted at `/work` and creates the class file with your user's ownership.

2. Run the compiled class using the JRE image:

    ```{terminal}
    :user: dev
    :host: ubuntu
    :dir: ~/hello-world

    docker run -v $PWD:/work --rm ubuntu/jre:21-24.04_stable exec java -cp /work HelloWorld

    Hello, World
    ```

    The `--user` flag is omitted here because the JRE process only reads `HelloWorld.class` and does not write to the mounted volume.

    ````{note}
    Starting with OpenJDK 25 (`ubuntu/jre:25-*`), the JRE image bundles `jdk.compiler` and the `javac` binary, allowing source-file launch directly on the JRE image.

    ```{terminal}
    :user: dev
    :host: ubuntu
    :dir: ~/hello-world

    docker run -v $PWD:/work --rm ubuntu/jre:25-26.04_stable exec -w work java HelloWorld.java

    Hello, World
    ```
    ````

## Managing a service with Pebble checks

For long-running applications, Pebble provides process supervision, automatic restarts, and health monitoring. Because the JRE ROCK has no shell, health checks cannot execute shell scripts (`sh -c ...`). Instead, Pebble natively performs HTTP and TCP checks against application endpoints.

1. Create a service file, for example at `HelloService.java`, using the standard library's `jdk.httpserver` module:

    ```java
    import com.sun.net.httpserver.HttpServer;
    import java.io.OutputStream;
    import java.net.InetSocketAddress;

    public class HelloService {
        public static void main(String[] args) throws Exception {
            HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
            server.createContext("/", exchange -> {
                byte[] body = "Hello, World\n".getBytes();
                exchange.sendResponseHeaders(200, body.length);
                try (OutputStream out = exchange.getResponseBody()) {
                    out.write(body);
                }
            });
            server.start();
        }
    }
    ```

2. Create a Pebble layer definition file named `001-hello-service.yaml`:

    ```yaml
    summary: HelloService layer
    services:
      hello-service:
        override: replace
        command: /usr/bin/java -cp / HelloService
        startup: enabled
        on-check-failure:
          up: restart
    checks:
      up:
        override: replace
        period: 5s
        threshold: 3
        http:
          url: http://localhost:8080/
    ```

    Pebble loads layers in alphanumeric order and merges them in a single configuration file.
    The JRE ROCK does not have a shell, so we use the built-in Pebble HTTP health check to query
    `HelloService`. The health check will make a GET request to `http://localhost:8080/` every 5 seconds,
    and if the check fails 3 consecutive times, Pebble will restart `HelloService`.

3. Build and package the service in a `Dockerfile`:

    ```dockerfile
    FROM ubuntu/jdk:21-24.04_stable AS builder
    USER root
    WORKDIR /app
    COPY HelloService.java .
    RUN javac HelloService.java

    FROM ubuntu/jre:21-24.04_stable
    COPY 001-hello-service.yaml /var/lib/pebble/default/layers/
    COPY --from=builder /app/HelloService.class /
    ```

    ```{note}
    The `CMD` instruction is omitted because Pebble automatically starts any service configured with `startup: enabled` in its default layers.
    ```

4. Build and run the service container in the background:

    ```{terminal}
    :user: dev
    :host: ubuntu
    :dir: ~/hello-service

    docker build -t hello-service .
    ```

    ```{terminal}
    :user: dev
    :host: ubuntu
    :dir: ~/hello-service

    docker run -d --name hello-service -p 8080:8080 hello-service
    ```

5. Query service status and health checks:

    ```{terminal}
    :user: dev
    :host: ubuntu
    docker exec hello-service pebble services
    
    Service        Startup  Current  Since
    hello-service  enabled  active   today at 09:09 UTC
    ```
    ```{terminal}
    :user: dev
    :host: ubuntu
    docker exec hello-service pebble checks
    
    Check  Level  Startup  Status  Successes  Failures  Change
    up     -      enabled  up      4          0/3       1
    ```
    ```{terminal}
    :user: dev
    :host: ubuntu
    docker exec hello-service pebble health
    
    healthy
    ```

## Next steps

- **Pebble**: Explore advanced health check types and service options in the [Pebble documentation](https://documentation.ubuntu.com/pebble/).
- **Source repositories**: Track releases or report issues at [`canonical/jre-rock`](https://github.com/canonical/jre-rock) and [`canonical/jdk-rock`](https://github.com/canonical/jdk-rock).
- **Rockcraft**: Explore [Rockcraft documentation](https://ubuntu.com/containers/rockcraft/docs/) and build your own ROCK containers.
