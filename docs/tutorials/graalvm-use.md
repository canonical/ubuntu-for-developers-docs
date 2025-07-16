(use-graalvm)=
## Compiling Spring Boot applications to native executables 
Spring Boot 3+ provides official support for compiling a Java application to a native executable. The documentation is found at [GraalVM Native Images](https://docs.spring.io/spring-boot/reference/packaging/native-image/index.html) in the Spring Boot references.

1. To support native compilation with a Maven project, the [native-maven-plugin](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html) declaration needs to be added to the `pom.xml` file:

   ```xml
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

   ```none
   sudo snap install graalvm-jdk --channel=v21
   ```

3. Point the `JAVA_HOME` environment variable to the GraalVM CE installation:

   ```none
   export JAVA_HOME=/snap/graalvm-jdk/current/graalvm-ce/
   ```

4. Finally, use this command to do a native compilation for your Maven project:

   ```none
   ./mvnw -Pnative native:compile
   ```

To build a Gradle project, use this command:
   ```none
   ./gradlew nativeCompile
   ```

The last step builds the application using the typical Maven/Gradle workflow, subsequently invoking GraalVM native-image to compile it into a native executable. For a Maven project, the native executable is created under the target directory in the project. The application may be launched by executing this file on the command line.

This [screen-cast](https://drive.google.com/file/d/1ZqSMvyhjia4T5MuJa1IcbWNDDkC5xJbD/view?usp=sharing) captures the workflow mentioned above for the [Spring Boot Pet Clinic](https://github.com/spring-projects/spring-petclinic) sample application.

::: {note}
With Maven or Gradle installed, use the `mvn` or `gradle` command in the last step, instead of the wrapper scripts (`mvnw` and `gradlew`) used here.
:::
