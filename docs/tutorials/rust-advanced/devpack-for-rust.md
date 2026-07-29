---
myst:
  html_meta:
    description: "Use devpack-for-rust to install a Rust toolchain, an IDE, and Rust-friendly CLI tools on Ubuntu through one interactive wizard."
---

(devpack-for-rust)=
# Devpack for Rust

This tutorial shows how to use {pkg}`devpack-for-rust` to install a Rust toolchain, an IDE, and a set of Rust-friendly command-line tools on Ubuntu through a single interactive wizard. The devpack automates environment setup so that a fresh Ubuntu installation goes from zero to a working Rust development environment in one run.

For background on devpacks, see {ref}`devpacks`. For manual instructions on installing the Rust toolchain, see {ref}`install-rust`.


## Installing the devpack

{pkg}`devpack-for-rust` is distributed as a classic-confinement snap. Install it with:

```{terminal}
:user: dev
:host: ubuntu

sudo snap install devpack-for-rust --classic --channel latest/edge
```


## Running the setup wizard

{pkg}`devpack-for-rust` is a single interactive wizard with no subcommands. Start it by running the snap command:

```{terminal}
:user: dev
:host: ubuntu

devpack-for-rust
```

The wizard displays a selection tree with three choice groups. Navigate the tree, pick the items you want, and confirm the **All done?** node to run the installation. The three groups are:

- **Pick a Rust channel** (required, choose one): {command}`stable`, {command}`beta`, or {command}`nightly`. The wizard uses Rustup to set the default channel. If Rustup is not already installed, the wizard installs the {pkg}`rustup` snap first (with classic confinement), then runs {command}`rustup default <channel>`.
- **Pick an IDE?** (required, choose one): install one editor as a classic snap.
  - [Helix](https://helix-editor.com/) -- a post-modal text editor.
  - [VS Code](https://code.visualstudio.com/) -- a general-purpose editor with strong Rust support through the rust-analyzer extension.
  - [RustRover](https://www.jetbrains.com/rust/) -- JetBrains' IDE for Rust.
- **Oxidize your tooling?** (optional, choose any): install Rust-friendly command-line utilities through apt.
  - [du-dust](https://github.com/bootandy/dust) -- a more intuitive alternative to {command}`du`.
  - [fd-find](https://github.com/sharkdp/fd) -- a fast, user-friendly alternative to {command}`find`. The Ubuntu package ships the binary as {command}`fdfind`; the wizard offers an optional {command}`fd` alias.
  - [ripgrep](https://github.com/BurntSushi/ripgrep) -- a fast recursive directory searcher. The Ubuntu package ships the binary as {command}`ripgrep`; the wizard offers an optional {command}`rg` alias.
  - [sd](https://github.com/chmln/sd) -- an intuitive find-and-replace CLI.

:::{note}
The wizard prompts for the {command}`fd` and {command}`rg` aliases as child nodes of the corresponding tool. Selecting a tool without its alias node installs the package but does not create the shortcut.
:::

:::{note}
For tools with an alias, the wizard auto-detects your shell and writes the alias to the corresponding config file (for example, {file}`~/.bash_aliases` for Bash or {file}`~/.zshrc` for Zsh).
:::


## Command-line options

- {command}`-d`, {command}`--dry-run` -- print what the wizard will do without executing any commands.
- {command}`-C`, {command}`--continue-after-failure` -- continue with remaining recipes after one fails.
- {command}`-S`, {command}`--override-shell-type <bash|posix|fish|zsh>` -- override automatic shell detection for alias placement.
- {command}`-v` / {command}`-vv` -- increase log verbosity (warnings by default; informational with {command}`-v`, debug with {command}`-vv`).


## Verifying the installation

To confirm the Rust toolchain is installed, check the compiler and package manager versions:

```{terminal}
:user: dev
:host: ubuntu

rustc --version
cargo --version
```

To build and run a first Rust project, follow the step-by-step tutorial at {ref}`use-rust`.


## What next

- {ref}`install-rust`
- {ref}`use-rust`
- {ref}`devpacks`


## Additional resources

- [devpack-for-rust source repository](https://github.com/canonical/devpack-for-rust)
