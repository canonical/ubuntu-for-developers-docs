---
myst:
  html_meta:
    description: "Set up Python, Go, Rust, GCC, Clang, .NET, Java, and Zig toolchains on Ubuntu Desktop."
---

(ubuntu-for-developers)=
# Ubuntu for developers

:::{toctree}
---
maxdepth: 2
hidden: true
---
tutorials/index
howto/index
reference/index
explanation/index
toolchains/index

Contribute documentation <howto/contribute-docs.md>
:::

**Ubuntu is a Linux-based operating system and development platform.** Python, Go, Rust, GCC, Clang, .NET, Java, and Zig toolchains are available through Ubuntu repositories and snaps, with build tools, debuggers, linters, formatters, and IDEs.

**This documentation guides developers from a fresh Ubuntu Desktop install to a productive development setup.** It covers toolchain installation, first-program tutorials, version-reference data, and background context. It does not teach programming; no prior Ubuntu experience is required.


## In this documentation

The following sections map the documentation by lifecycle stage – from platform basics and setup through toolchain installation and active development – so you can find content by where it falls in your workflow.


### Introduction

Pages covering platform-level setup and Ubuntu-specific concepts that apply across all toolchains.

* **The basics**: {ref}`Overview <explanation>` • {ref}`Installing Ubuntu Desktop for developers <install-ubuntu>` • {ref}`Using Git version control on Ubuntu <use-git>` • {ref}`Integrated developer environments <ides>`


### Language toolchains and support

Each supported language has its own installation guide, first-program tutorial, and version availability reference.

* **{ref}`Python <python-on-ubuntu>`**: {ref}`Install <install-python>` | {ref}`Tutorial <use-python>` | {ref}`Available versions <python-toolchain-availability>`
* **{ref}`Go <go-on-ubuntu>`**: {ref}`Install <install-golang>` | {ref}`Tutorial <use-go>` | {ref}`Available versions <go-toolchain-availability>`
* **{ref}`Rust <rust-on-ubuntu>`**: {ref}`Install <install-rust>` | {ref}`Tutorial <use-rust>` | {ref}`Available versions <rust-toolchain-availability>`
* **{ref}`GCC <gcc-on-ubuntu>`**: {ref}`Install <install-gcc>` | {ref}`Tutorial <use-gcc>` | {ref}`Available versions <gcc-toolchain-availability>`
* **{ref}`Clang <clang-on-ubuntu>`**: {ref}`Install <install-clang>` | {ref}`Tutorial <use-clang>` | {ref}`Available versions <llvm-toolchain-availability>`
* **{ref}`.NET <dotnet-on-ubuntu>`**: {ref}`Install <install-dotnet>` | {ref}`Tutorial <use-dotnet>` | {ref}`Available versions <dotnet-toolchain-availability>` | {ref}`Debugging <debugging-with-dotnet>`
* **{ref}`Java <java-on-ubuntu>`**: {ref}`Install <install-java>` | {ref}`Tutorial <use-java>` | {ref}`Available versions <java-toolchain-availability>` | {ref}`Advanced <java-advanced>`
* **{ref}`Zig <zig-on-ubuntu>`**: {ref}`Install <install-zig>` | {ref}`Tutorial <use-zig>` | {ref}`Available versions <zig-toolchain-availability>`


### Packaging and distribution

Distribute software built on Ubuntu as packages, snaps, or container images.

* **Packaging**: {ref}`Packaging software <packaging>`


## How this documentation is organized

This documentation uses the [Diátaxis documentation structure](https://diataxis.fr/).

* {ref}`Tutorials <tutorials>` guide you through developing a 'Hello, world!' application with each toolchain on Ubuntu Desktop, and demonstrate the use of debuggers, linters, and other supporting tools.
* {ref}`How-to guides <howto>` cover the installation and configuration of each toolchain and its supporting tooling on Ubuntu Desktop.
* {ref}`Reference <reference>` covers toolchain version availability across Ubuntu releases and lists supported integrated development environments.
* {ref}`Explanation <explanation>` discusses Ubuntu installation considerations, version-control setup, packaging, and toolchain-specific background.


## Project and community

Ubuntu Desktop is part of the Ubuntu family of open-source projects, developed and maintained by Canonical and a worldwide community of contributors.


### Get involved

* [Ask Ubuntu](https://askubuntu.com/)
* [Matrix channel](https://matrix.to/#/#discuss:ubuntu.com)
* [Issue tracker](https://github.com/canonical/ubuntu-for-developers-docs/issues/new)
* {ref}`Contribution guide <contribute-docs>`


### Governance and policies

* {external+project:ref}`code-of-conduct`


### Commercial support

Thinking about using Ubuntu Desktop as your development platform? See [Ubuntu Desktop for developers](https://ubuntu.com/desktop/developers).
