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

Contribute documentation <howto/contribute-docs.md>
:::

**Ubuntu is a Linux-based operating system and development platform.** Python, Go, Rust, GCC, Clang, .NET, Java, and Zig toolchains are available through Ubuntu repositories and snaps, with build tools, debuggers, linters, formatters, and IDEs.

**This documentation guides developers from a fresh Ubuntu Desktop install to a productive development setup.** It covers toolchain installation, first-program tutorials, version-reference data, and background context. It does not teach programming; no prior Ubuntu experience is required.


## In this documentation

The following sections organize the documentation by development activity — installing, working, and distributing — so you can find content by what you are trying to do.


### Installing

Set up Ubuntu Desktop, configure version control, and install any of the supported toolchains.

* **System**: {ref}`Installing Ubuntu Desktop for developers <install-ubuntu>` • {ref}`Using Git version control on Ubuntu <use-git>`
* **Python**: {ref}`Install and set up Python <install-python>` • {ref}`Available Python versions <python-toolchain-availability>`
* **Go**: {ref}`Install and set up Go <install-golang>` • {ref}`Available Golang versions <go-toolchain-availability>`
* **Rust**: {ref}`Install and set up Rust <install-rust>` • {ref}`Available Rust versions <rust-toolchain-availability>`
* **GCC**: {ref}`Install and set up GCC <install-gcc>` • {ref}`Available GCC versions <gcc-toolchain-availability>`
* **Clang**: {ref}`Install and set up Clang <install-clang>` • {ref}`Available LLVM/Clang versions <llvm-toolchain-availability>`
* **.NET**: {ref}`Install and set up .NET <install-dotnet>` • {ref}`Available .NET versions <dotnet-toolchain-availability>`
* **Java**: {ref}`Install and set up Java <install-java>` • {ref}`Available Java versions <java-toolchain-availability>`
* **Zig**: {ref}`Install and set up Zig <install-zig>` • {ref}`Available Zig versions <zig-toolchain-availability>`


### Working

Build, run, and debug code with each toolchain, and use IDEs and supporting tools on Ubuntu Desktop.

* **Python**: {ref}`Develop with Python <use-python>`
* **Go**: {ref}`Develop with Go <use-go>`
* **Rust**: {ref}`Develop with Rust <use-rust>`
* **GCC**: {ref}`Develop with GCC <use-gcc>`
* **Clang**: {ref}`Develop C and C++ with Clang <use-clang>`
* **.NET**: {ref}`Develop with .NET <use-dotnet>` • {ref}`Introduction to the .NET toolchain <dotnet-introduction>` • {ref}`Debugging with .NET <debugging-with-dotnet>`
* **Java**: {ref}`Develop with Java <use-java>` • {ref}`GraalVM native compilation <graalvm-introduction>` • {ref}`Compile Spring Boot apps to native executables <use-graalvm>` • {ref}`Fast start for Spring Boot apps with CRaC <use-crac>`
* **Zig**: {ref}`Develop with Zig <use-zig>`
* **IDEs**: {ref}`Integrated developer environments <ides>`


### Distributing

Package software built on Ubuntu for distribution.

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

* [Code of conduct](https://ubuntu.com/community/ethos/code-of-conduct)


### Commercial support

Thinking about using Ubuntu Desktop as your development platform? See [Ubuntu Desktop for developers](https://ubuntu.com/desktop/developers).
