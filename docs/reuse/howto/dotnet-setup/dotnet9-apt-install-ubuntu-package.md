**Installing the SDK**

The .NET SDK allows you to develop apps with .NET. To install the .NET SDK, run the following command:

```text
sudo apt update && sudo apt install --install-suggests dotnet-sdk-9.0
```

```{note}
Additionally the package `dotnet-sdk-aot-9.0` is installed as a recommended dependency. This package contains components to build your .NET application as native ahead-of-time compiled code. You can instruct APT to not install this package by adding the `--no-install-recommends` flag.

The flag `--install-suggests` instructs APT to install the suggested dependencies `dotnet-sdk-dbg-9.0`, `aspnetcore-runtime-dbg-9.0` and `dotnet-runtime-dbg-9.0`. These packages provide PDB debug symbols. Remove this flag if you do not want to install these packages.
```

```{tip}
There also exists a package with the name `dotnet9`. This is an alias for the `dotnet-sdk-9.0` package.
```

**Installing the runtime**

```{note}
If you installed the .NET SDK, the corresponding runtime is installed automatically as a required dependency.
```

A .NET runtime allows you to run .NET apps that don't provide a runtime. The following command installs the ASP\.NET Core Runtime, which is the most compatible runtime for .NET:

```text
sudo apt update && sudo apt install --install-suggests aspnetcore-runtime-9.0
```

```{note}
The flag `--install-suggests` instructs APT to install the suggested dependencies `aspnetcore-runtime-dbg-9.0` and `dotnet-runtime-dbg-9.0`. These packages provide PDB debug symbols. Remove this flag if you do not want to install these packages.
```

Alternatively, you can just install the .NET runtime without the ASP\.NET Core components:

```text
sudo apt update && sudo apt install --install-suggests dotnet-runtime-9.0
```

```{note}
The flag `--install-suggests` instructs APT to install the suggested dependency `dotnet-runtime-dbg-9.0`. These packages provide PDB debug symbols. Remove this flag if you do not want to install this package.
```
