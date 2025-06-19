(use-graalvm)=

# Native compilation of Spring Boot applications using GraalVM
This tutorial introduces the GraalVM native image technology and provides the elementary instructions to do a native compile, of a Spring Boot application, using the GraalVM Community Edition snap on Ubuntu.

## GraalVM Native Image
[GraalVM](https://www.graalvm.org/) is a high-performance JDK distribution that compiles Java applications into standalone, native binaries, using ahead-of-time compilation of Java byte-code to native machine code. These binaries start instantly, perform well right from the startup, use fewer resources and scale very well. GraalVM may be used like any other JDK, with your favorite IDE.

While GraalVM also offers a JIT-based runtime and rich polyglot capabilities through the [Truffle](https://www.graalvm.org/latest/graalvm-as-a-platform/language-implementation-framework/LanguageTutorial/) framework, this tutorial only uses its native image capability. The GraalVM binary packages - both enterprise edition and community edition - come with a `native-image` binary. This is the tool used to compile Java applications into native binaries.

## What GraalVM offers
GraalVM [ahead-of-time compiles](https://www.marcobehler.com/guides/graalvm-aot-jit) all the classes, including those from Java's standard library, that are encountered on all possible code paths of an application. Static members of these classes may be initialized at compile time. This is a significant departure from Java’s lazy loading of classes.

There is no JIT compiler. So, there is no runtime profiling and optimization. Also, very limited Garbage Collection [options](https://www.graalvm.org/latest/reference-manual/native-image/optimizations-and-performance/MemoryManagement/) are offered. The community edition only offers the 'serial garbage collector' option. Oracle’s GraalVM Enterprise Edition additionally offers the G1 generational garbage collector option. It is possible to completely disable garbage collection using the epsilon collector! Limited garbage collection and no JIT compilation save considerable CPU cycles that the application can use.

In short, GraalVM trades Java’s dynamic/runtime features for an improved application startup performance, more efficient use of resources and better scaling.

## GraalVM Community Edition for Ubuntu
GraalVM Community Edition is available, and supported, on Ubuntu 24.04 and above, through [a snap package](https://snapcraft.io/graalvm-jdk), which is built from source. Please refer to the installation instructions provided here {ref}`here <graalvm-install>`.

Please report issues [here](https://github.com/canonical/graalvm-jdk-snap/issues).

## Native compilation of Spring Boot applications
Spring Boot 3+ provides official support for compiling a Java application to a native executable. The official documentation is found [here](https://docs.spring.io/spring-boot/reference/packaging/native-image/index.html).

1. To support native compilation with a maven project, the [native-maven-plugin](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html) declaration needs to be added to the `pom.xml` file:

```XML
<plugin>
  <groupId>org.graalvm.buildtools</groupId>
  <artifactId>native-maven-plugin</artifactId>
</plugin>
```

For a Gradle project, add the following [plugin](https://graalvm.github.io/native-build-tools/latest/gradle-plugin.html) declaration to the plugins block in the `build.gradle` file:
```groovy
id 'org.graalvm.buildtools.native' version '0.10.6'
```

2. Install the GraalVM Community Edition snap from the snap store:

```shell
sudo snap install graalvm-jdk --channel=v21
```

3. Point the JAVA_HOME environment variable to the GraalVM CE installation:

```shell
export JAVA_HOME=/snap/graalvm-jdk/current/graalvm-ce/
```

4. Finally, use this command to do a native compilation for your Maven project:

```shell
./mvnw -Pnative native:compile
```

If you are building a Gradle project, use this command:
```shell
./gradlew nativeCompile
```

The last step builds the application using the typical Maven/Gradle workflow, subsequently invoking GraalVM native-image to compile it into a native executable. For a Maven project, the native executable will be created under the target directory in the project. The application may be launched by simply executing this file on the command line.

[This](https://drive.google.com/file/d/1ZqSMvyhjia4T5MuJa1IcbWNDDkC5xJbD/view?usp=sharing) screen-cast captures the workflow mentioned above for the [Spring Boot Pet Clinic](https://github.com/spring-projects/spring-petclinic) sample application.

::: {note}
If you have Maven or Gradle installed, you may use `mvn` or `gradle` command in the last step, instead of the wrapper scripts, `mvnw` and `gradlew`, used here.
:::

## Does every Java application benefit from native compilation?

The short answer is, no!

As noted before, GraalVM trades some of Java’s dynamic behaviors for startup performance of Java applications that also scale well. Consequently, applications that do not depend on those compromised behaviors stand to benefit from GraalVM.

Typically, long-running applications running on the Java Virtual Machine see significant benefits of JIT compilation, runtime profiling and re-optimization, over time. This is popularly referred to as 'warm-up'. Long-running applications also need mature and fine-tuned garbage collection strategies. In contrast, GraalVM benefits short-lived applications that need to start quickly that do not really need memory management!

For fast-startup of long-running Java applications, [OpenJDK CRaC](https://launchpad.net/ubuntu/+source/openjdk-21-crac) (Coordinated Restore at Checkpoint) offers a more promising solution.
