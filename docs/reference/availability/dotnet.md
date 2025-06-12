(dotnet-toolchain-availability)=
# Available .NET versions

```{raw} html
<style>
    .dim {
        opacity: 0.65;
    }
</style>
```

```{role} dim
```

This article lists Canonical maintained .NET builds.

## .NET Snap

The [`dotnet` snap](https://snapcraft.io/dotnet) let's you install .NET components of the following versions on Ubuntu 22.04+ for `amd64` and `arm64` architectures.

(dotnet-snap-components)=
### Components

````{list-table}
:header-rows: 1

* - .NET component
  - identifier
  - description
* - .NET SDK 
  - ```none
    sdk
    ```
  - let's you build and run .NET apps
* - ASP\.NET Core Runtime
  - ```none
    aspnetcore-runtime
    ```
  - let's you run .NET apps (including ASP\.NET Core apps)
* - .NET Runtime
  - ```none
    runtime
    ```
  - let's you run .NET apps (without the components needed to run ASP\.NET Core apps)
````

(dotnet-snap-versions)=
### Versions

````{list-table}
:header-rows: 1

* - .NET version
  - identifiers
  - End of Life
* - .NET 9 (STS)
  - ```none
    latest
    ```
    ```none
    9
    ```
    ```none
    9.0
    ```
  - 12 May 2026
* - .NET 8 (LTS)
  - ```none
    lts
    ```
    ```none
    8
    ```
    ```none
    8.0
    ```
  - 10 November 2026
* - .NET 7 (STS)
  - ```none
    7
    ```
    ```none
    7.0
    ```
  - 14 May 2024
* - .NET 6 (LTS)
  - ```none
    6
    ```
    ```none
    6.0
    ```
  - 12 November 2024
````

See: {ref}`dotnet-installation-snap`

## Ubuntu (deb) packages

| Ubuntu version              | `amd64` | `arm64` | `s390x` | `ppc64el` |
|-----------------------------|---------|---------|---------|-----------|
| 25.10 (Questing Quokka)     | **8**, 9, 10{dim}`³` | **8**, 9, 10{dim}`³` | **8**, 9 | **8**, 9 |
| 25.04 (Plucky Puffin)       | **8**, 9, 10{dim}`³` | **8**, 9, 10{dim}`³` | **8**, 9 | **8**, 9 |
| 24.10 (Oracular Oriole)     | **8**, 9 | **8**, 9 | **8**, 9 | **8**, 9 |
| 24.04 LTS (Noble Numbat)    | 6{dim}`¹ ²`, 7{dim}`¹ ²`, **8**, 9{dim}`¹`, 10{dim}`³` | 6{dim}`¹ ²`, 7{dim}`¹ ²`, **8**, 9{dim}`¹`, 10{dim}`³` | **8**, 9{dim}`¹` | **8**, 9{dim}`¹` |
| 22.04 LTS (Jammy Jellyfish) | **6**, 7, **8**, 9{dim}`¹`, 10{dim}`³` | **6**, 7, **8**, 9{dim}`¹`, 10{dim}`³` | **8**, 9{dim}`¹` | **8**, 9{dim}`¹` |

<!-- Do not forget to add 4 spaces at the end of line to keep future diffs more readable -->
**bold** -- package is in main    
¹ -- available in the {ref}`dotnet-backports-ppa` only    
² -- version is no longer maintained by Canonical (End of Life)    
³ -- available in the {ref}`dotnet-previews-ppa` only until final release    

```{note}
.NET 10 will be available in the Ubuntu archive for Ubuntu 24.04+ and included in main upon its official release. For Ubuntu 22.04, it will be provided via the Backports PPA.

Additionally, .NET 10 will be available for the `ppc64el` and `s390x` architectures until the final release.
```

| .NET Version | Source package | End of Life (Upstream) | 
|--------------|----------------|------------------------|
| .NET 10 preview | [dotnet10](https://launchpad.net/~dotnet/+archive/ubuntu/previews) | (not yet supported) |
| .NET 9 (STS) | {lpsrc}`dotnet9` | 12 May 2026 |
| .NET 8 (LTS) | {lpsrc}`dotnet8` | 10 November 2026 |
| .NET 7 (STS) | {lpsrc}`dotnet7` | 14 May 2024 |
| .NET 6 (LTS) | {lpsrc}`dotnet6` | 12 November 2024 |

LTS -- Long Term Support (Upstream patches bugs for 36 months after release)    
STS -- Standard Term Support (Upstream patches bugs for 18 month after release)

See: {ref}`dotnet-installation-ubuntu-packages`

(dotnet-debug-packages)=
### .NET Debug Symbols packages

:::{list-table}
   :header-rows: 1

  * - .NET Version
    - available Debug Symbols packages
  * - .NET 8
    - ```text
      dotnet-sdk-dbg-8.0
      ```
      ```text
      dotnet-runtime-dbg-8.0
      ```
      ```text
      aspnetcore-runtime-dbg-8.0
      ```
  * - .NET 9
    - ```text
      dotnet-sdk-dbg-9.0
      ```
      ```text
      dotnet-runtime-dbg-9.0
      ```
      ```text
      aspnetcore-runtime-dbg-9.0
      ```
  * - .NET 10
    - ```text
      dotnet-sdk-dbg-10.0
      ```
      ```text
      dotnet-runtime-dbg-10.0
      ```
      ```text
      aspnetcore-runtime-dbg-10.0
      ```
:::

(dotnet-backports-ppa)=
### Backports PPA

.NET versions which Canonical is not committed to maintain for the entire lifetime of an Ubuntu release will be provided via the [.NET backports PPA](https://launchpad.net/~dotnet/+archive/ubuntu/backports).

Canonical provides best-effort maintenance for packages contained in this archive, which is limited to the upstream lifespan of the .NET version or the support period of the particular Ubuntu series. See the [upstream support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) for more information about the upstream support lifespan of .NET releases or the [Ubuntu Releases Wiki entry](https://wiki.ubuntu.com/Releases) for more information about the support period of any Ubuntu series.

(dotnet-previews-ppa)=
### Previews PPA

Before each major .NET release, Microsoft publishes multiple previews for public testing. We package and test these previews in the [.NET previews PPA](https://launchpad.net/~dotnet/+archive/ubuntu/previews) to prepare for the final release. We encourage you to try them out and share your feedback.

```{important}
These builds are not intended for production environments. Neither Microsoft nor Canonical provides warranties or support for these preview versions.
```
