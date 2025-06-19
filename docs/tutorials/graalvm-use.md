(use-graalvm)=

# Native compilation of Spring Boot applications using GraalVM
This tutorial introduces the GraalVM native image technology and provides the elementary instructions to do a native compile, of a Spring Boot application, using the GraalVM Community Edition snap on Ubuntu.

## GraalVM Native Image
GraalVM is a high-performance JDK distribution that compiles Java applications into standalone, native binaries, using ahead-of-time compilation of Java bytecode to native machine code. These binaries start instantly, perform well right from the startup, use fewer resources and scale very well. GraalVM may be used like any other JDK, with your favorite IDE. 

While GraalVM also offers a JIT-based runtime and rich polyglot capabilities through the Truffle framework, this tutorial coverts its “native image” capabilities. GraalVM’s binary packages - both enterprise edition and community edition - come with a `native-image` binary. This is the tool used to compile Java applications into native binaries.

## What GraalVM offers
GraalVM ahead-of-time compiles all the classes, including those from Java's standard libary, that are encountered on all possible code paths of an application. Static members of these classes may be initialized at compile time. This is a significant departure from Java’s lazy loading of classes. This also makes Java reflection convoluted with GraalVM.

There is no JIT compiler. So, there is no runtime profiling and optimization. Also, very limited Garbage Collection options are offered. The community edition offers serial GC only. Oracle’s GraalVM Enterprise Edition additionally offers G1 GC. It is possible to completely disable garbage collection using the epsilon GC option. Limited GC and no JIT save considerable CPU cycles that the application can use.

In short, GraalVM trades Java’s dynamic/runtime features for an improved application startup performance, more efficient use of resources and better scaling.

## GraalVM Community Edition for Ubuntu
GraalVM Community Edition is available, and supported, on Ubuntu 24.04 and above, through a snap package. Please refer to the installation instructions {ref}`here <graalvm-install>`.

## Native compilation of Spring Boot applications
Spring Boot 3+ provides official support for compiling Java applications to native executables. The official documentation is found [here](https://docs.spring.io/spring-boot/reference/packaging/native-image/index.html). To support native compilation with a maven project, a new plugin declaration needs to be added to the pom.xml:

```xml
<plugin>
  <groupId>org.graalvm.buildtools</groupId>
  <artifactId>native-maven-plugin</artifactId>
</plugin>
```

For a Gradle project, add the following plugin declaration to the plugins block in the build.gradle:
```groovy
id 'org.graalvm.buildtools.native' version '0.10.6'
```

Install the GraalVM Community Edition snap from the snap store.
```shell
sudo snap install graalvm-jdk --channel=v21
```

Point the JAVA_HOME environment variable to the GraalVM CE installation.
```shell
export JAVA_HOME=/snap/graalvm-jdk/current/graalvm-ce/
```

Finally, use this command to do a native compilation for your Maven project:
```shell
mvn -Pnative native:compile
```

If you are building a Gradle project, use this command:
```shell
./gradlew nativeCompile
```

The last step builds the application using the typical maven/gradle workflow, subsequently invoking GraalVM native-image to compile it into a native executable. For a Maven project, the native executable will be created under the target directory in the project. The application may be launched by simply executing this file on the command line.

[This] screen-cast captures the workflow mentioned above for the Spring Boot Pet Clinic sample application.

## Does every Java application benefit from native compilation?

The short answer is, no!

As noted before, GraalVM trades some of Java’s dynamic behaviors for startup performance and better scalability of Java applications. Consequently, applications that do not depend on those compromised behaviors stand to benefit from GraalVM.

Typically, long-running applications running on the JVM see significant benefits of JIT compilation, runtime profiling and re-optimization, over time. This is popularly referred to as 'warm-up'. Long-running applications also need mature and fine-tuned garbage collection strategies. In contrast, GraalVM benefits short-lived applications that need to start quickly that do not really need memory management!

For fast-startup of long-running Java applications, OpenJDK CRaC (Coordinated Restore at Checkpoint) offers a more promising solution.
