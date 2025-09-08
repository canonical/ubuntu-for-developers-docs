(use-crac)=

# Fast start for Spring Boot apps using OpenJDK CRaC 

This post introduces OpenJDK with the Coordinated Restore at Checkpoint (CRaC) capability. It guides the reader to checkpoint and restore a Spring Boot application and helps appreciate the start-up performance gains CRaC brings to Java applications.

## Background

Java applications are characterized by a slow start-up, causing significant delays in application instances becoming available, which may be unacceptable in real-world deployments. Due to the inherent nature of the Java runtime, applications begin with a poor performance, go through a warm-up phase, eventually reaching a state of peak performance.

Checkpoint/Restore In Userspace (CRIU) is a tool that can capture a memory snapshot of a running process at any moment. This snapshot can then be used to restore the process to the exact state it was in. OpenJDK CRaC brings this same checkpoint-and-restore capability to the Java runtime.

CRaC makes it possible to checkpoint a Java application, running in a state of 'peak performance'. Using the checkpoint snapshot, subsequent instances of the application could be spun up, almost instantaneously, in nearly the same state of execution.


## OpenJDK CRaC for Ubuntu

[CRaC](https://openjdk.org/projects/crac/), which began as an incubation project under the OpenJDK umbrella, has achieved production-grade maturity. OpenJDK CRaC packages for versions [17](https://launchpad.net/ubuntu/+source/openjdk-17-crac) and [21](https://launchpad.net/ubuntu/+source/openjdk-17-crac) were introduced in Ubuntu 24.10.

To install OpenJDK CRaC on Ubuntu 24.10 and above, use:

```none
sudo apt update && sudo apt install openjdk-21-crac-jdk-headless
```

## Checkpointing and restoring Spring Boot applications

Spring Boot 3.2 introduced [support for CRaC](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.2-Release-Notes#initial-support-for-jvm-checkpoint-restore). This, coupled with the underlying OpenJDK CRaC runtime, lets us checkpoint and restore Spring Boot applications.

The following sections list steps to build, checkpoint, and restore a Spring Boot application.

## Building a Spring Boot application with CRaC support

1. Clone the `Spring Boot PetClinic` application:

    ```none
    git clone https://github.com/spring-projects/spring-petclinic && \
    cd spring-petclinic
    ```

2. Add the `org.crac` dependency into the `pom.xml` file:

   ```xml
   <dependency>
       <groupId>org.crac</groupId>
       <artifactId>crac</artifactId>
       <version>1.4.0</version>
   </dependency>
   ```

3. Point the JAVA_HOME environment variable to the OpenJDK CRaC installation:

    ```none
    export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-crac-amd64
    ```

4. Build with maven:

    ```none
    mvn clean package
    ```

Upon a successful build, a JAR file is generated in the target directory.

## Checkpointing the Spring Boot application on start-up

1. Start the application using this command:

    ```none
    $JAVA_HOME/bin/java -XX:CRaCCheckpointTo=$HOME/cr-image -jar target/spring-petclinic-3.5.0-SNAPSHOT.jar
    ```

    The `-XX:CRaCCheckpointTo` option lets you configure the directory where the snapshot image is saved, on checkpoint.

    The PetClinic application typically becomes available for requests within 5-7 seconds of startup.
    ```none
    ...
    2025-09-04T06:50:25.842Z  INFO 7522 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path '/'
    2025-09-04T06:50:25.851Z  INFO 7522 --- [           main] o.s.s.petclinic.PetClinicApplication     : Started PetClinicApplication in 4.657 seconds (process running for 5.157)
    ```

    The web-app should now be accessible at `http://localhost:8080`.


2. Open another terminal and issue the `jcmd` command to list the running Java processes:

    ```none
    jcmd
    ```

    This produces output like:

    ```none
    4146 target/spring-petclinic-3.5.0-SNAPSHOT.jar
    4206 jdk.jcmd/sun.tools.jcmd.JCmd
    ```

    Here, the `PetClinic` application is running in process with process-id 4146.

3. To checkpoint, again use `jcmd` and issue this command:

    ```none
    jcmd 4146 JDK.checkpoint
    ```
    The `PetClinic` application should now crash with a message reading "Killed".

    ```none
    ...
    2025-09-04T06:53:56.670Z  INFO 7522 --- [Attach Listener] jdk.crac                                 : Starting checkpoint
    2025-09-04T06:53:56.677Z  INFO 7522 --- [Attach Listener] o.s.b.w.e.tomcat.GracefulShutdown        : Commencing graceful shutdown. Waiting for active requests to complete
    2025-09-04T06:53:56.695Z  INFO 7522 --- [tomcat-shutdown] o.s.b.w.e.tomcat.GracefulShutdown        : Graceful shutdown complete
    2025-09-04T06:53:56.700Z  WARN 7522 --- [Attach Listener] o.s.b.j.HikariCheckpointRestoreLifecycle : HikariDataSource (HikariPool-1) is not configured to allow pool suspension. This will cause problems when the application is checkpointed. Please configure allow-pool-suspension to fix this!
    2025-09-04T06:53:56.700Z  INFO 7522 --- [Attach Listener] o.s.b.j.HikariCheckpointRestoreLifecycle : Evicting Hikari connections
    Killed
    ```

    The snapshot, which is a set of `.img` files, should be located in the configured directory. We used `$HOME/cr-data` as an example:

    ```none
    $ ls $HOME/cr-data
    core-3445.img  core-3455.img  core-3467.img  core-3479.img  core-3551.img  core-7531.img  core-7543.img  core-7555.img  core-7632.img  mm-3445.img
    core-3446.img  core-3456.img  core-3468.img  core-3480.img  core-7522.img  core-7532.img  core-7544.img  core-7556.img  core-7633.img  mm-7522.img
    core-3447.img  core-3457.img  core-3469.img  core-3481.img  core-7523.img  core-7533.img  core-7545.img  core-7557.img  dump4.log      pagemap-3445.img
    core-3448.img  core-3458.img  core-3472.img  core-3482.img  core-7524.img  core-7534.img  core-7546.img  core-7558.img  fdinfo-2.img   pagemap-7522.img
    core-3449.img  core-3459.img  core-3473.img  core-3483.img  core-7525.img  core-7535.img  core-7549.img  core-7559.img  files.img      pages-1.img
    core-3450.img  core-3460.img  core-3474.img  core-3545.img  core-7526.img  core-7536.img  core-7550.img  core-7560.img  fs-3445.img    pstree.img
    core-3451.img  core-3461.img  core-3475.img  core-3546.img  core-7527.img  core-7537.img  core-7551.img  core-7627.img  fs-7522.img    seccomp.img
    core-3452.img  core-3462.img  core-3476.img  core-3547.img  core-7528.img  core-7538.img  core-7552.img  core-7628.img  ids-3445.img   stats-dump
    core-3453.img  core-3463.img  core-3477.img  core-3549.img  core-7529.img  core-7539.img  core-7553.img  core-7629.img  ids-7522.img   timens-0.img
    core-3454.img  core-3466.img  core-3478.img  core-3550.img  core-7530.img  core-7540.img  core-7554.img  core-7631.img  inventory.img  tty-info.img
    ```

## Restoring the Spring Boot application at checkpoint

Using the snapshot produced at checkpoint, restore the application in the same state.

Use this command to restore:

```none
$JAVA_HOME/bin/java -XX:CRaCRestoreFrom=$HOME/cr-data
```

This should bring up the `PetClinic` application in less than a second.

```none
$ java -XX:CRaCRestoreFrom=$HOME/cr-data
2025-09-04T06:57:58.872Z  WARN 7522 --- [l-1:housekeeper] com.zaxxer.hikari.pool.HikariPool        : HikariPool-1 - Thread starvation or clock leap detected (housekeeper delta=4m5s281ms870µs908ns).
2025-09-04T06:57:58.896Z  INFO 7522 --- [Attach Listener] o.s.c.support.DefaultLifecycleProcessor  : Restarting Spring-managed lifecycle beans after JVM restore
2025-09-04T06:57:58.961Z  INFO 7522 --- [Attach Listener] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path '/'
2025-09-04T06:57:58.975Z  INFO 7522 --- [Attach Listener] o.s.c.support.DefaultLifecycleProcessor  : Spring-managed lifecycle restart completed (restored JVM running for 225 ms)
```

## Practical considerations


 - OpenJDK CRaC mostly benefits applications that are long-running and `stateful`.
 - Ideally, the checkpoint process is carried out in a staging environment with a load that is representative of the real-world load. The snapshot may then be used in production to rapidly spin-up application instances.
 - CRaC also presents a [Java API](https://crac.github.io/jdk/jdk-crac/api/java.base/jdk/crac/package-summary.html) for CRaC-enabling application classes. If done right, this should lead to further gains in the startup performance.
