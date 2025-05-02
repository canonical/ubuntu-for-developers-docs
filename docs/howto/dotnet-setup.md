(install-dotnet)=
# How to set up a development environment for .NET on Ubuntu

## Installing .NET

There are multiple methods for installing the .NET toolchain on Ubuntu:

- Using the [`dotnet` snap](https://snapcraft.io/dotnet) – a .NET toolchain installer that makes it easy to install the latest releases of .NET  SDKs/runtimes in parallel.
- Using Ubuntu packages from Ubuntu package feeds – official packages maintained by the Ubuntu team and installed through the Ubuntu package-management system.
- Using Microsoft packages from the Microsoft package feed – official packages maintained by Microsoft and installed through the Ubuntu package-management  system.
- Using Microsoft's installation script – a script you download and run in your terminal that allows you to install any .NET release.
- Manual installation – download the release binaries as a tarball and install them manually.

```{warning}
It's recommended to install the .NET toolchain from.**Do not mix multiple installation methods**, as this may lead to problems when applications try to resolve a specific version of .NET or when you try to update your installation to a new release.
```

### Deciding how to install .NET

```{tip}
**We recommend to use the `dotnet` snap** as we created it specifically to make installing .NET on Ubuntu easy, but there are cases where this may not fit your needs.
```

With the many options available to install .NET on Ubuntu, it can seem overwhelming at first, which method to choose. Below you find an overview and more details for specific cases that should help you select an installation method:

```{mermaid}
:zoom:

%%{init: {"flowchart": {"htmlLabels": false}} }%%
flowchart TD
    NeedNewerFeatureBands{{"`Do you need a higher<br>SDK feature band?<br>(higher than x.x.1xx)`"}}
    NeedPreviewsOrOlderVersions{{"`Do you need preview or older (unsupported) versions?`"}}
    WhichArch1{{"`What is the architecture of your system you want to install .NET on?`"}}
    WhichArch2{{"`What is the architecture of your system you want to install .NET on?`"}}
    WhichArch3{{"`What is the architecture of your system you want to install .NET on?`"}}
    NeedAPT{{"`Do you prefer to use APT?`"}}
    UsesAmd64JammyOrNewer{{"`Do you want to install .NET on Ubuntu 22.04 or newer?`"}}
    UsesArm64JammyOrNewer{{"`Do you want to install .NET on Ubuntu 22.04 or newer?`"}}
    UsesS390xOrPowerJammyOrNewer{{"`Do you want to install .NET on Ubuntu 22.04 or newer?`"}}
    
    UbuntuPackagesInstallation["`Use Ubuntu packages`"]
    SnapInstallation["`**Use the <c>dotnet</c> Snap**`"]
    MicrosoftPackagesInstallation1["`Use Microsoft packages`"]
    MicrosoftPackagesInstallation2["`Use Microsoft packages`"]
    MicrosoftScriptInstallation1["`Use the Microsoft<br>installer script`"]
    MicrosoftScriptInstallation2["`Use the Microsoft<br>installer script`"]
    MicrosoftScriptInstallation3["`Use the Microsoft<br>installer script`"]
    NoInstallation1["`Unfortunately there exists no supported installation method for this case`"]
    NoInstallation2["`Unfortunately there exists no supported installation method for this case`"]
    NoInstallation3["`Unfortunately there exists no supported installation method for this case`"]

    NeedNewerFeatureBands -- Yes --> WhichArch1
    NeedNewerFeatureBands -- No --> NeedPreviewsOrOlderVersions
    WhichArch1 -- x64 --> MicrosoftPackagesInstallation1
    WhichArch1 -- arm64 or arm32 --> MicrosoftScriptInstallation1
    WhichArch1 -- other --> NoInstallation1

    NeedPreviewsOrOlderVersions -- No ----> WhichArch3
    NeedPreviewsOrOlderVersions -- Yes --> WhichArch2
    WhichArch2 -- x64, arm64 or arm32 --> MicrosoftScriptInstallation2
    WhichArch2 -- other --> NoInstallation2
    

    WhichArch3 -- x64 --> UsesAmd64JammyOrNewer
    WhichArch3 -- arm64 --> UsesArm64JammyOrNewer
    WhichArch3 -- arm32 --> MicrosoftScriptInstallation3
    WhichArch3 -- s390x or ppc64el --> UsesS390xOrPowerJammyOrNewer
    WhichArch3 -- other --> NoInstallation3

    UsesAmd64JammyOrNewer -- No --> MicrosoftPackagesInstallation2
    UsesAmd64JammyOrNewer -- Yes --> NeedAPT

    UsesArm64JammyOrNewer -- Yes --> NeedAPT
    UsesArm64JammyOrNewer -- No --> MicrosoftScriptInstallation3

    UsesS390xOrPowerJammyOrNewer -- Yes --> UbuntuPackagesInstallation
    UsesS390xOrPowerJammyOrNewer -- No ---> NoInstallation3

    NeedAPT -- No --> SnapInstallation
    NeedAPT -- Yes --> UbuntuPackagesInstallation
```

```{list-table}
   :header-rows: 1

* - Method
  - Pros
  - Cons
* -  [`dotnet` snap](#dotnet-installation-snap)
  - - **easy & simple installation experience**
  - - currently only supports `x64` and `arm64` system architectures
    - currently only supports Ubuntu 22.04+
* - [Ubuntu packages](dotnet-installation-ubuntu-packages)
  - - supports IBM System Z and POWER system architectures for .NET 8+
  - - some .NET versions are only available after installing an 
      APT repository
    - by default, non-security updates are made available with a
      delay of 1+ week(s); APT can be configured to install them
      as soon as they are available
    - only supports Ubuntu 22.04+
* - [Microsoft packages](dotnet-installation-microsoft-packages)
  - - supports Ubuntu 16.04, 18.04, 20.04
    - higher SDK feature bands are available (> x.x.1xx)
  - - requires installing an APT repository
    - APT may needs to be configure to resolve conflicts with
      Ubuntu packages
    - no support for Ubuntu 24.04+¹
    - only supports the `x64` system architecture
* - Microsoft's [scripted](#dotnet-installation-microsoft-script) / 
    [manual](dotnet-installation-microsoft-manual) installation
  - - control where .NET is installed
    - preview releases are available
    - old (unsupported) versions of .NET are available
    - higher SDK feature bands are available (> x.x.1xx)
    - supports the `arm32` system architecture
  - - error-prone
    - updates need to be installed manually
    - dependencies have to be installed manually
    - no support for IBM System Z and POWER  system architectures
```

¹ Clarification: Canonical maintains .NET packages since 2023. The maintainer team has asked Microsoft to discontinue their package feed for newer Ubuntu versions in favor of Canonical Ubuntu packages.

<!--

#### I need to install old (unsupported) .NET versions

TODO

#### I need to install .NET preview versions

TODO

#### I need to install a newer .NET SDK feature band (> x.x.1xx)

TODO

#### I need to install .NET on an Arm based system

TODO

#### I need to install .NET on a IBM System Z or POWER platform

TODO

#### I want to use an APT/`.deb` based installation method

TODO

-->
---

(dotnet-installation-snap)=
### Installing .NET with the `dotnet` snap

Install the `dotnet` snap:

```text
sudo snap install --classic --edge dotnet
```

Now you are effectively done. If you run the `dotnet` command without any .NET component installed, the snap automatically installs the latest .NET LTS SDK before proceeding with the invoked command. 

#### Listing installed/available components and versions

To list components and versions that are installed or available for installation, run the following command in a terminal:

```text
dotnet-installer list
```

```{tip}
By default, unsupported (end of life) versions are not listed. To list all available versions, add the `--all` flag.
```

Example output:

```{terminal}
:scroll:
:input: dotnet-installer list
┌────────────┬────────────────────┬──────────────────────┬─────────────────────┬─────────────┐
│ Version    │ .NET Runtime       │ ASP.NET Core Runtime │ SDK                 │ End of Life │
├────────────┼────────────────────┼──────────────────────┼─────────────────────┼─────────────┤
│ .NET 9     │ Available [9.0.2]  │ Available [9.0.2]    │ Available [9.0.103] │ 5/12/2026   │
│ .NET 8 LTS │ Installed [8.0.13] │ Installed [8.0.13]   │ Installed [8.0.113] │ 11/10/2026  │
└────────────┴────────────────────┴──────────────────────┴─────────────────────┴─────────────┘
```

#### Installing .NET components

To install a .NET component, run the following command:

```text
dotnet-installer install [<component> [<versison>]]
```

Valid values for the `<component>` parameter are:
- `runtime`: installs the .NET runtime (without the components needed to run ASP\.NET Core apps)
- `aspnetcore-runtime`: installs the ASP\.NET Core runtime
- `sdk` (default): installs the .NET SDK (including the .NET runtime with the components needed to run ASP\.NET Core apps)

Valid values for the `<version>` parameter are:
- `lts`: installs the latest .NET LTS release
- `latest` (default): installs the latest .NET release
- `9.0`: installs .NET 9.0
- `9`:  installs .NET 9.0
- `8.0`:  installs .NET 8.0
- `8`:  installs .NET 8.0
- `6.0`:  installs .NET 6.0
- `6`:  installs .NET 6.0

Examples:

- To install the runtime of the latest .NET release, run:
  ```text
  dotnet-installer install runtime latest
  ```
- To install the SDK of the latest .NET LTS release, run:
  ```text
  dotnet-installer remove sdk lts
  ```
- To install the .NET 8 ASP\.NET Core runtime, run:
  ```text
  dotnet-installer install aspnetcore-runtime 8
  ```
- To install the .NET 9 SDK, run:
  ```text
  dotnet-installer install sdk 9.0
  ```

#### Uninstalling .NET components

To install a .NET component, run the following command:

```text
dotnet-installer remove <component> <versison>
```

The command works similar to the `dotnet installer install` command (documented above) -- just uninstalling instead of installing. One difference to the syntax of the installation command is that the parameters `<component>` and
`<version>` are required.

#### Uninstalling the `dotnet` snap

To remove the `dotnet` snap and all installed components, run:

```text
snap remove dotnet
```

(dotnet-installation-ubuntu-packages)=
### Installing .NET from Ubuntu packages

Choose your Ubuntu version:

````{tip}
You can see your Ubuntu versions by running the following command in a terminal:
```text
lsb_release -rs
```
````

::::::{tab-set}
:sync-group: series

:::::{tab-item} 25.04
:sync: plucky

Choose the .NET version you want to install:

::::{tab-set}
:sync-group: dotnet-version

:::{tab-item} .NET 9
:sync: 9.0

<!-- Content for Ubuntu 25.04 (Plucky Puffin) and .NET 9 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`, `s390x` (aka IBM System Z), `ppc64el` (aka POWER)

```{include} /reuse/howto/dotnet-setup/dotnet-install-proposed-updates.md
```

```{include} /reuse/howto/dotnet-setup/dotnet9-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 8
:sync: 8.0

<!-- Content for Ubuntu 25.04 (Plucky Puffin) and .NET 8 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`, `s390x` (aka IBM System Z), `ppc64el` (aka POWER)

```{include} /reuse/howto/dotnet-setup/dotnet-install-proposed-updates.md
```

```{include} /reuse/howto/dotnet-setup/dotnet8-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 7
:sync: 7.0

<!-- Content for Ubuntu 25.04 (Plucky Puffin) and .NET 7 -->

.NET 7 isn't supported on 25.04 (Plucky Puffin).
:::

:::{tab-item} .NET 6
:sync: 6.0


<!-- Content for 25.04 (Plucky Puffin) and .NET 6 -->

.NET 6 isn't supported on 25.04 (Plucky Puffin).
:::

::::

:::::

:::::{tab-item} 24.10
:sync: oracular

Choose the .NET version you want to install:

::::{tab-set}
:sync-group: dotnet-version

:::{tab-item} .NET 9
:sync: 9.0

<!-- Content for Ubuntu 24.10 (Oracular Oriole) and .NET 9 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`, `s390x` (aka IBM System Z), `ppc64el` (aka POWER)

```{include} /reuse/howto/dotnet-setup/dotnet-install-proposed-updates.md
```

```{include} /reuse/howto/dotnet-setup/dotnet9-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 8
:sync: 8.0

<!-- Content for Ubuntu 24.10 (Oracular Oriole) and .NET 8 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`, `s390x` (aka IBM System Z), `ppc64el` (aka POWER)

```{include} /reuse/howto/dotnet-setup/dotnet-install-proposed-updates.md
```

```{include} /reuse/howto/dotnet-setup/dotnet8-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 7
:sync: 7.0

<!-- Content for Ubuntu 24.10 (Oracular Oriole) and .NET 7 -->

.NET 7 isn't supported on 24.10 (Oracular Oriole).
:::

:::{tab-item} .NET 6
:sync: 6.0


<!-- Content for 24.10 (Oracular Oriole) and .NET 6 -->

.NET 6 isn't supported on 24.10 (Oracular Oriole).
:::

::::

:::::

:::::{tab-item} 24.04 LTS
:sync: noble

Choose the .NET version you want to install:

::::{tab-set}
:sync-group: dotnet-version

:::{tab-item} .NET 9
:sync: 9.0

<!-- Content for Ubuntu 24.04 LTS (Noble Numbat) and .NET 9 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`, `s390x` (aka IBM System Z), `ppc64el` (aka POWER)

```{include} /reuse/howto/dotnet-setup/dotnet-install-backports-ppa.md
```

```{include} /reuse/howto/dotnet-setup/dotnet9-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 8
:sync: 8.0

<!-- Content for Ubuntu 24.04 LTS (Noble Numbat) and .NET 8 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`, `s390x` (aka IBM System Z), `ppc64el` (aka POWER)

```{include} /reuse/howto/dotnet-setup/dotnet-install-proposed-updates.md
```

```{include} /reuse/howto/dotnet-setup/dotnet8-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 7
:sync: 7.0

<!-- Content for Ubuntu 24.04 LTS (Noble Numbat) and .NET 7 -->

```{include} /reuse/howto/dotnet-setup/dotnet-version-no-longer-maintained.md
```

Available for architectures:
: `amd64` (aka `x64`), `arm64`

```{include} /reuse/howto/dotnet-setup/dotnet-install-backports-ppa.md
```

```{include} /reuse/howto/dotnet-setup/dotnet7-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 6
:sync: 6.0

<!-- Content for Ubuntu 24.04 LTS (Noble Numbat) and .NET 6 -->

```{include} /reuse/howto/dotnet-setup/dotnet-version-no-longer-maintained.md
```

Available for architectures:
: `amd64` (aka `x64`), `arm64`

```{include} /reuse/howto/dotnet-setup/dotnet-install-backports-ppa.md
```

```{include} /reuse/howto/dotnet-setup/dotnet6-apt-install-ubuntu-package.md
```
:::

::::

:::::

:::::{tab-item} 22.04 LTS
:sync: jammy

Choose the .NET version you want to install:

::::{tab-set}
:sync-group: dotnet-version

:::{tab-item} .NET 9
:sync: 9.0

<!-- Content for Ubuntu 22.04 LTS (Jammy Jellyfish) and .NET 9 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`, `s390x` (aka IBM System Z), `ppc64el` (aka POWER)

```{include} /reuse/howto/dotnet-setup/dotnet-install-backports-ppa.md
```

```{include} /reuse/howto/dotnet-setup/dotnet9-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 8
:sync: 8.0

<!-- Content for Ubuntu 22.04 LTS (Jammy Jellyfish) and .NET 8 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`, `s390x` (aka IBM System Z), `ppc64el` (aka POWER)

```{include} /reuse/howto/dotnet-setup/dotnet-install-proposed-updates.md
```

```{include} /reuse/howto/dotnet-setup/dotnet8-apt-install-ubuntu-package.md
```
:::


:::{tab-item} .NET 7
:sync: 7.0

<!-- Content for Ubuntu 22.04 LTS (Jammy Jellyfish) and .NET 7 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`

```{include} /reuse/howto/dotnet-setup/dotnet-install-proposed-updates.md
```

```{include} /reuse/howto/dotnet-setup/dotnet7-apt-install-ubuntu-package.md
```
:::

:::{tab-item} .NET 6
:sync: 6.0


<!-- Content for Ubuntu 22.04 LTS (Jammy Jellyfish) and .NET 6 -->

Available for architectures:
: `amd64` (aka `x64`), `arm64`

```{include} /reuse/howto/dotnet-setup/dotnet-install-proposed-updates.md
```

```{include} /reuse/howto/dotnet-setup/dotnet6-apt-install-ubuntu-package.md
```
:::

::::

:::::

::::::

(dotnet-install-proposed-updates)=
#### Installing proposed .NET updates 

This section shows how to install proposed updates for Ubuntu .NET packages from the Ubuntu archive. 

##### Motivation

Every .NET release that does not contain security fixes has to follow the Ubuntu [stable release update (SRU) process](https://documentation.ubuntu.com/sru/en/latest/). This process delays the deployment of .NET releases by at least a week and sometimes much longer (depending on the backlog of the SRU reviewers).

If you want to install new .NET releases as soon as they are available, you can configure APT to install the proposed updates to skip this delay.

```{note}
Canonical is collaborating with Microsoft and other .NET partners..NET releases are thoroughly tested before they are uploaded to the Ubuntu archive. Historically, no significant regressions were reported for .NET proposed updates. Therefore, the risk of installing proposed updates for .NET can be considered minimal or at least insignificantly small compared to waiting for the SRU completion.
```

##### Adding the Ubuntu proposed updates APT repository

First add the Ubuntu proposed updates APT repository as a source for APT to install updates from.

If the file `/etc/apt/sources.list.d/ubuntu.sources` exists on your system, add `<release>-proposed` to the `Suites:` line. For example:

```text
Types: deb
URIs: http://archive.ubuntu.com/ubuntu
Suites: noble noble-updates noble-backports noble-proposed
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

Otherwise, modify the software sources manually by adding the proposed archive to your APT sources:

- for `amd64` (aka `x64`) systems:
  
  ```text
  sudo tee /etc/apt/sources.list.d/ubuntu-$(lsb_release -cs)-proposed.list >/dev/null <<EOF
  # Enable Ubuntu proposed archive
  deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -cs)-proposed restricted main multiverse universe
  EOF
  ```

- for `arm64`, `s390x` (aka IBM System Z) or `ppc64el` (aka POWER) systems 

  ```text
  sudo tee /etc/apt/sources.list.d/ubuntu-$(lsb_release -cs)-proposed.list >/dev/null <<EOF
  # Enable Ubuntu proposed archive
  deb http://ports.ubuntu.com/ubuntu-ports $(lsb_release -cs)-proposed restricted main multiverse universe
  EOF
  ```

Now update APT to fetch the package index from the added archive:

```text
sudo apt update
```

````{important}
If using Ubuntu 22.04 or lower, configure APT to not install proposed updates by default. This is already the default since Ubuntu 24.04. Otherwise APT installs proposed updates for all packages.

```text
sudo tee /etc/apt/preferences.d/proposed-updates >/dev/null <<EOF
# Configure apt to allow selective installs of packages from proposed
Package: *
Pin: release a=$(lsb_release -cs)-proposed
Pin-Priority: 400
EOF
```
````

##### Configuring APT to install proposed .NET updates

Finally, configure APT to consider .NET packages from the proposed archive for installation: 

```text
sudo tee /etc/apt/preferences.d/dotnet-proposed-updates >/dev/null <<EOF
# Configure apt to install dotnet packages from proposed
Package: src:dotnet*
Pin: release a=$(lsb_release -cs)-proposed
Pin-Priority: 500
EOF
```

##### Disabling installation of proposed updates

To stop the package management system from installing proposed .NET updates:

1. Delete the configuration you created.
2. Update the APT package index:

   ```text
   sudo apt update
   ```

````{note}
Already installed proposed updates remain installed. To remove them, uninstall and re-install the affected packages.
````

(dotnet-installation-microsoft-packages)=
### Installing .NET from Microsoft packages

<!-- 

TODO: add doumentation about conflicts with Ubuntu provided packages 
      and how to resolve them
-->
For this installation method, see Microsoft's documentation: [Install .NET SDK or .NET Runtime on Ubuntu](https://learn.microsoft.com/en-us/dotnet/core/install/linux-ubuntu-install).

(dotnet-installation-microsoft-script)=
### Installing .NET with the Microsoft installation script

For this installation method, see Microsoft's documentation: [Install .NET on Linux by using an install script or by extracting binaries](https://learn.microsoft.com/en-us/dotnet/core/install/linux-scripted-manual).

(dotnet-installation-microsoft-manual)=
### Installing .NET manually

For this installation method, see Microsoft's documentation: [Manual install](https://learn.microsoft.com/en-us/dotnet/core/install/linux-scripted-manual#manual-install).


## Checking installed versions and components

To display installed .NET SDKs, runtimes, and other useful information, run the following command:

```text
dotnet --info
```

To list installed .NET SDKs, run the following command:

```text
dotnet --list-sdks
```

To list installed .NET runtimes, run the following command:

```text
dotnet --list-runtimes
```

Example output:

```{terminal}
:input: dotnet --info
.NET SDK:
 Version:           8.0.113
 Commit:            67977f6ab7
 Workload version:  8.0.100-manifests.bbbf61fd

Runtime Environment:
 OS Name:     ubuntu
 OS Version:  24.04
 OS Platform: Linux
 RID:         ubuntu.22.04-x64
 Base Path:   /var/snap/dotnet/common/dotnet/sdk/8.0.113/

.NET workloads installed:
 Workload version: 8.0.100-manifests.bbbf61fd
There are no installed workloads to display.

Host:
  Version:      9.0.1
  Architecture: x64
  Commit:       1cf154a56d

.NET SDKs installed:
  8.0.113 [/var/snap/dotnet/common/dotnet/sdk]

.NET runtimes installed:
  Microsoft.AspNetCore.App 8.0.13 [/var/snap/dotnet/common/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.NETCore.App 8.0.13 [/var/snap/dotnet/common/dotnet/shared/Microsoft.NETCore.App]

Other architectures found:
  None

Environment variables:
  Not set

global.json file:
  Not found

Learn more:
  https://aka.ms/dotnet/info

Download .NET:
  https://aka.ms/dotnet/download

:input: dotnet --list-sdks
8.0.113 [/var/snap/dotnet/common/dotnet/sdk]

:input: dotnet --list-runtimes
Microsoft.AspNetCore.App 8.0.13 [/var/snap/dotnet/common/dotnet/shared/Microsoft.AspNetCore.App]
Microsoft.NETCore.App 8.0.13 [/var/snap/dotnet/common/dotnet/shared/Microsoft.NETCore.App]
```

## Setting up a .NET IDE

Many editors and IDEs (Integrated Development Environment) come with various degrees of support for .NET workloads. Here are some popular ones:

### JetBrains Rider

JetBrains Rider currently offers the best developer experience for .NET projects on Linux. It integrates extensive debugging and profiling tools. It is free for non-commercial use.

To install [JetBrains Rider](https://snapcraft.io/rider), run the following command:

```text
sudo snap install rider --classic
```

### Visual Studio Code

The following popular .NET extensions are available for VS Code:

```{list-table}
   :header-rows: 1

  * - Extension
    - Description
    - Terms
  * - [C#](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp):
    - Base language support for C#
    - free
  * - [C# {spellexception}`Dev` Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
    - Extended language support and builds on top of the "C#" extension
    - - free for individuals, academia, and open-source development
      - paid for organizations
      
      see [details](https://aka.ms/vs/csdevkit/license)
  * - [Ionide for F#](https://marketplace.visualstudio.com/items?itemName=Ionide.Ionide-fsharp)
    - F# language support
    - free
```
  
To install [VS Code](https://snapcraft.io/code) run the following command:

```text
sudo snap install code --classic
```

### VS Codium

The following popular .NET extensions are available for VS Codium:

```{list-table}
   :header-rows: 1

  * - Extension
    - Description
    - Terms
  * - [C#](https://open-vsx.org/extension/muhammad-sammy/csharp):
    - Base language support for C# 
    
      (fork of the Microsoft extension that replaces the proprietary debugger with Samsung's FOSS .NET debugger)
    - free
  * - [Ionide for F#](https://open-vsx.org/extension/Ionide/Ionide-fsharp)
    - F# language support
    - free
```

To install [VS Codium](https://snapcraft.io/codium), run the following command:

```text
sudo snap install codium --classic
```


## What next

See the tutorial introducing the use of .NET and related tooling: {ref}`use-dotnet`.
