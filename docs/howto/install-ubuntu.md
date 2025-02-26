# How to install Ubuntu Desktop for developers

Ubuntu desktop is an open-source operating system designed for a range of tasks including development. In this guide, you will install Ubuntu Desktop as a platform for your software development environment.

:::
### Prerequisites
:::

Before you can install Ubuntu Desktop, you need to make sure you have:

- A laptop or PC with at least 256GB of storage. It is recommended that you install Ubuntu on a device listed on the [Ubuntu-certified hardware](https://ubuntu.com/certified?q=&limit=20&category=Desktop&category=Laptop) page.
- A USB stick with at least 12 GB of free space.

## Preparing for installation

You can install Ubuntu desktop as:

- The only operating system (OS) on your device (single boot), which is ideal if you run resource-intensive tasks requiring full hardware utilization.
- Along with another OS (dual boot), which is ideal if you need Ubuntu OS for only specific development tasks.
- Run it inside another OS using virtualization software. This is ideal for testing Ubuntu without affecting your main system. This guide explains how to [install Ubuntu as a VM using VirtualBox](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview).

Whichever mode you choose to install Ubuntu desktop in, you can run it in GUI (with a user interface) or headless mode (without a user interface). For a developer environment, you will install Ubuntu desktop with a GUI, as headless mode is more suitable for cloud servers.

## Automated installation

You can install Ubuntu automatically using an `autoinstall.yaml` file. This allows you to skip most of the installation steps and restore an existing Ubuntu environment setup automatically. This guide explains how you can [provide an autoinstall configuration during installation](https://canonical-subiquity.readthedocs-hosted.com/en/latest/tutorial/providing-autoinstall.html).

## Extended app selection

During your Ubuntu installation process, you can choose to add more apps to Ubuntu’s default selection using the Extended selection which contains but is not limited to:

- Compilers and language-specific tools like Node.js and Ruby.
- Containers & Virtualization tools like Docker, VirtualBox, and Vagrant.
- Database management tools like MySQL workbench and PgAdmin.

:::{note}
The list above is not comprehensive and you can always add more apps to Ubuntu using the app centre.
:::

## Single boot configuration

A single boot configuration is straightforward and eliminates the need to manage multiple operating systems in your device, thus, making updates and maintenance easier. This guide explains how you can [install Ubuntu as the only OS on your device](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

:::{note}
Before proceeding with this installation, ensure that all your data is backed up and can be restored as this process will erase everything on your hard drive.
:::

## Dual boot configuration

In a dual-boot configuration, you install Ubuntu and another operating system on your device. To proceed with the dual boot option, you need to have enough free disk space to allocate separate partitions for both operating systems and additional room for updates and personal files.

The Ubuntu installer automatically selects the largest partition on the drive to install, however, you can switch to manual partitioning for a more fine-grained control of the partitions. This guide explains how you can [install Ubuntu desktop as a secondary OS](https://ubuntu.com/tutorials/install-ubuntu-desktop#installing-ubuntu-alongside-another-operating-system) on your device.

## Authentication with Active Directories

On the “Create login details” screen during a manual installation, you will be allowed to link your system to an existing Active Directory domain. This will allow you to log in with your domain account after installation. This guide explains how to [join an Active Directory during installation](https://documentation.ubuntu.com/adsys/en/stable/how-to/join-ad-installation/#join-at-installation-time).

## Post installation recommendations

Welcome to Ubuntu!! Be sure to keep your system up to date to receive the latest updates and security patches. You can automate this process by enabling automatic updates.

Now that you have installed Ubuntu desktop, you can take your developer environment to the next level by installing and configuring a version control system like Git.
