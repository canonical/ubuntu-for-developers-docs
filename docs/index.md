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

Contribute documentation <howto/contribute-docs.md>
:::

**Ubuntu is a Linux-based operating system that provides a complete development platform supporting multiple programming languages and toolchains.**

**Each supported toolchain integrates with Ubuntu's package management and tooling ecosystem.** Python, Go, Rust, GCC, Clang, .NET, and Java are available through Ubuntu repositories and snaps, together with build tools, debuggers, linters, formatters, and IDEs (integrated development environments).

**This documentation reduces the time needed to configure a working development environment on Ubuntu.** It covers toolchain installation, first-program tutorials, version-reference data, and background context, providing a path from a fresh Ubuntu Desktop install to a productive development setup.

**The documentation is for developers who use or plan to use Ubuntu Desktop as their workstation.** It does not teach programming; it shows how to install toolchains, build first programs, and use supporting tools on Ubuntu Desktop. No prior Ubuntu experience is required.


## In this documentation

The following sections map the documentation by development lifecycle stage — from environment setup and toolchain installation through active development to software distribution.

**Tutorial**: {ref}`Develop with Python <use-python>`


### Initialization and setup

Setting up development on Ubuntu Desktop involves platform-level choices and toolchain-specific configuration.

* **System preparation**: {ref}`Installing Ubuntu Desktop for developers <install-ubuntu>` • {ref}`Using Git version control on Ubuntu <use-git>`
* **Editor selection**: {ref}`Integrated developer environments <ides>`
* **Toolchain configuration**: {ref}`Install and set up Python <install-python>` • {ref}`Install and set up Go <install-golang>` • {ref}`Install and set up Rust <install-rust>` • {ref}`Install and set up GCC <install-gcc>` • {ref}`Install and set up Clang <install-clang>` • {ref}`Install and set up .NET <install-dotnet>` • {ref}`Install and set up Java <install-java>`


### Active development

These pages cover the toolchain-specific workflows for building, running, and debugging code on Ubuntu Desktop.

* **First programs**: {ref}`Develop with Go <use-go>` • {ref}`Develop with Rust <use-rust>` • {ref}`Develop with GCC <use-gcc>` • {ref}`Develop C and C++ with Clang <use-clang>` • {ref}`Develop with .NET <use-dotnet>` • {ref}`Develop with Java <use-java>`
* **.NET ecosystem**: {ref}`Introduction to the .NET toolchain <dotnet-introduction>` • {ref}`Debugging with .NET <debugging-with-dotnet>`
* **Java ecosystem**: {ref}`Compile Spring Boot apps to native executables <use-graalvm>` • {ref}`GraalVM native compilation <graalvm-introduction>` • {ref}`Fast start for Spring Boot apps with CRaC <use-crac>`


### Evolution and packaging

This section covers distributing software built on Ubuntu Desktop as a Debian package, snap, or container image.

* **Software distribution**: {ref}`Packaging software <packaging>`


### Resources and references

Version matrices for each supported toolchain, showing what is available across Ubuntu releases.

* **Toolchain availability**: {ref}`Python <python-toolchain-availability>` • {ref}`Go <go-toolchain-availability>` • {ref}`Rust <rust-toolchain-availability>` • {ref}`GCC <gcc-toolchain-availability>` • {ref}`LLVM/Clang <llvm-toolchain-availability>` • {ref}`.NET <dotnet-toolchain-availability>` • {ref}`Java <java-toolchain-availability>`


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

* [Code of conduct](https://ubuntu.com/community/ethos/code-of-conduct)


### Commercial support

Thinking about using Ubuntu Desktop as your development platform? See [Ubuntu Desktop for developers](https://ubuntu.com/desktop/developers).
