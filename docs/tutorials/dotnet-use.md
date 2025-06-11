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

(publishing-dotnet-project)=
## Publishing the .NET project

The `dotnet run` command is useful for development when you have a .NET SDK installed. But realistically, you want to distribute your application and run it on a system where just a .NET runtime is installed. To do that, use the `dotnet publish` command:

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

This directory also contains a `HelloWorld` file. This is a wrapper that is able to search for a compatible .NET runtime on the target system and use that to invoke the `HelloWorld.dll` binary. So, you can also run your application just by executing:

```none
HelloWorld
```

Finally, there is also a file called `HelloWorld.pdb` available in the publish directory. This is the {ref}`PDB debug symbol file<pdb-files>` for your application, which is not a required file to run the application, but is useful when an error happens and you need to debug your code.

## Debugging the .NET project

The .NET tooling does not include a debugger; therefore, to debug a .NET application, you need to either use a development environment that includes a .NET debugger, such as Visual Studio Code or JetBrains Rider (see {ref}`setting-up-dotnet-ide` for a list of available development environments for .NET), or install a compatible standalone debugger, such as the open-source [Samsung .NET debugger](https://github.com/Samsung/netcoredbg).

Regardless of your choice, once you learn to use a debugger in one environment, the knowledge should transfer to whichever other environment you might encounter in the future. For the purposes of this tutorial, we will walk through how to use the .NET debugger available in Visual Studio Code.

### Preparing a debugging session

First, install Visual Studio Code.

```none
sudo snap install --classic code
```

Open the Hello World project created in the previous steps with Visual Studio Code by running the following command from within the project root directory.

```none
code .
```

Make sure to have the C# language support extension installed to have access to the debugger.

```{figure} /images/debug-dotnet/01-csharp-extension.png
   :alt: C# extension entry in the Visual Studio Code extensions tab
```

Now, replace the content of `Program.cs` with the following code block:

```csharp
var names = new List<string> { "Alice", "Bob", "Charlie" };
var index = 0;

while (index < names.Count)
{
    index++; 
    Console.WriteLine($"Hello, {names[index]}");
}
```

Our goal with this piece of code is to build a list of names – Alice, Bob, and Charlie – then greet each one with “Hello” within the `while` loop. However, running this code shows that it is not working as expected:

```{terminal}
:dir: ~/HelloWorld
:user: dev
:host: ubuntu
:input: dotnet run
Hello, Bob
Hello, Charlie
Unhandled exception. System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index')
   at System.Collections.Generic.List`1.get_Item(Int32 index)
   at Program.<Main>$(String[] args) in /home/ubuntu/HelloWorld/Program.cs:line 8
```

Two problems appeared:

1. The first name of the list, Alice, is skipped, followed by a `Hello, Bob`, then `Hello, Charlie`.
2. An unhandled exception of type `System.ArgumentOutOfRangeException` happens. According to the error message, we are trying to access an index that does not exist in the collection.

Let’s debug.

### Debugging with VS Code

To debug a .NET application with Visual Studio Code, we need to create a launch profile. VS Code can create one automatically by clicking the {guilabel}`Run and Debug` icon, then the {guilabel}`Run and Debug` button, and selecting the {guilabel}`.NET 5+ and .NET Core` item from the menu that pops up.

```{figure} /images/debug-dotnet/02-create-debug-profile.png
   :alt: Screenshot displaying how to create a debug profile for .NET
```

With a launch profile created, go back to the {guilabel}`Run and Debug` section and click the little {guilabel}`Play` icon to start debugging the application. You will see that the exception is thrown on line 8, during the `Console.WriteLine` call.

```{figure} /images/debug-dotnet/03-exception-thrown.png
   :alt: A debugger notification showing an ArgumentOutOfRangeException thrown
```

By analyzing the {guilabel}`Variables` window, we see that the `names` variable has three items, but our index variable is already at 3. In .NET, arrays are indexed starting at 0, which means that the current index is one unit larger than the collection size. That explains the `ArgumentOutOfRangeException` being thrown.

```{figure} /images/debug-dotnet/04-variables-analysis.png
   :alt: A debugger session highlighting the name variable contains 3 elements and index has value 3
```

The issue is that we are incrementing the index variable *before* accessing the names collection. Since the index variable is first assigned to 0, the first increment brings it to 1, making the program greet names starting from the second one -- this is a classic [off-by-one error](https://en.wikipedia.org/wiki/Off-by-one_error). We fix this by moving `index++` one line down. Running the program again shows no errors:

```{figure} /images/debug-dotnet/05-program-fixed.png
   :alt: A highlight that the program exited successfully with exit code 0
```

#### Stepping over code

Another great use of debuggers is the ability to step through code line by line. This is possible by setting breakpoints in the code. A breakpoint indicates to the debugger that, when running the program, it should pause execution at that specific line. This is especially useful when you, as the developer, want to understand the behavior of your code at one specific point.

To set a breakpoint in Visual Studio Code, hover the mouse over the blank space to the left of the line numbers and click the line you want to set the breakpoint in. A red dot should appear indicating that a breakpoint is now set.

Let's go ahead and set a breakpoint on line 6.

```{figure} /images/debug-dotnet/06-breakpoint-set.png
   :alt: A breakpoint is set on the line that contains the WriteLine function
```

Now, running the debugger should pause the execution of the program whenever it hits that specific line of code. You can analyze current variable values in the {guilabel}`Variables` window, see the call stack of the program at that specific line in the {guilabel}`Call Stack` window, and so on.

```{figure} /images/debug-dotnet/07-breakpoint-hit.png
   :alt: The debugger hits the line containing the WriteLine function due to the breakpoint set
```

Clicking the {guilabel}`Step Over` icon, or pressing {kbd}`F10`, should also let you execute the code line by line and watch how the program behaves in “slow motion”. For example, let’s step over the `Console.WriteLine` instruction, which should print `Hello, Alice` to the output console.

```{figure} /images/debug-dotnet/08-first-step-over.png
   :alt: The debugger goes to the next line after stepping over the WriteLine function and printing out "Hello, Alice"
```

The index variable holds the value 0 at that specific point in time. Stepping over the variable increment instruction on line 7 should now bring `index` to 1.

```{figure} /images/debug-dotnet/09-index-step-over.png
   :alt: The debugger steps over the index increment instruction, setting its value to 1
```

To continue execution as usual, click the {guilabel}`Continue` button, or {kbd}`F5`, and the program should now execute until it hits the next breakpoint. As we’ve set one inside the `while` loop, it stops again at the next iteration. To remove the breakpoint, clicking the red dot again, then click {guilabel}`Continue` to let the program resume and finish execution.

#### Stepping into code

Another feature of debuggers is the ability to step into functions as they are called. As an example, let’s create a function called `SayHello`, which prints a greeting for whichever name is passed as a parameter. Then, instead of calling `Console.WriteLine` from within the `while` loop, we call `SayHello`.

```csharp
var names = new List<string> { "Alice", "Bob", "Charlie" };
var index = 0;

while (index < names.Count)
{
    SayHello(names[index]);
    index++;
}

void SayHello(string name)
{
    Console.WriteLine($"Hello, {name}");
}
```

Setting a breakpoint on line 6 should allow us to pause the execution right before calling the `SayHello` function.

```{figure} /images/debug-dotnet/10-breakpoint-sayhello.png
   :alt: The SayHello function is created and a breakline is set where it is called
```

Now, instead of stepping **over** this line, we step **into** it by clicking {guilabel}`Step Into`, or {kbd}`F11`, which should allow us to go into the `SayHello` function and step over its implementation.

```{figure} /images/debug-dotnet/11-first-step-into-01.png
   :alt: The debugger pauses on SayHello and the step into button is highlighted
```

#### Stepping into .NET code

When debugging, stepping into functions within your own code is straightforward, as the debugger has direct access to the source. However, stepping into functions from external libraries or .NET itself requires debug symbols, specifically {ref}`pdb-files`.

This is the case if you want to step into `Console.WriteLine` itself, for example. Clicking {guilabel}`Step Into` when the debugger hits that line simply steps over it, as the debugger does not have the necessary symbols for the library that provides that function.

However, if you install .NET from the Ubuntu archive packages, you can also install matching {ref}`.NET debug symbols packages<dotnet-debug-symbols-packages>` that contain PDB files for the .NET SDK, Runtime, and ASP\.NET Core Runtime. With these packages installed, debuggers are able to step into functions defined within .NET itself.

Let’s set a breakpoint at `Console.WriteLine` on line 12. Make sure to disable {guilabel}`Just My Code` in your debug launcher; otherwise, the debugger would not step into framework code. To do that, add `"justMyCode": false` to your `launch.json` profile.

```{figure} /images/debug-dotnet/12-disable-justmycode.png
   :alt: The launch profile is open with the line disabling JustMyCode highlighted
```

Now, run the debugger.

```{figure} /images/debug-dotnet/13-writeline-breakpoint.png
   :alt: The debugger steps into SayHello and lands in the WriteLine function call
```

If we step **into** that function, or {kbd}`F11`, we go into the `Concat` function implementation, which is responsible for joining our `Hello, ` string with the `name` variable.

```{figure} /images/debug-dotnet/14-concat.png
   :alt: The debugger steps into the first line of the Concat function of .NET
```

Let’s go ahead and step out of this function, since we want to look into the implementation of `Console.WriteLine` instead. Click {guilabel}`Step Out`, or {kbd}`Shift + F11`, and the debugger takes us back to `Console.WriteLine` again – stepping out means “execute the rest of this function and go back to where its value is returned”.

Now, {guilabel}`Step Into` it again, and the debugger should take us right to the implementation of the `WriteLine` function itself. 

You can keep stepping into the many functions that make up `Console.WriteLine` to better understand how it works internally.

```{figure} /images/debug-dotnet/15-writeline.png
   :alt: The debugger steps into the first line of the WriteLine function of .NET
```
