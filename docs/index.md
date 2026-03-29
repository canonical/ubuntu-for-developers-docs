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

The following sections group all major pages by topic, organizing the documentation along subject lines rather than by documentation type.


### Getting to 'Hello, world!'

Tutorials guide you through writing a first program and using supporting tooling with each toolchain on Ubuntu Desktop.

* **Python**: {ref}`Develop with Python <use-python>`
* **Go**: {ref}`Develop with Go <use-go>`
* **Rust**: {ref}`Develop with Rust <use-rust>`
* **GCC**: {ref}`Develop with GCC <use-gcc>`
* **Clang**: {ref}`Develop C and C++ with Clang <use-clang>`
* **.NET**: {ref}`Develop with .NET <use-dotnet>`
* **Java**: {ref}`Develop with Java <use-java>` • {ref}`Compile Spring Boot apps to native executables <use-graalvm>` • {ref}`Fast start for Spring Boot apps with CRaC <use-crac>`


### Installing and configuring toolchains

How-to guides cover installation and setup for each toolchain and its supporting tooling.

* **Python**: {ref}`Install and set up Python <install-python>`
* **Go**: {ref}`Install and set up Go <install-golang>`
* **Rust**: {ref}`Install and set up Rust <install-rust>`
* **GCC**: {ref}`Install and set up GCC <install-gcc>`
* **Clang**: {ref}`Install and set up Clang <install-clang>`
* **.NET**: {ref}`Install and set up .NET <install-dotnet>`
* **Java**: {ref}`Install and set up Java <install-java>`


### Toolchain availability

Toolchain versions are tied to Ubuntu releases — these pages show which versions ship with each release and what IDEs are available on Ubuntu.

* **Versions**: {ref}`Python <python-toolchain-availability>` • {ref}`Go <go-toolchain-availability>` • {ref}`Rust <rust-toolchain-availability>` • {ref}`GCC <gcc-toolchain-availability>` • {ref}`LLVM/Clang <llvm-toolchain-availability>` • {ref}`.NET <dotnet-toolchain-availability>` • {ref}`Java <java-toolchain-availability>`
* **IDEs**: {ref}`Integrated developer environments <ides>`


### Background and context

These pages explain the concepts and context behind the steps, from Ubuntu installation choices to how specific toolchains and technologies work.

* **Ubuntu**: {ref}`Installing Ubuntu Desktop for developers <install-ubuntu>`
* **Version control**: {ref}`Using Git version control on Ubuntu <use-git>`
* **Packaging**: {ref}`Packaging software <packaging>`
* **.NET**: {ref}`Introduction to the .NET toolchain <dotnet-introduction>` • {ref}`Debugging with .NET <debugging-with-dotnet>`
* **GraalVM**: {ref}`GraalVM native compilation <graalvm-introduction>`


## How this documentation is organized

This documentation follows the [Diátaxis documentation framework](https://diataxis.fr/).

* {ref}`Tutorials <tutorials>` guide you through developing a 'Hello, world!' application with each toolchain on Ubuntu Desktop, and demonstrate the use of debuggers, linters, and other supporting tools.
* {ref}`How-to guides <howto>` provide step-by-step instructions for installing and setting up each toolchain and its supporting tooling on Ubuntu Desktop.
* {ref}`Reference <reference>` covers toolchain version availability across Ubuntu releases and lists supported integrated development environments.
* {ref}`Explanation <explanation>` discusses Ubuntu installation considerations, version-control setup, packaging, and toolchain-specific background.


## Project and community

Ubuntu Desktop is part of the Ubuntu family of open-source projects, developed and maintained by Canonical and a worldwide community of contributors.


### Get involved

* [Ask Ubuntu](https://askubuntu.com/)
* Matrix: [Discuss Ubuntu](https://matrix.to/#/#discuss:ubuntu.com)
* [Report issues in this documentation](https://github.com/canonical/ubuntu-for-developers-docs/issues/new)
* {ref}`Contribute to this documentation <contribute-docs>`


### Governance and policies

* [Code of conduct](https://ubuntu.com/community/ethos/code-of-conduct)


### Commercial support

Thinking about using Ubuntu Desktop as your development platform? [Get it](https://ubuntu.com/desktop/developers).
