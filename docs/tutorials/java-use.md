(use-java)=
# Develop with Java on Ubuntu

This tutorial provides basic guidance on how to use of the Java toolchain for development on Ubuntu. It shows how to create a 'Hello, world!' program and explains how to build projects using Gradle or Maven.

For instructions on how to install Java and related tooling, including IDEs, see the dedicated guide on {ref}`install-java`. This article assumes that tooling suggested in that article has been installed.


## `javac` vs build systems

[`javac` is the actual compiler](https://docs.oracle.com/en/java/javase/21/docs/specs/man/javac.html), but developers usually use build systems to compile, build, and package Java projects. [Gradle](https://gradle.org/) and [Maven](https://maven.apache.org/) are popular tools for building Java projects.

To use {command}`javac` directly, refer to the example {ref}`compiling-java-application-using-javac-directly`.


## Creating a Java project using Maven

Setting up and building a new Java project using the Apache Maven tool.


:::
### Prerequisites
:::

- Java Development Kit; refer to {ref}`installing-java-development-kit`.

- Apache Maven:

    To install Maven and the default Java Development Kit from the Ubuntu archive, use:

    ```none
    sudo apt install maven
    ```

    Alternatively, download Maven from [Apache Maven Project](https://maven.apache.org/download.cgi) and follow the installation instructions: [Installing Apache Maven](https://maven.apache.org/install.html).


:::
### Maven project
:::

1. Create a new Java project using the `archetype:generate` Maven sub-command:

    ```none
    mvn archetype:generate -DgroupId=com.yourcompany \
        -DartifactId=helloworld -Dversion=1.0-SNAPSHOT \
        -Dpackage=com.yourcompany.helloworld \
        -DarchetypeGroupId=org.apache.maven.archetypes \
        -DarchetypeArtifactId=maven-archetype-quickstart \
        -DarchetypeVersion=1.4
    ```

    Press {kbd}`Enter` when prompted to confirm your selection.

    This creates a new project using [Maven Quickstart Archetype](https://maven.apache.org/archetypes/maven-archetype-quickstart/).

    Maven sets up a basic project structure:

    ```{terminal}
    :input: tree
    :user: dev
    :host: ubuntu

    .
    └── helloworld
        ├── pom.xml
        └── src
        ├── main
        │   └── java
        │       └── com
        │           └── yourcompany
        │               └── helloworld
        │                   └── App.java
        └── test
            └── java
                └── com
                    └── yourcompany
                        └── helloworld
                            └── AppTest.java
    ```

    That includes a 'Hello World' application and a unit test:

    ```{code-block} java
    :caption: `src/main/java/com/yourcompany/helloworld/App.java`

    package com.yourcompany.helloworld;

    /**
    * Hello world!
    *
    */
    public class App
    {
        public static void main( String[] args )
        {
            System.out.println( "Hello World!" );
        }
    }
    ```

    ```{code-block} java
    :caption: `src/test/java/com/yourcompany/helloworld/AppTest.java`

    package com.yourcompany.helloworld;

    import static org.junit.Assert.assertTrue;

    import org.junit.Test;

    /**
    * Unit test for simple App.
    */
    public class AppTest
    {
        /**
        * Rigorous Test :-)
        */
        @Test
        public void shouldAnswerWithTrue()
        {
            assertTrue( true );
        }
    }
    ```

2. Change to the project directory:

    ```
    cd helloworld
    ```

3. Build and package the application:

    ```none
    mvn -Dmaven.compiler.release=8 package
    ```

    :::{note}
    Notice the `-Dmaven.compiler.release=8` option. The `maven-archetype-quickstart` archetype generates a project that targets Java 7, which is no longer supported by the Java 21 LTS release. The project target can be changed by updating the `maven.compiler.target` and `maven.compiler.source` properties in the {file}`pom.xml` file.
    :::

    This builds and runs unit tests.

    Run the application:

    ```{terminal}
    :input: java -cp target/helloworld-1.0-SNAPSHOT.jar com.yourcompany.helloworld.App
    :user: dev
    :host: ubuntu

    Hello World!
    ```


## Creating a Java project using Gradle

Setting up and building a new Java project using the Gradle build tool.


:::
### Prerequisites
:::

- Java Development Kit; refer to {ref}`installing-java-development-kit`.

- Gradle:

    Install the Gradle snap:

    ```none
    sudo snap install gradle --classic
    ```

    Alternatively, download Gradle from the [Gradle Releases](https://gradle.org/releases) page and follow the provided instructions: [Installing manually](https://gradle.org/install/#manually).


:::
### Gradle project
:::

1. Create a Java project using the `gradle init` command:

    ```none
    mkdir helloworld
    cd helloworld
    gradle init \
        --type java-application \
        --dsl kotlin \
        --test-framework junit-jupiter \
        --package com.yourcompany.helloworld \
        --project-name helloworld  \
        --no-split-project \
        --no-incubating
    ```

    Press {kbd}`Enter` when prompted for the Java version.

    Gradle sets up a basic project structure:

    ```{terminal}
    :input: tree
    :user: dev
    :host: ubuntu

    .
    └── helloworld-gradle
        ├── app
        │   ├── build.gradle.kts
        │   └── src
        │       ├── main
        │       │   ├── java
        │       │   │   └── com
        │       │   │       └── yourcompany
        │       │   │           └── helloworld
        │       │   │               └── App.java
        │       │   └── resources
        │       └── test
        │           ├── java
        │           │   └── com
        │           │       └── yourcompany
        │           │           └── helloworld
        │           │               └── AppTest.java
        │           └── resources
        ├── gradle
        │   ├── libs.versions.toml
        │   └── wrapper
        │       ├── gradle-wrapper.jar
        │       └── gradle-wrapper.properties
        ├── gradlew
        ├── gradlew.bat
        └── settings.gradle.kts
    ```

    That includes a 'Hello World' application and a unit test:

    ```{code-block} java
    :caption: `app/src/main/java/com/yourcompany/helloworld/App.java`

    /*
    * This Java source file was generated by the Gradle 'init' task.
    */
    package com.yourcompany.helloworld;

    public class App {
        public String getGreeting() {
            return "Hello World!";
        }

        public static void main(String[] args) {
            System.out.println(new App().getGreeting());
        }
    }
    ```

    ```{code-block} java
    :caption: `app/src/test/java/com/yourcompany/helloworld/AppTest.java`
    /*
    * This Java source file was generated by the Gradle 'init' task.
    */
    package com.yourcompany.helloworld;

    import org.junit.jupiter.api.Test;
    import static org.junit.jupiter.api.Assertions.*;

    class AppTest {
        @Test void appHasAGreeting() {
            App classUnderTest = new App();
            assertNotNull(classUnderTest.getGreeting(), "app should have a greeting");
        }
    }
    ```

    Gradle generates `gradlew` - a script that manages Gradle download
    and installation for your project. It requires `java` binary to be
    present in the path, or `JAVA_HOME` environment variable set.
    For example:
    ```bash
    export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
    ```

2. Build and run the project using the generated Gradle Wrapper:

    ```{terminal}
    :input: gradle run
    :user: dev
    :host: ubuntu

    gradle run
    Calculating task graph as no cached configuration is available for tasks: run

    > Task :app:run
    Hello World!

    BUILD SUCCESSFUL in 424ms
    2 actionable tasks: 1 executed, 1 up-to-date
    Configuration cache entry stored.

    ```


(compiling-java-application-using-javac-directly)=
## Compiling Java application using `javac` directly

Compiling a Java application directly using the {command}`javac` tool.


:::
### Prerequisites
:::

- Java Development Kit; refer to {ref}`installing-java-development-kit`.


:::
### Procedure
:::

1. Create a 'Hello World' application in a file named {file}`App.java`:

    ```{code-block} java
    public class App {
        public String getGreeting() {
            return "Hello World!";
        }

        public static void main(String[] args) {
            System.out.println(new App().getGreeting());
        }
    }
    ```

2. Compile the class file in the {file}`out` directory:

    ```none
    javac App.java -d out
    ```

3. Execute the program:

    ```{terminal}
    :input: java -cp out/ App
    :user: dev
    :host: ubuntu

    Hello World!
    ```


## Running Java application as a shebang script

Running a Java application as a script with the {command}`java` interpreter specified using the 'shebang' (`#!`) interpreter directive.


:::
### Prerequisites
:::

- Java Development Kit; refer to {ref}`installing-java-development-kit`.


:::
### Procedure
:::

1. Create a 'Hello World' application in a file named {file}`App` and include the interpreter directive on the first line:

    ```{code-block} java
    :caption: `App`
    :force:

    #!/usr/bin/java
    public class App {
        public String getGreeting() {
            return "Hello World!";
        }

        public static void main(String[] args) {
            System.out.println(new App().getGreeting());
        }
    }
    ```

    :::{note}
    This file does not have a `.java` extension.
    :::

2. Make the file executable:

    ```
    chmod +x App
    ```

3. Run the application:

    ```{terminal}
    :input: ./App
    :user: dev
    :host: ubuntu

    Hello World!
    ```
