# Debugging with .NET

Sometimes, the code you write may not behave as intended, and the process of identifying and removing errors, also known as “bugs”, from your code is called **debugging**. It involves systematically testing, analyzing, and modifying code to ensure it functions correctly.

There are many ways to debug a piece of code. Still, the most common one is to use a software called a **debugger**, which allows you to go through each line of code and understand what happens at each step, such as which values are stored in variables and which path the execution is taking whenever it hits a conditional statement.

(pdb-files)=
## PDB files

PDB files, which stand for Program Database files, are essential for debugging .NET applications. These files hold debugging and project state information that allow a debugger to link the compiled code back to the original source code.

Without them, when an error occurs, the debugger can only show the machine code being executed, not the original lines of source code that caused the issue. This makes it incredibly challenging to understand and fix bugs. PDB files contain vital information such as the mapping of compiled instructions to source lines, the names of variables, function names, and the layout of data structures, which the debugger uses to provide a meaningful debugging experience. Without these debug symbols, the debugger treats functions as black boxes, only allowing stepping over them, not into them, as it lacks the necessary information to trace their internal execution.

To obtain PDB files for their own software, developers need to ensure they are generated during the build process. Typically, when compiling a .NET application in debug mode, PDB files are automatically created. However, in release builds, they can be omitted to reduce file size and make it more difficult to reverse engineer the code.

Building an application with the .NET CLI should output the program’s PDB files by default, regardless of the build configuration. As an example, running `dotnet build` for an application called “HelloWorld” should output the program’s PDB file under `bin/Debug/HelloWorld.pdb` relative to the project root directory.

On the other hand, to obtain PDB files for third-party libraries, developers often rely on the package managers through which those libraries are distributed. For .NET projects, NuGet.org is the primary source for packages, and many package authors publish symbol packages along with their library packages. These symbol packages, ending with ".snupkg", contain the PDB files needed for debugging.

NuGet has a centralized repository called the NuGet Symbol Server where all these symbols become available on-demand, and all the major .NET code editors and IDEs support pulling symbols from this server during debug sessions.

(dotnet-debug-symbols-packages)=
## .NET Debug Symbols packages

When stepping into framework functions provided by .NET in a debug session, the debugger needs to have access to the PDB files that contain debug symbols for the libraries that define these functions. For that, .NET Debug Symbols packages are available in the Ubuntu archive starting with .NET 8. These packages contain PDB debug symbols for the .NET Runtime, the ASP\.NET Core Runtime, and the .NET SDK DLLs.

| .NET Version     | Symbol packages available                                                         |
|------------------|-----------------------------------------------------------------------------------|
| .NET 8           | `dotnet-sdk-dbg-8.0`<br/>`dotnet-runtime-dbg-8.0`<br/>`aspnetcore-runtime-dbg-8.0`|
| .NET 9           | `dotnet-sdk-dbg-9.0`<br/>`dotnet-runtime-dbg-9.0`<br/>`aspnetcore-runtime-dbg-9.0`|

```{important}
The symbols available in these packages are meant to be used only with the .NET builds available through the Ubuntu archive packages, as they only strictly match the DLLs in these builds.
```

The .NET Debug Symbols packages can be installed with `apt` just like any other regular Ubuntu package, e.g.

```none
sudo apt install dotnet-sdk-dbg-9.0 dotnet-runtime-dbg-9.0 aspnetcore-runtime-dbg-9.0
```

It is also possible to install them automatically when installing the .NET SDK and Runtime packages by including `--install-suggests` in the install command, e.g.

```none
sudo apt install dotnet9 --install-suggests
```

The symbols packages are structured so that PDB files are placed side-by-side with the DLLs they match. This is what the SDK directory looks like after installing the `dotnet-sdk-dbg-9.0` package. Notice that for each DLL, there is a matching PDB file available.

```{terminal}
:dir: ~
:user: dev
:host: ubuntu
:input: tree -L 1 --charset unicode /usr/lib/dotnet/shared/Microsoft.NETCore.App/9.0.5/
/usr/lib/dotnet/shared/Microsoft.NETCore.App/9.0.5/
…
|-- Microsoft.CSharp.dll
|-- Microsoft.CSharp.pdb
|-- Microsoft.NETCore.App.deps.json
|-- Microsoft.NETCore.App.runtimeconfig.json
|-- Microsoft.VisualBasic.Core.dll
|-- Microsoft.VisualBasic.Core.pdb
|-- Microsoft.VisualBasic.dll
|-- Microsoft.VisualBasic.pdb
|-- Microsoft.Win32.Primitives.dll
|-- Microsoft.Win32.Primitives.pdb
|-- Microsoft.Win32.Registry.dll
|-- Microsoft.Win32.Registry.pdb
|-- mscorlib.dll
|-- mscorlib.pdb
|-- netstandard.dll
|-- netstandard.pdb
|-- System.AppContext.dll
|-- System.AppContext.pdb
|-- System.Buffers.dll
|-- System.Buffers.pdb
|-- System.Collections.Concurrent.dll
|-- System.Collections.Concurrent.pdb
|-- System.Collections.dll
|-- System.Collections.Immutable.dll
|-- System.Collections.Immutable.pdb
|-- System.Collections.NonGeneric.dll
|-- System.Collections.NonGeneric.pdb
|-- System.Collections.pdb
|-- System.Collections.Specialized.dll
|-- System.Collections.Specialized.pdb
…
```
