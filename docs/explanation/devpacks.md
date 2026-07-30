---
myst:
  html_meta:
    description: "What devpacks are, how they work, and what they automate on Ubuntu."
---

(devpacks)=
# Devpacks

Devpacks are snap-packaged command-line tools that automate development environment setup, project scaffolding, and library management for specific toolchains on Ubuntu. They aim to lower the barrier of entry for developers building software according to best practices.


## What devpacks do

A devpack provides a curated set of tools, libraries, and resources for a specific development context. Typically, a devpack automates:

- **Environment setup**: installing the language runtime, build tools, IDEs, and supporting utilities through a single command
- **Project scaffolding**: creating new projects with sensible defaults and pre-configured build files
- **Library management**: providing prebuilt libraries as locally stored packages, reducing build times and enabling offline development
- **Build plugins**: running formatters and linters, as well as packaging tools with pre-configured settings


## How devpacks are distributed

Each devpack is distributed as a [snap](https://snapcraft.io/) package with classic confinement, which allows it to access system resources required for development tooling. Installing a devpack installs the devpack command-line tool itself, which then orchestrates the installation of additional apt and snap packages.

A devpack is not a development container. A devcontainer is a customized container with all necessary software pre-installed, while a devpack is a collection of opinionated tools and resources. Devpacks also support creating devcontainers, but the two concepts are distinct.


## When to use a devpack

Use a devpack to quickly set up a development environment on a fresh Ubuntu installation, or to ensure consistent tooling across multiple machines. Devpacks are particularly useful when:

- Setting up a new development workstation
- Onboarding new team members with a consistent environment
- Automating repetitive setup tasks across projects

For manual control over which packages are installed, use the individual toolchain setup guides in the {ref}`howto` section instead.


## What next

- {ref}`devpack-for-spring` tutorial
