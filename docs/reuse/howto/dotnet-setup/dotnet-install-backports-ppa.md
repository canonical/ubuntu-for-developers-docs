**Registering the .NET backports PPA**

This version of .NET is not available in the Ubuntu archive because Canonical is not committed to maintaining this version of .NET for the lifetime of this Ubuntu version. But Canonical maintains builds in the {ref}`.NET backports PPA <dotnet-backports-ppa>`. The maintenance is on a best-effort basis and limited to the upstream lifetime of this .NET version: [.NET Support Policy](https://dotnet.microsoft.com/en-us/platform/support/policy).

Add the .NET backports PPA as a source for APT:

```text
sudo add-apt-repository ppa:dotnet/backports
```

If you later want to remove the .NET backports PPA, run the above command with the `--remove` flag.

````{tip}
{manpage}`add-apt-repository(1)` is a command provided by the `software-properties-common` package. On most Ubuntu systems, this package is installed by default. If your system reports that the command `add-apt-repository` could not be found, install the `software-properties-common` package:

```text
sudo apt update && sudo apt install software-properties-common
```
````
