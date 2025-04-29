(use-dotnet)=
# Develop with .NET on Ubuntu

This tutorial provides basic guidance on how to use the .NET toolchain for development on Ubuntu. It shows how to create a ‘Hello, world!’ program and how to create, build, test, run, and publish .NET projects using the `dotnet` command-line interface (CLI).

For instructions on how to install .NET and related tooling, including the .NET SDK, see the dedicated guide on {ref}`install-dotnet`. This article assumes that tooling suggested in that article has been installed.


## The .NET CLI

The `dotnet` command can handle multiple installed .NET SDKs and runtimes. It selects the right version of the .NET SDK or runtime when invoked. This has the advantage that you can use one command to interact with multiple versions of .NET.

Any .NET SDK provides sub-commands including `new`, `run`, `build`, and `publish`, which we use to develop the 'Hello, world!' application.

Run `dotnet --help` to see all available sub-commands.


## Creating a .NET project

Create a directory where the project should be located and change into it:

```none
mkdir "HelloWorld" && cd "HelloWorld"
```

Use the `dotnet new` command to create a .NET project from a template. Select the programming language of the project:

::::::{tab-set}
:sync-group: language

:::::{tab-item} C#
:sync: csharp

<!-- Content for C# -->
Run the following command to create a ‘Hello World’ console application written in C#:

```none
dotnet new console
```

This creates the following files:

- `Program.cs`: C# application code. C# source files usually have the `.cs` file extension.
- `HelloWorld.csproj`: This is the C# project file. C# project files usually have the `.csproj` file extension.
- `obj` directory: This directory is used to store temporary files used in order to create the final build output. Because it just contains temporary files, it is safe to delete and should be omitted from your version control system. You can ignore this directory for the rest of this article.
:::::

:::::{tab-item} F#
:sync: fsharp

<!-- Content for F# -->
Run the following command to create a ‘Hello, world!’ console application written in F#:

```none
dotnet new console -lang F#
```

This creates the following files:

- `Program.fs`: F# application code. F# source files usually have the `.fs` file extension.
- `HelloWorld.fsproj`: This is the F# project file. F# project files usually have the `.fsproj` file extension.
- `obj` directory: This directory is used to store temporary files used in order to create the final build output. Because it just contains temporary files, it is safe to delete and should be omitted from your version control system. You can ignore this directory for the rest of this article.
:::::

:::::{tab-item} VB
:sync: vb

<!-- Content for VB -->
Run the following command to create a ‘Hello World’ console application written in Visual Basic:

```none
dotnet new console -lang VB
```

This creates the following files:

- `Program.vb`: Visual Basic application code. Visual Basic source files usually have the `.vb` file extension.
- `HelloWorld.vbproj`: This is the Visual Basic project file. VB project files usually have the `.vbproj` file extension.
- `obj` directory: This directory is used to store temporary files used in order to create the final build output. Because it just contains temporary files, it is safe to delete ans should be omitted from your version control system. You can ignore this directory for the rest of this article.
:::::

::::::

````{tip}
Run the following command in a terminal to see a list of available templates:

```none
dotnet new list
```
````

````{tip}
If you use {manpage}`git(1)` as you version control system, you can generate a `.gitignore` file for .NET projects by using the template with the same name:

```none
dotnet new .gitignore
```
````

## Running the .NET project

Let's see the application in action. Use the `dotnet run` command to restore dependencies (if we would have any), build, and run the application:

```{terminal}
:dir: ~/HelloWorld
:user: dev
:host: ubuntu
:input: dotnet run

Hello, World!
```

```{note}
The actual output you see depends on the programming language chosen because the `console` templates have slightly different text. The above output is from the C# template, the F# template would result in `Hello from F#`, and the VB template would result in `Hello World!` (without the `,`).
```

## Publishing the .NET project

The `dotnet run` command is useful for development when you have a .NET SDK installed. But realistically, you want to distribute your application and run it on a system where just a .NET runtime is installed. To do that, use the `dotnet publish command`:

```{terminal}
:dir: ~/HelloWorld
:user: dev
:host: ubuntu
:input: dotnet publish 

Restore complete (0.7s)
  HelloWorld succeeded (1.7s) → bin/Release/net9.0/publish/

Build succeeded in 2.7s
```

As shown by the terminal output, in this case (using .NET 9) the build output is located in `bin/Release/net9.0/publish/`. This directory would also contain all dependencies (but in this case, there aren't any). You can copy this directory to the target system and run the application with:

```none
dotnet HelloWorld.dll
```

This directory also contains a `HelloWorld` directory. This is a wrapper that is able to search for a compatible .NET runtime on the target system and use that to invoke the `HelloWorld.dll` binary. So, you can also run your application just by executing:

```none
HelloWorld
```
