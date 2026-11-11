---
myst:
  html_meta:
    description: ".NET versions available in Ubuntu releases, with source packages and support status."
---

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

The [`dotnet` snap](https://snapcraft.io/dotnet) lets you install .NET components of the following versions on Ubuntu 22.04 LTS and above for `amd64` and `arm64` architectures.

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
  - lets you build and run .NET apps
* - ASP\.NET Core Runtime
  - ```none
    aspnetcore-runtime
    ```
  - lets you run .NET apps (including ASP\.NET Core apps)
* - .NET Runtime
  - ```none
    runtime
    ```
  - lets you run .NET apps (without the components needed to run ASP\.NET Core apps)
````

(dotnet-snap-versions)=
### Versions

````{list-table}
:header-rows: 1

* - .NET version
  - identifiers
  - End of Life
* - .NET 11 (STS)
  - ```none
    latest
    ```
    ```none
    11
    ```
    ```none
    11.0
    ```
  - 14 November 2028
* - .NET 10 (LTS)
  - ```none
    lts
    ```
    ```none
    10
    ```
    ```none
    10.0
    ```
  - 14 November 2028
* - .NET 9 (STS, end of life)
  - ```none
    9
    ```
    ```none
    9.0
    ```
  - 10 November 2026
* - .NET 8 (LTS, end of life)
  - ```none
    8
    ```
    ```none
    8.0
    ```
  - 10 November 2026
* - .NET 6 (LTS, end of life)
  - ```none
    6
    ```
    ```none
    6.0
    ```
  - 12 November 2024
````

End-of-life versions can still be installed with the snap, but `dotnet-installer list` only shows them when you add the `--all` flag.

```{note}
.NET 7 isn't available through the `dotnet` snap. It was already out of support when the snap was created, and only a .NET Runtime content snap exists for it, without an ASP\.NET Core Runtime or SDK.
```

See: {ref}`dotnet-installation-snap`

## Ubuntu (deb) packages

| Ubuntu version              | `amd64` | `arm64` | `s390x` | `ppc64el` |
|-----------------------------|---------|---------|---------|-----------|
| 26.10 (Stonking Stingray)   | **10**, 11 | **10**, 11 | **10**, 11 | **10**, 11 |
| 26.04 LTS (Resolute Raccoon) | 8{dim}`¹ ²`, 9{dim}`¹ ²`, **10**, 11{dim}`¹` | 8{dim}`¹ ²`, 9{dim}`¹ ²`, **10**, 11{dim}`¹` | 8{dim}`¹ ²`, 9{dim}`¹ ²`, **10**, 11{dim}`¹` | 8{dim}`¹ ²`, 9{dim}`¹ ²`, **10**, 11{dim}`¹` |
| 24.04 LTS (Noble Numbat)    | 6{dim}`¹ ²`, 7{dim}`¹ ²`, **8**{dim}`²`, 9{dim}`¹ ²`, **10**, 11{dim}`¹` | 6{dim}`¹ ²`, 7{dim}`¹ ²`, **8**{dim}`²`, 9{dim}`¹ ²`, **10**, 11{dim}`¹` | **8**{dim}`²`, 9{dim}`¹ ²`, **10**, 11{dim}`¹` | **8**{dim}`²`, 9{dim}`¹ ²`, **10**, 11{dim}`¹` |
| 22.04 LTS (Jammy Jellyfish) | **6**{dim}`²`, 7{dim}`²`, **8**{dim}`²`, 9{dim}`¹ ²`, 10{dim}`¹`, 11{dim}`¹` | **6**{dim}`²`, 7{dim}`²`, **8**{dim}`²`, 9{dim}`¹ ²`, 10{dim}`¹`, 11{dim}`¹` | **8**{dim}`²`, 9{dim}`¹ ²`, 10{dim}`¹`, 11{dim}`¹` | **8**{dim}`²`, 9{dim}`¹ ²`, 10{dim}`¹`, 11{dim}`¹` |

<!-- Do not forget to add 4 spaces at the end of line to keep future diffs more readable -->
**bold** -- package is in main    
¹ -- available in the {ref}`dotnet-backports-ppa` only    
² -- version is no longer maintained by Canonical (End of Life)    

| .NET Version | Source package | End of Life (Upstream) | 
|--------------|----------------|------------------------|
| .NET 11 (STS) | {lpsrc}`dotnet11` | 14 November 2028 |
| .NET 10 (LTS) | {lpsrc}`dotnet10` | 14 November 2028 |
| .NET 9 (STS) | {lpsrc}`dotnet9` | 10 November 2026 |
| .NET 8 (LTS) | {lpsrc}`dotnet8` | 10 November 2026 |
| .NET 7 (STS) | {lpsrc}`dotnet7` | 14 May 2024 |
| .NET 6 (LTS) | {lpsrc}`dotnet6` | 12 November 2024 |

LTS -- Long Term Support (Upstream patches bugs for 3 years after release)    
STS -- Standard Term Support (Upstream patches bugs for 2 years after release)

See: {ref}`dotnet-installation-ubuntu-packages`

(dotnet-debug-packages)=
### .NET Debug Symbols packages

:::{list-table}
   :header-rows: 1

  * - .NET Version
    - available Debug Symbols packages
  * - .NET 11
    - ```text
      dotnet-sdk-dbg-11.0
      ```
      ```text
      dotnet-runtime-dbg-11.0
      ```
      ```text
      aspnetcore-runtime-dbg-11.0
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
:::

(dotnet-backports-ppa)=
### Backports PPA

.NET versions which Canonical is not committed to maintain for the entire lifetime of an Ubuntu release will be provided via the [.NET backports PPA](https://launchpad.net/~dotnet/+archive/ubuntu/backports).

Canonical provides best-effort maintenance for packages contained in this archive, which is limited to the upstream lifespan of the .NET version or the support period of the particular Ubuntu series. See the [upstream support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) for more information about the upstream support lifespan of .NET releases or the [list of Ubuntu releases](https://documentation.ubuntu.com/project/release-team/list-of-releases) for more information about the support period of any Ubuntu series.

(dotnet-previews-ppa)=
### Previews PPA

Before each major .NET release, Microsoft publishes multiple previews for public testing. We package and test these previews in the [.NET previews PPA](https://launchpad.net/~dotnet/+archive/ubuntu/previews) to prepare for the final release. We encourage you to try them out and share your feedback.

```{important}
These builds are not intended for production environments. Neither Microsoft nor Canonical provides warranties or support for these preview versions.
```
