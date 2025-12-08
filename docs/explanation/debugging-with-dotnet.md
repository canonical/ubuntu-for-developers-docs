# Debugging with .NET

This article introduces you to key concepts when debugging .NET applications on Ubuntu.

(pdb-files)=
## PDB files

When building a .NET project, two key artifacts are produced:
- an application binary (`.exe` or `.dll`) and
- a **debugging "symbol" file (`.pdb`)**.

PDB files, which stand for *Program Database files*, are essential for debugging .NET applications. Critically, PDB files contain a mapping of each operation in the application binaries to the source lines that produced them, including the names of variables, function names, and the layout of data structures, which the debugger uses to provide a meaningful debugging experience.

Without them, the debugger treats functions as black boxes, only allowing stepping over them, not into them, as it lacks the necessary information to trace their internal execution. Also, when an error occurs, the debugger can only show the machine code being executed, not the original lines of source code that caused the issue. This makes it incredibly challenging to understand and fix bugs.

To obtain PDB files for their own software, developers need to ensure they are generated during the build process, as shown in the {ref}`Hello World example <publishing-dotnet-project>`. Typically, when compiling a .NET application, PDB files are automatically created. However, in release builds, they can be omitted to reduce the overall program size.

On the other hand, developers typically rely on package managers to obtain both libraries and symbols. For .NET projects, {ref}`NuGet <nuget-package-manager>` is the primary source for packages, and many package authors publish symbol packages along with their library packages. These symbol packages, ending with `.snupkg`, contain the PDB files needed for debugging.

NuGet has a centralized repository called the NuGet Symbol Server where symbols are available on-demand. .NET code editors and IDEs typically support pulling symbols from this server to enable a good debugging experience.

(dotnet-debug-symbols-packages)=
## .NET Debug Symbols packages

When stepping into framework functions provided by .NET in a debug session, the debugger needs to have access to the PDB files that contain debug symbols for the libraries that define these functions. For that, .NET Debug Symbols packages are available in the Ubuntu archive starting with .NET 8. These packages contain PDB debug symbols for the .NET Runtime, the ASP\.NET Core Runtime, and the .NET SDK DLLs.

See available {ref}`dotnet-debug-packages`.

```{important}
The symbols available in these packages are meant to be used only with the .NET builds available through the Ubuntu packages, as they only strictly match the DLLs in these builds.
```

The .NET Debug Symbols packages can be installed with `apt` just like any other regular Ubuntu package, for example:

```none
sudo apt install dotnet-sdk-dbg-9.0 dotnet-runtime-dbg-9.0 aspnetcore-runtime-dbg-9.0
```

It is also possible to install them automatically when installing the .NET SDK and Runtime packages by including `--install-suggests` in the `apt install` command:

```none
sudo apt install dotnet9 --install-suggests
```

The symbols packages are structured so that PDB files are placed side-by-side with the DLLs they match. This is what the SDK directory looks like after installing the `dotnet-sdk-dbg-9.0` package. Notice that for each DLL, there is a matching PDB file available.

```{terminal}
:dir: ~
:user: dev
:host: ubuntu

tree -L 1 --charset unicode /usr/lib/dotnet/shared/Microsoft.NETCore.App/9.0.5/
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
