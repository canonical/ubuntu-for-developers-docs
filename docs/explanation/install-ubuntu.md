# Installing Ubuntu Desktop for developers

Ubuntu Desktop is an open-source operating system designed for a range of tasks, including development. This article explains considerations for installing the system to serve as a platform for software development.


:::{note}
This article doesn't provide guidance on installing the system. For Ubuntu Desktop installation instructions, go to [Install Ubuntu Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop).
:::


## Enterprise deployment considerations

Users in enterprise or large organizations might benefit from installation automation and connection to centralized authentication and authorization mechanisms.


### Automating system installation with Autoinstall

Use Autoinstall to configure a custom installation of the system that is easy to replicate on multiple machines, including virtual machines. Refer to [Creating Autoinstall configuration](https://canonical-subiquity.readthedocs-hosted.com/en/latest/tutorial/creating-autoinstall-configuration.html) for instructions on how to configure and use the Autoinstall mechanism.


### Authentication with Active Directory

The **Create login details** screen of the Ubuntu Desktop installer allows to link the system to an existing Active Directory domain and use a domain account for logging in. Refer to [Join machine to AD during installation](https://documentation.ubuntu.com/adsys/en/stable/how-to/join-ad-installation/#join-at-installation-time) for detailed instructions.


## Post installation tasks

After completing the system installation, install tooling to turn the system into a developer workstation. Based on what toolchain you plan on using for development, your work habits, and the circumstances of the project you intend to work on, this can include a text editor, an integrated development environment (IDE), a version control system, and other utilities.


### Developer tooling

The Ubuntu Desktop default set of installed packages does not include basic developer tooling. For guidance on how to add specific developer tooling to an Ubuntu Desktop system, follow instructions in these how-to guides:

* How to install and configure IDE
* How to install and configure version control


### Toolchains

This documentation provides guidance on how to install and set up the following toolchains provided by Ubuntu:

* Python
* Java: [How to set up development environment for Java on Ubuntu](../howto/java-setup.md)
* Rust: [How to set up development environment for Rust on Ubuntu](../howto/rust-setup.md)
* GCC
* Golang: [How to set up development environment for Go on Ubuntu](../howto/go-setup.md)
* .NET: [How to set up development environment for .NET on Ubuntu](../howto/dotnet-setup.md)


## Additional resources

* [Getting started with Autoinstall on Ubuntu Desktop 24.04 LTS](https://blog.local-optimum.net/getting-started-with-autoinstall-on-ubuntu-desktop-24-04-lts-147a1defb2de)

