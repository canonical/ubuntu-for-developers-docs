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
```{figure} /images/crac-use/01-normal-startup.png
   :alt: Screenshot displaying a normal `PetClinic` application startup
```

    The web-app should now be accessible at `http://localhost:8080`.


2. Open another terminal and issue the `jcmd` command to list the running Java processes:
```none
jcmd
```
This produces output like:
```
4146 target/spring-petclinic-3.5.0-SNAPSHOT.jar
4206 jdk.jcmd/sun.tools.jcmd.JCmd
```
Here, the `PetClinic` application is running in process with process-id 4146.

3. To checkpoint, again use `jcmd` and issue this command:
```none
jcmd 4146 JDK.checkpoint
```
The `PetClinic` application should now crash with a message reading "Killed".

```{figure} /images/crac-use/02-app-killed.png
   :alt: Screenshot displaying the `PetClinic` application killed on checkpoint.
```

The snapshot, which is a set of `.img` files, should be located in the configured directory. We used `$HOME/cr-data` as an example:

```{figure} /images/crac-use/03-snapshot-dir.png
   :alt: Screenshot showing the contents of the snapshot directory.
```

## Restoring the Spring Boot application at checkpoint

Using the snapshot produced at checkpoint, restore the application in the same state.

Use this command to restore:
```none
$JAVA_HOME/bin/java -XX:CRaCRestoreFrom=$HOME/cr-data
```

This should bring up the `PetClinic` application in less than a second.

```{figure} /images/crac-use/04-restore-app.png
   :alt: Screen showing the application startup through CRaC restore.
```

## Practical considerations

 - OpenJDK CRaC mostly benefits applications that are long-running and `stateful`.
 - Ideally, the checkpoint process is carried out in a staging environment with a load that is representative of the real-world load. The snapshot may then be used in production to rapidly spin-up application instances.
 - CRaC also presents a [Java API](https://crac.github.io/jdk/jdk-crac/api/java.base/jdk/crac/package-summary.html) for the CRaC enablement of application classes. If done right, this should lead to further gains in the startup performance.
