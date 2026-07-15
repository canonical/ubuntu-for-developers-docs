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

The following sections map the documentation by lifecycle stage — from platform basics and setup through toolchain installation and active development — so you can find content by where it falls in your workflow.


### Introduction

Pages covering platform-level setup and Ubuntu-specific concepts that apply across all toolchains.

* **The basics**: {ref}`Overview <explanation>` • {ref}`Installing Ubuntu Desktop for developers <install-ubuntu>` • {ref}`Using Git version control on Ubuntu <use-git>` • {ref}`Integrated developer environments <ides>`
* **Ubuntu uniqueness**: {ref}`Packaging software <packaging>` • {ref}`Toolchain availability <toolchain-availability>`


### Language toolchains and support

Each supported language has its own installation guide, first-program tutorial, and version availability reference.

* **Python**: {ref}`Install and set up Python <install-python>` • {ref}`Develop with Python <use-python>` • {ref}`Available Python versions <python-toolchain-availability>`
* **Go**: {ref}`Install and set up Go <install-golang>` • {ref}`Develop with Go <use-go>` • {ref}`Available Golang versions <go-toolchain-availability>`
* **Rust**: {ref}`Install and set up Rust <install-rust>` • {ref}`Develop with Rust <use-rust>` • {ref}`Available Rust versions <rust-toolchain-availability>`
* **GCC**: {ref}`Install and set up GCC <install-gcc>` • {ref}`Develop with GCC <use-gcc>` • {ref}`Available GCC versions <gcc-toolchain-availability>`
* **Clang**: {ref}`Install and set up Clang <install-clang>` • {ref}`Develop C and C++ with Clang <use-clang>` • {ref}`Available LLVM/Clang versions <llvm-toolchain-availability>`
* **.NET**: {ref}`Introduction to the .NET toolchain <dotnet-introduction>` • {ref}`Install and set up .NET <install-dotnet>` • {ref}`Develop with .NET <use-dotnet>` • {ref}`Debugging with .NET <debugging-with-dotnet>` • {ref}`Available .NET versions <dotnet-toolchain-availability>`
* **Java**: {ref}`Install and set up Java <install-java>` • {ref}`Develop with Java <use-java>` • {ref}`GraalVM native compilation <graalvm-introduction>` • {ref}`Compile Spring Boot apps to native executables <use-graalvm>` • {ref}`Fast start for Spring Boot apps with CRaC <use-crac>` • {ref}`Available Java versions <java-toolchain-availability>`
* **Zig**: {ref}`Install and set up Zig <install-zig>` • {ref}`Develop with Zig <use-zig>` • {ref}`Available Zig versions <zig-toolchain-availability>`


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
