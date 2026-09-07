---
myst:
    html_meta:
        description: 'Use the Java Workshop SDKs to build, and run a Java application on Ubuntu.'
---

(java-workshop-sdks)=

# Develop with Java Workshop SDKs on Ubuntu

This tutorial provides basic guidance on using the Java Workshop SDKs for development environments on Ubuntu with the [Workshop](https://ubuntu.com/workshop) tool. It shows how to create a `”Hello, World!”` program, explains how to build projects using Gradle or Maven and goes in-depth with an example using the `petclinic` application.

For instructions on how to install Workshop and related tooling, see the dedicated guide on how to [Get started with workshops](https://ubuntu.com/workshop/docs/). This article assumes that the tooling suggested has been installed. There is no need to install Java or related tooling as they are installed through the examples process.

## Currently supported Java Workshop SDKs

The following Workshop SDKs have been made available for the Java ecosystem:

| SDK Name                                              | Versions      | Description                            |
| :---------------------------------------------------- | :------------ | :------------------------------------- |
| [`openjdk`](https://github.com/canonical/openjdk-sdk) | 17, 21 and 25 | Open-source Java Development Kit (JDK) |
| [`maven`](https://github.com/canonical/maven-sdk)     | 3.9           | Apache Maven build tool                |
| [`gradle`](https://github.com/canonical/gradle-sdk)   | 8 and 9       | Gradle build tool                      |

## Getting started with Java Workshop SDKs

To get started using these SDKs, make sure to [install Workshop and its prerequisites](https://ubuntu.com/workshop/docs/tutorial/part-1-get-started/), to ensure it runs. This can be done with the following commands:

```{terminal}
:copy:
:user: dev
:host: ubuntu

sudo snap install --channel=6/stable lxd
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

sudo snap install --classic workshop
```

Before initializing a workshop, we can search the SDK Store to confirm whether they exist and also get information about the publisher and versions available.

```{terminal}
:copy:
:user: dev
:host: ubuntu

sdk find openjdk  # To confirm/search for available SDKs
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

sdk info openjdk  # Inspect an SDKs release information
```

## Creating a Java Workshop using OpenJDK

Compiling a Java application directly using tools from the `openjdk` workshop SDK.

### Prerequisites

- [Install Workshop and its prerequisites](https://ubuntu.com/workshop/docs/tutorial/part-1-get-started/)

### Procedure

1. Initialize the applications workshop definition with the `openjdk` SDK:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop init openjdk-example --sdks openjdk/21/stable
```

This command writes the definition to the `.workshop/openjdk-example.yaml` file with the `openjdk` SDK pinned to the `21/stable` channel.

```{code-block} yaml
:caption: .workshop/openjdk-example.yaml

name: openjdk-example
base: ubuntu@24.04
sdks:
  - name: openjdk
    channel: 21/stable
```

**Note:** The choice of `openjdk-example` as the name of the workshop here is arbitrary, however it could reflect the expected environment context. For example, a project could have development, production and testing workshop definitions to sandbox internal and external release environments whilst keeping them replicable for all users.

2. Create a ‘Hello, World’ application in a file named `App.java`:

```{code-block} java
public class App {
    public String getGreeting() {
        return "Hello, World!";
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
    }
}
```

3. To get the workshop ready for use, we can launch it and confirm the runtime information matches our definition file:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop launch openjdk-example  # Prepare workshop after initialization
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop info openjdk-example    # View information about the workshop
```

This will prepare the workshop by automatically pulling and installing the defined SDKs, after which it will then start the workshop container. If any changes are made to the `.workshop/openjdk-example.yaml` file, the workshop can be refreshed using the `workshop refresh` command.

**Note:** To stop the workshop environment from running, we can use the `workshop stop` to do so. To then make the workshop ready for use again, it can be started with the `workshop start` command.

4. Compile the class file in the `out` directory within the workshop:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop exec openjdk-example -- javac App.java -d out
```

5. Execute the compiled program from within the workshop:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop exec openjdk-example -- java -cp out App
```

This will print `”Hello, World!”` to the workshop console.

## Creating a Java Workshop using Maven

Setting up and building a new Java project using the `maven` workshop SDK.

### Prerequisites

- [Install Workshop and its prerequisites](https://ubuntu.com/workshop/docs/tutorial/part-1-get-started/)

### Procedure

1. Initialize the applications workshop definition with the `openjdk` and `maven` SDKs:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop init maven-example --sdks openjdk/21/stable,maven/3.9/stable
```

This command writes the definition to the `.workshop/maven-example.yaml` file with the SDKs pinned to their respective channels.

```{code-block} yaml
:caption: .workshop/maven-example.yaml

name: maven-example
base: ubuntu@24.04
sdks:
  - name: openjdk
    channel: 21/stable
  - name: maven
    channel: 3.9/stable
```

2. To get the workshop ready for use, we can launch it and confirm the runtime information matches our definition file:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop launch maven-example  # Prepare workshop after initialization
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop info maven-example    # View information about the workshop
```

3. Enter the workshop using the `workshop exec` command:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop exec maven-example bash
```

4. Create a new Java project using the `archetype:generate` Maven sub-command from within the workshop:

```{terminal}
:copy:
:user: dev
:host: ubuntu

mvn archetype:generate -DgroupId=com.yourcompany \
    -DartifactId=helloworld -Dversion=1.0-SNAPSHOT \
    -Dpackage=com.yourcompany.helloworld \
    -DarchetypeGroupId=org.apache.maven.archetypes \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DarchetypeVersion=1.4
```

Press ENTER when prompted to confirm your selection. This creates a new project using [Maven Quickstart Archetype](https://maven.apache.org/archetypes/maven-archetype-quickstart/) and will set up a basic project structure that is replicated between the workshop environment and your host directory.

5. Change to the project directory and package the application:

```{terminal}
:copy:
:user: dev
:host: ubuntu

cd helloworld
```

```{terminal}
:copy:
:user: dev
:host: ubuntu
:dir: ~/helloworld

mvn -Dmaven.compiler.release=8 package
```

## Creating a Java Workshop using Gradle

Setting up and building a new Java project using the `gradle` workshop SDK.

### Prerequisites

- [Install Workshop and its prerequisites](https://ubuntu.com/workshop/docs/tutorial/part-1-get-started/)

### Procedure

1. Initialize the applications workshop definition with the `openjdk` and `gradle` SDKs:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop init gradle-example --sdks openjdk/21/stable,gradle/9/stable
```

This command writes the definition to the `.workshop/gradle-example.yaml` file with the SDKs pinned to their respective channels.

```{code-block} yaml
:caption: .workshop/gradle-example.yaml

name: gradle-example
base: ubuntu@24.04
sdks:
  - name: openjdk
    channel: 21/stable
  - name: gradle
    channel: 9/stable
```

2. To get the workshop ready for use, we can launch it and confirm the runtime information matches our definition file:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop launch gradle-example  # Prepare workshop after initialization
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop info gradle-example     # View information about the workshop
```

3. Enter the workshop using the `workshop exec` command:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop exec gradle-example bash
```

4. Create a new Java project using the `gradle init` command from within the workshop:

```{terminal}
:copy:
:user: dev
:host: ubuntu

mkdir helloworld && cd helloworld
```

```{terminal}
:copy:
:user: dev
:host: ubuntu
:dir: ~/helloworld

gradle init \
    --type java-application \
    --dsl kotlin \
    --test-framework junit-jupiter \
    --package com.yourcompany.helloworld \
    --project-name helloworld \
    --no-split-project \
    --no-incubating
```

Press ENTER when projected for the Java version. This creates a new project which includes a `”Hello, World!”` application and a unit test that is mounted between the workshop environment and your host directory.

5. Change the project directory to build and run the project using the generated Gradle wrapper:

```{terminal}
:copy:
:user: dev
:host: ubuntu

./gradlew run
```

## Advanced Example with `petclinic`

Setting up and building the `petclinic` sample application using the Java workshop SDKs.

### Prerequisites

- [Install Workshop and its prerequisites](https://ubuntu.com/workshop/docs/tutorial/part-1-get-started/)

### Procedure

1. Initialize the `petclinic` project directory by cloning the target repository:

```{terminal}
:copy:
:user: dev
:host: ubuntu

git clone https://github.com/spring-projects/spring-petclinic.git
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

cd spring-petclinic
```

2. Initialize the applications workshop definition with your choice of SDKs. For this example we are going to use the `openjdk` and `maven` SDKs:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop init petclinic-example --sdks openjdk/21/stable,maven/3.9/stable
```

This command writes the definition to the `.workshop/petclinic-example.yaml` file with the SDKs pinned to their respective channels.

3. Extend the `.workshop/petclinic-example.yaml` configuration to include a slot and plug pair that will expose the application over the `localhost:8080` endpoint, and some actions to manage the application:

```{code-block} yaml
:caption: .workshop/petclinic-example.yaml

name: petclinic-example
base: ubuntu@24.04
sdks:
  - name: openjdk
    channel: 21/stable
  - name: maven
    channel: 3.9/stable
    slots:
      petclinic:
        interface: tunnel
        endpoint: localhost:8080
  - name: system
    plugs:
      petclinic:
        interface: tunnel
        endpoint: localhost:8080
actions:
  build: mvn clean package    # Note: We use `mvn` over the `./mvnw` wrapper
  start: mvn spring-boot:run  # to use our custom defined channel version
```

The plug and slot pair that we defined above are the interfaces that define how to communicate and share resources. This allows each workshop to operate in its own isolated environment, whilst still allowing controlled interactions between the SDKs and the host. In our example, we first define a slot for Maven which provides the capability to expose a desired network endpoint through the tunnel interface.

Secondly our example defines a tunnel plug that consumes the capability provided by the Maven slot. Since the plug defined is for the system SDK, this then routes the Maven endpoint to the host endpoint and allows us to access the application from the host. This can be seen in the diagram below, where our interface pairing allows the client access to the application in the workshop.

**![][image1]**

4. After adding the changes above, we can launch the workshop and confirm that the runtime information matches the workshop definition:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop launch petclinic-example        # Prepare workshop after initialization
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop info petclinic-example          # View information about the workshop
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop run petclinic-example -- start  # And start the application using Maven
```

Alternatively, commands can be execute directly inside the environment:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop exec petclinic-example -- mvn clean package
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop exec petclinic-example -- ls -l target/*.jar
```

Since we have exposed the application through the configured slot/plug pairing, we can then see the application in any browser on the host machine at the `http://localhost:8080` endpoint.

5. We can modify the workshop definition to use `gradle` instead of `maven` by updating the actions to work with Gradle instead:

```{code-block} yaml
:caption: .workshop/petclinic-example.yaml

name: petclinic-example
base: ubuntu@24.04
sdks:
  - name: openjdk
    channel: 17/stable
  - name: gradle
    channel: 8/stable
    slots:
      petclinic:
        interface: tunnel
        endpoint: localhost:8080
  - name: system
    plugs:
      petclinic:
        interface: tunnel
        endpoint: localhost:8080
actions:
  build: gradle build    # Note: We use 'gradle' over the './gradlew' wrapper
  start: gradle bootRun  # since we want to use our defined channel version
```

6. Refresh the workshop to now use the `gradle` SDK instead of the `maven` SDK:

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop refresh petclinic-example      # Refreshes environment with Gradle
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop info petclinic-example         # Confirm that information has changed
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

workshop run petclinic-example -- start  # And start the application using Gradle
```

Note: For the `petclinic` project, make sure that the combination of `openjdk` and the chosen build tool versions are compatible.

[image1]: data:image/png;base64,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
