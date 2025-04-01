**Register the .NET backports PPA**

This version of .NET is not available in the Ubuntu archive, because Canonical
is not committed  to maintain this version of .NET for the lifetime of this
Ubuntu version, but Canonical maintains builds in the .NET backports PPA. The
maintenance is on a best effort basis and limited to the
[upstream lifetime](https://dotnet.microsoft.com/en-us/platform/support/policy)
of this .NET version.

Add the .NET backports PPA as a source for APT:

```text
sudo add-apt-repository ppa:dotnet/backports
```

```{tip}
If you later want to remove the .NET backports PPA simply add the `--remove` flag.
```

````{tip}
{manpage}`add-apt-repository(1)` is a command provided by the
`software-properties-common` package. On most Ubuntu systems this package is
installed by default. Should you encounter the situation that your system tells
you that the command `add-apt-repository` could not be found, simply install the
package `software-properties-common`:

```text
sudo apt update && sudo apt install software-properties-common
```
````
