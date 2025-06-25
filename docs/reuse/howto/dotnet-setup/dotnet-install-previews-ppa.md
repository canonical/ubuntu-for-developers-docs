**Registering the .NET previews PPA**

This version of .NET is not available in the Ubuntu archive yet because it is still a preview and therefore is not intended for production environments. Neither Microsoft nor Canonical provides warranties or support guarantees for these preview versions. But Canonical maintains builds in the {ref}`.NET previews PPA <dotnet-previews-ppa>`. The maintenance is on a best-effort basis.

Add the .NET previews PPA as a source for APT:

```text
sudo add-apt-repository ppa:dotnet/previews
```

If you later want to remove the .NET previews PPA, run the above command with the `--remove` flag.

````{tip}
{manpage}`add-apt-repository(1)` is a command provided by the `software-properties-common` package. On most Ubuntu systems, this package is installed by default. If your system reports that the command `add-apt-repository` could not be found, install the `software-properties-common` package:

```text
sudo apt update && sudo apt install software-properties-common
```
````
