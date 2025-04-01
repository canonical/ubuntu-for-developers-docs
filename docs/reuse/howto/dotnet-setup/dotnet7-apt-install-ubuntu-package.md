**Install the SDK**

The .NET SDK allows you to develop apps with .NET.
To install the .NET SDK, run the following command:

```text
sudo apt update && sudo apt install dotnet-sdk-7.0
```

```{tip}
There also exists a package with the name `dotnet7`. This is effectively just an
alias for the `dotnet-sdk-7.0` package.
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
sudo apt update && sudo apt install aspnetcore-runtime-7.0
```

Alternatively, you can just install the .NET runtime without the ASP\.NET Core
compponents:

```text
sudo apt update && sudo apt install dotnet-runtime-7.0
```
