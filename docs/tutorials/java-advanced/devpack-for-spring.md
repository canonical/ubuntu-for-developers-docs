---
myst:
  html_meta:
    description: "Use devpack-for-spring to scaffold, build, and run a Spring Boot application on Ubuntu."
---

(devpack-for-spring)=
# Devpack for Spring

This tutorial shows how to use {pkg}`devpack-for-spring` to set up a Java development environment, scaffold a Spring Boot project, and run it on Ubuntu. The devpack automates environment setup and project scaffolding, and provides offline library management.

For background on devpacks, see {ref}`devpacks`. For instructions on installing the Java toolchain manually, see {ref}`install-java`.


## Installing the devpack

{pkg}`devpack-for-spring` is distributed as a classic-confinement snap. Install it with:

```{terminal}
:user: dev
:host: ubuntu

sudo snap install devpack-for-spring --classic --channel latest/edge
```


## Setting up the development environment

The {command}`setup` command installs the tools required for Java and Spring Boot development, including OpenJDK, build tools, and container runtimes.

To install OpenJDK 21 non-interactively, run:

```{terminal}
:user: dev
:host: ubuntu

devpack-for-spring setup --add openjdk-21-jdk
```

The {command}`--add` option accepts a comma-separated list of software items defined in the devpack's configuration. To see all available items, run {command}`devpack-for-spring setup` without arguments to launch the interactive menu for selecting and deselecting items individually.

:::{note}
Gradle is not installed separately — the scaffolded project includes the Gradle wrapper, which downloads the required Gradle version automatically.
:::

:::{note}
The list of available software items is defined in the {file}`setup-configuration.yaml` file. To override the default selection, create a custom configuration file at {file}`~/.config/devpack-for-spring/setup-configuration.yaml` or set the `SPRING_CLI_SETUP_COMMANDS_CONFIGURATION` environment variable to point to your file.
:::


## Scaffolding a Spring Boot project

The {command}`boot start` command launches an interactive wizard that scaffolds a new Spring Boot project.

1. Run the command in the directory where the project is created:

   ```{terminal}
   :user: dev
   :host: ubuntu

   devpack-for-spring boot start
   ```

1. In the wizard, select **Gradle** as the build system and add the **Spring Web** dependency. Confirm the remaining defaults.

1. After the wizard completes, a new project directory is created with a standard Spring Boot project structure.


### Using the non-interactive CLI

To see what the wizard does under the hood, the equivalent non-interactive command is:

```{terminal}
:user: dev
:host: ubuntu

devpack-for-spring boot start --path demo --project gradle-project \
    --language java --boot-version 4.1.0 --group com.example \
    --artifact demo --name demo --description demo \
    --package-name com.example.demo --packaging jar --java-version 21 \
    --version 0.0.1 --dependencies web

Extracted to <path>/demo
```

The version numbers and other values are examples — adjust them to match your environment and requirements. This creates a {file}`demo/` directory with the same project structure as the wizard. The tool asks for any missing parameters in an interactive way.


### Adding a REST endpoint

The scaffolded project includes a static index page. To add a simple REST endpoint that returns a greeting, create a controller class:

1. Create the file {file}`src/main/java/com/example/demo/GreetingController.java` inside the project directory:

   ```{code-block} java
   :caption: `src/main/java/com/example/demo/GreetingController.java`

   package com.example.demo;

   import org.springframework.web.bind.annotation.GetMapping;
   import org.springframework.web.bind.annotation.RestController;


   @RestController
   class GreetingController {

       @GetMapping("/greeting")
       String greeting() {
           return "Hello from Spring Boot on Ubuntu!\n";
       }
   }
   ```

   The exact package name depends on the group name chosen during scaffolding. Adjust the {command}`package` declaration accordingly.


### Building and running the application

1. Build the project and start the application using the Gradle wrapper:

   ```{terminal}
   :user: dev
   :host: ubuntu
   :dir: ~/demo

   ./gradlew bootRun
   ```

   The application starts and listens on port 8080.

1. In another terminal, verify the endpoint:

   ```{terminal}
   :user: dev
   :host: ubuntu

   curl http://localhost:8080/greeting

   Hello from Spring Boot on Ubuntu!
   ```

1. Press {kbd}`Ctrl-C` in the first terminal to stop the application.


## Formatting source code

{pkg}`devpack-for-spring` includes a format plugin that applies consistent formatting to the project source code. To run it:

```{terminal}
:user: dev
:host: ubuntu
:dir: ~/demo

devpack-for-spring run format
```

To list all available plugins, use {command}`devpack-for-spring plugins`.

:::{admonition} Gradle deprecation warnings
The format command runs a Gradle build internally. Gradle may report deprecated features and generate a problems report at {file}`build/reports/problems/problems-report.html`. These deprecation warnings originate from Gradle init scripts that the devpack installs — not from the project source code. They are safe to ignore and will be resolved in future devpack releases.
:::


## Managing offline library dependencies

{pkg}`devpack-for-spring` provides Spring Boot libraries as content snaps, which are prebuilt binary packages stored locally. Using content snaps reduces build times by avoiding repeated downloads of dependencies.

To list installed and available libraries:

```{terminal}
:user: dev
:host: ubuntu

devpack-for-spring libraries
```

To install or remove a library, use the {command}`install` and {command}`remove` sub-commands respectively.


## What next

- {ref}`install-java`
- {ref}`use-graalvm`
- {ref}`use-crac`


## Additional resources

- [devpack-for-spring README](https://github.com/canonical/devpack-for-spring/blob/main/devpack-for-spring/README.md)
