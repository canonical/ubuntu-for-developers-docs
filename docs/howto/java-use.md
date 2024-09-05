# How to develop using Java on Ubuntu

This article guides the basic use of the Java toolchain for development on Ubuntu. It shows how to create a 'hello world' program and explains how to build projects using `Gradle` or `maven`.

[`javac` is the actual compiler](https://docs.oracle.com/en/java/javase/21/docs/specs/man/javac.html) but usually Java projects are built using a build system. [`gradle`](https://gradle.org/) and [`maven`](https://maven.apache.org/) are popular tools for building Java projects.

If you want to use `javac` directly, refer to the example [Using `javac` directly](#how-to-use-javac-directly).

## Install Java Development Kit

Run

```
apt install default-jdk
```

to install the default Java Development Kit for your Ubuntu release.

Use ``apt install openjdk-21-jdk`` to install the latest LTS release.


## Install Maven

Run

```
apt install maven
```

to install Maven and the default Java Development Kit from the Ubuntu archive.

Alternatively, download Maven from https://maven.apache.org/download.cgi.

## Create a Java project using Maven

1. Create a new Java project using the `archetype:generate` Maven sub-command:

    ```
    mvn archetype:generate -DgroupId=com.yourcompany \
        -DartifactId=helloworld -Dversion=1.0-SNAPSHOT \
        -Dpackage=com.yourcompany.helloworld \
        -DarchetypeGroupId=org.apache.maven.archetypes \
        -DarchetypeArtifactId=maven-archetype-quickstart \
        -DarchetypeVersion=1.4
    ```

    Press <kbd>Enter</kbd> when prompted to confirm your selection.

    This creates a new project using [maven-archetype-quickstart](https://maven.apache.org/archetypes/maven-archetype-quickstart/).


2. Change to the project directory:

    ```
    cd hello_world
    ```

    Maven has already set up a basic project structure that includes a `Hello world` application and a unit test:

    ```
    helloworld
    |-- pom.xml
    `-- src
        |-- main
        |   `-- java
        |       `-- $package
        |           `-- App.java
        `-- test
            `-- java
                `-- $package
                    `-- AppTest.java
    ```

    ```{code-block} java
    :caption: src/main/java/com/yourcompany/helloworld/App.java

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
    :caption: src/test/java/com/yourcompany/helloworld/AppTest.java

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

3. Build and run the program:

    ```
    mvn -Dmaven.compiler.release=8 package
    ```

    :::{note}
    Notice the `-Dmaven.compiler.release=8` option.
    Maven quickstart generates a project that targets Java 7 which is no longer supported by the Java 21 LTS release. The project target can be changed by updating the `maven.compiler.target` and `maven.compiler.source` properties in `pom.xml`
    :::

    This builds and runs unit tests.

    Run the application:

    ```
    java -cp target/helloworld-1.0-SNAPSHOT.jar com.yourcompany.helloworld.App
    Hello World!
    ```

## Install Gradle

Download Gradle from [gradle.org](https://gradle.org/releases).

:::{note}
Gradle introduced Java 21 support in version 8.5.
:::


Alternatively, run

```
snap install gradle
```

to install community-maintained Gradle snap. The snap provides Gradle version 7 but does not support Java 21.

:::{note}
The snap requires setting up the `JAVA_HOME` variable. For example:

```bash
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
```
:::

## Create a Java project using Gradle

1. Create a Java project using the `gradle init` command:

    ```bash
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
    Press <kbd>Enter</kbd> when prompted for the Java version.

    Gradle sets up a basic project structure with a `Hello World!` application:

    ```{code-block} java
    :caption: app/src/main/java/com/yourcompany/helloworld/App.java

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


    and a unit test:

    ```{code-block} java
    :caption: app/src/test/java/com/yourcompany/helloworld/AppTest.java
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

    2. Build and run the project:

    ```
    ./gradlew run
    ```

    This builds and runs the project.

(how-to-use-javac-directly)=
## How to Use `javac` Directly

1. Create a Hello World application in a file `App.java`:

    ```Java
    public class App {
        public String getGreeting() {
            return "Hello World!";
        }

        public static void main(String[] args) {
            System.out.println(new App().getGreeting());
        }
    }
    ```

    Run

    ```
    javac App.java -d out
    ```
    to compile the class file in the `out` directory.

    Execute the program:

    ```
    java -cp out/ App
    Hello World!
    ```

## Running Java application as a shebang script

1. Create a Hello World application in a file `App`:

    ```{code-block}
    :caption: App

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

    :::{important}
    This file does not have a `.java` extension!
    :::

    Make the file executable:

    ```
    chmod +x App
    ```

    Run the application

    ```
    ./App
    Hello World!
    ```