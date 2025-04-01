**Install the SDK**

The .NET SDK allows you to develop apps with .NET.
To install the .NET SDK, run the following command:

```text
sudo apt update && sudo apt install --install-suggests dotnet-sdk-8.0
```

```{note}
The flag `--install-suggests` instructs APT to install the suggested
dependencies `dotnet-sdk-dbg-8.0`, `aspnetcore-runtime-dbg-8.0` and
`dotnet-runtime-dbg-8.0`. These packages provide PDB debug symbols.
Remove this flag if you do not want to install these packages.
```

```{tip}
There also exists a package with the name `dotnet8`. This is effectively just an
alias for the `dotnet-sdk-8.0` package.
```

**Install the runtime**

```{note}
If you installed the .NET SDK, the corresponding
runtime is installed automatically as a required dependency.
```

A .NET runtime allows you to run .NET apps that didn't provide a runtime.
The following command installs the ASP\.NET Core Runtime, which is the most
compatible runtime for .NET:

```text
sudo apt update && sudo apt install --install-suggests aspnetcore-runtime-8.0
```

```{note}
The flag `--install-suggests` instructs APT to install the suggested
dependencies `aspnetcore-runtime-dbg-8.0` and `dotnet-runtime-dbg-8.0`.
These packages provide PDB debug symbols. Remove this flag if you do not
want to install these packages.
```

Alternatively, you can just install the .NET runtime without the ASP\.NET Core
compponents:

```text
sudo apt update && sudo apt install --install-suggests dotnet-runtime-8.0
```

```{note}
The flag `--install-suggests` instructs APT to install the suggested
dependency `dotnet-runtime-dbg-8.0`. These packages provide PDB debug symbols.
Remove this flag if you do not want to install this package.
```
