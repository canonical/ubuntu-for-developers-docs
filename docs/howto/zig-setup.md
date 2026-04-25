---
myst:
  html_meta:
    description: "Install Zig and set up a development environment on Ubuntu Desktop."
---

(install-zig)=
# How to set up a development environment for Zig on Ubuntu

This guide covers installing the Zig toolchain and setting up a development environment on Ubuntu. [Zig](https://ziglang.org/) is a general-purpose systems programming language designed for robustness, performance, and simplicity, with built-in cross-compilation support.


## Installing Zig

There are two main options for installing Zig on Ubuntu:

* Using Ubuntu packages from the Ubuntu archive: Official packages maintained by the Ubuntu team and installed through the Ubuntu package-management system. Packages are available from **Ubuntu 25.10** onward. Use this method on a supported release to get a system-managed installation.

* Using the [Zig snap](https://snapcraft.io/zig), a community-maintained snap package. Use this method if you need a recent Zig release on an older Ubuntu release, or want a version not yet available in the archive.


### Installing Zig from Ubuntu packages

Zig packages are available in the Ubuntu archive from Ubuntu 25.10 (Questing Quokka) onward.

1. Install the {pkg}`zig` package:

    ```{terminal}
    :dir: ~
    :user: dev
    :host: ubuntu

    sudo apt install zig
    ```

1. Verify the installation:

    ```{terminal}
    :dir: ~
    :user: dev
    :host: ubuntu

    zig version
    ```


### Installing Zig from the snap

The [Zig snap](https://snapcraft.io/zig) is a community-maintained package available for all Ubuntu releases. The `latest/beta` channel tracks Zig stable releases.

1. Install the snap from the `latest/beta` channel:

    ```{terminal}
    :dir: ~
    :user: dev
    :host: ubuntu

    sudo snap install zig --classic --channel=latest/beta
    ```

1. Verify the installation:

    ```{terminal}
    :dir: ~
    :user: dev
    :host: ubuntu

    zig version
    ```

:::{note}
The Zig snap does not currently publish a `latest/stable` channel. The `latest/beta` channel tracks the most recent Zig stable releases. The `latest/edge` channel tracks nightly development builds.
:::


## IDE integrations

Several editors and IDEs support Zig, primarily through [ZLS](https://github.com/zigtools/zls) (Zig Language Server), which provides code completion, go-to-definition, error highlighting, and other language features.

[Visual Studio Code](https://code.visualstudio.com/)
: Install VS Code from the Snap Store, then add the [Zig Language Support](https://marketplace.visualstudio.com/items?itemName=ziglang.vscode-zig) extension from the VS Code Marketplace. The extension automatically installs and manages ZLS.

  Install VS Code with:

  ```{terminal}
  :dir: ~
  :user: dev
  :host: ubuntu

  sudo snap install code --classic
  ```

[Codium](https://vscodium.com/)
: The freely-licensed binary distribution of VS Code. Install the [Zig Language Support](https://open-vsx.org/extension/ziglang/vscode-zig) extension from the Open VSX registry.

  Install Codium with:

  ```{terminal}
  :dir: ~
  :user: dev
  :host: ubuntu

  sudo snap install codium --classic
  ```

:::{note}
ZLS is managed automatically by the VS Code and Codium extensions. For other editors (Vim, {spellexception}`Neovim`, Emacs, Helix), install ZLS manually. Refer to the [ZLS installation guide](https://github.com/zigtools/zls#installation) for instructions.
:::


## What next

See the tutorial introducing the use of Zig and related tooling: {ref}`use-zig`.
