(graalvm-introduction)=
# GraalVM Native Compile
This tutorial introduces the GraalVM and native-image technology and talks about how Java applications can benefit from native compilation.

## GraalVM Native Image
[GraalVM](https://www.graalvm.org/) is a high-performance JDK distribution that compiles Java applications into standalone, native binaries using ahead-of-time compilation of Java byte-code to native machine code. These binaries start instantly, perform well right from the start, use fewer resources, and scale very well. GraalVM may be used like any other JDK, with your favorite IDE.

While GraalVM also offers a JIT-based runtime and rich polyglot capabilities through the [Truffle](https://www.graalvm.org/latest/graalvm-as-a-platform/language-implementation-framework/LanguageTutorial/) framework; this tutorial only uses its native image capability. The GraalVM binary packages - both enterprise edition and community edition - come with a `native-image` binary. This is the tool used to compile Java applications into native binaries.

## What GraalVM offers
GraalVM [ahead-of-time compiles](https://www.marcobehler.com/guides/graalvm-aot-jit) all the classes, including those from Java's standard library, that are encountered on all possible code paths of an application. Static members of these classes may be initialized at compile time. This is a significant departure from Java’s lazy loading of classes.

There is no JIT compiler. So, there is no runtime profiling and optimization. Also, if offers very limited garbage-collection [options](https://www.graalvm.org/latest/reference-manual/native-image/optimizations-and-performance/MemoryManagement/). The community edition only offers the 'serial garbage collector' option. Oracle’s GraalVM Enterprise Edition additionally offers the G1 generational garbage collector option. It is possible to completely disable garbage collection using the epsilon collector. Limited garbage collection and no JIT compilation save considerable CPU cycles that the application can use.

In short, GraalVM trades Java’s dynamic/runtime features for an improved application startup performance, more efficient use of resources, and better scaling.

## GraalVM Community Edition for Ubuntu
GraalVM Community Edition is available, and supported, on Ubuntu 24.04 and above, through a snap package: [graalvm-jdk](https://snapcraft.io/graalvm-jdk), which is built from source. Refer to the installation instructions: {ref}`graalvm-use <graalvm-install>`.

Please report issues int the [graalvm-jdk-snap repository](https://github.com/canonical/graalvm-jdk-snap/issues).

## Does every Java application benefit from native compilation?

The short answer is, no!

As noted before, GraalVM trades some of Java’s dynamic behaviors for startup performance of Java applications that also scale well. Consequently, applications that do not depend on those compromised behaviors stand to benefit from GraalVM.

Typically, long-running applications running on the Java Virtual Machine see significant benefits of JIT compilation, runtime profiling, and re-optimization, over time. This is popularly referred to as 'warm-up'. Long-running applications also need mature and fine-tuned garbage collection strategies. In contrast, GraalVM benefits short-lived applications that need to start quickly that do not really need memory management.

For fast start of long-running Java applications, [OpenJDK CRaC](https://launchpad.net/ubuntu/+source/openjdk-21-crac) (Coordinated Restore at Checkpoint) offers a more promising solution.

## Further reading

Refer to the {ref}`use-graalvm` guide for instructions to native compile a Spring Boot application using GraalVM Community Edition on Ubuntu.
