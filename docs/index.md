# Ubuntu for Developers

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

This documentation provides guidance for using the [Ubuntu Desktop](https://ubuntu.com/desktop) Linux distribution as a development platform. The guides focus on setting up and using the Ubuntu system as a workstation for developers, with an emphasis on the following toolchains:

:::{table} Toolchain overview
| Toolchain | How to install | Get started coding |
| --- | --- | --- |
| Python | {ref}`Install Python <install-python>` | {ref}`Develop with Python <use-python>` |
| Golang | {ref}`Install Golang <install-golang>` | {ref}`Develop with Golang <use-golang>` |
| Rust | {ref}`Install Rust <install-rust>` | {ref}`Develop with Rust <use-rust>` |
| GCC | {ref}`Install GCC <install-gcc>` | {ref}`Develop with GCC <use-gcc>` |
| .NET | {ref}`Install .NET <install-dotnet>` | {ref}`Develop with .NET <use-dotnet>` |
| Java | {ref}`Install Java <install-java>` | {ref}`Develop with Java <use-java>` |
:::

For each of the toolchains, there is a {ref}`tutorial <tutorials>` that shows a quick path to a 'Hello, world!' program and demonstrates the use of supporting tooling, including debuggers and linters, on Ubuntu Desktop.

The documentation doesn't teach coding skills -- it shows developers how to make the most of Ubuntu Desktop with their toolchain of choice. Even if you haven't used Ubuntu before, you can follow this guidance to set up a development environment that suits your purposes.


## In this documentation

::::{grid} 1 1 2 2

:::{grid-item-card} {ref}`tutorials`
:link: tutorials
:link-type: ref

**Get started** - hands-on introduction to developing on Ubuntu Desktop for new users, including a path to developing a 'Hello, world!' application with each of the toolchains.
:::

:::{grid-item-card} {ref}`howto`
:link: howto/index
:link-type: doc

**Step-by-step guides** covering basic system setup for the individual toolchains and installation of supporting tooling.
:::

::::

::::{grid} 1 1 2 2
:reverse:

:::{grid-item-card} {ref}`reference`
:link: reference/index
:link-type: doc

**Overview** of supported versions of all toolchains on different Ubuntu releases. An overview of available IDEs.
:::

:::{grid-item-card} {ref}`explanation`
:link: explanation/index
:link-type: doc

**Discussion and clarification** of key topics, including considerations for Ubuntu installation and version control.
:::

::::


## Project and community

The Ubuntu Desktop Linux distribution is part of the Ubuntu family of projects. It's an open-source project that warmly welcomes community contributions, suggestions, fixes, and constructive feedback.

[Read our code of conduct](https://ubuntu.com/community/ethos/code-of-conduct)
: As a community, we adhere to the Ubuntu code of conduct.

[Get support](https://askubuntu.com/questions/tagged/ubuntu)
: Ask Ubuntu is a question and answer site for Ubuntu users and developers.

Join our online chat
: - IRC: [#ubuntu](https://web.libera.chat/gamja/?channels=%23ubuntu)
  - Matrix: [Discuss Ubuntu](https://matrix.to/#/#discuss:ubuntu.com)

[Report bugs](https://github.com/canonical/ubuntu-for-developers-docs/issues/new)
: We want to know about the problems so we can fix them.

[Contribute docs on GitHub](https://github.com/canonical/ubuntu-for-developers-docs)
: The source is open, and we welcome contributions. See {ref}`contribute-docs`.

Thinking about using Ubuntu Desktop as your development platform? [Get it!](https://ubuntu.com/desktop/developers)
