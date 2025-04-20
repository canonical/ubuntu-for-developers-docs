# How to set up development environment for Python on Ubuntu

Python is an ubiquitous, object-oriented scripting language with an extensive ecosystem. This guide outlines how to install the Python interpreter and developer tooling on Ubuntu.


## Installing a Python runtime environment

In the Ubuntu package repository, the {pkg}`python3` package always depends on the currently default version of Python (from the 3.x series) in Ubuntu. Installing it ensures that your Python environment is continuously updated as new versions are introduced. The package installs the {pkg}`python3-minimal` dependency, which only includes the Python interpreter.

To get a more useful runtime environment, use the special dependency package, {pkg}`python3-full`, which automatically installs the interpreter with the complete class library, support for Python virtual environments (`venv`), and the basic Python IDE (IDLE). Similarly to {pkg}`python3`, the {pkg}`python3-full` is a metapackage that always depends on the currently default version of Python in Ubuntu.

```none
sudo apt install -y python3-full
```

When installed, the {file}`/usr/bin/python3` file is a symbolic link always pointing to the currently default version of the Python interpreter binary. For example:

```{prompt} text $ auto
$ ls -l /usr/bin/python3
lrwxrwxrwx 1 root root 10 Sep 12  2024 /usr/bin/python3 -> python3.12
```

:::{note}
Python 3 is the default, and Python 2 is no longer officially supported on Ubuntu. As a convenience, consider installing the {pkg}`python-is-python3` package, which provides a symbolic link from {file}`/usr/bin/python` to {file}`/usr/bin/python3`.
:::


## Installing a specific version of Python

To develop or test with a specific point version of Python, use either the [python3-alt](https://snapcraft.io/python3-alt) snap, or the [deadsnakes](https://launchpad.net/%7Edeadsnakes/+archive/ubuntu/ppa) PPA repository.


### Using snap

To install Python versions from Python 3.8 to 3.13 along with corresponding versions of the `pip` Python package installer:

```none
sudo snap install python3-alt
```

Upon installation, the following commands become available:

```{prompt} text $ auto
$ basename -a /snap/bin/python3-alt.*
python3-alt.3-13
python3-alt.3-12
python3-alt.3-11
python3-alt.3-10
python3-alt.3-9
python3-alt.3-8
python3-alt.pip3-13
python3-alt.pip3-12
python3-alt.pip3-11
python3-alt.pip3-10
python3-alt.pip3-9
python3-alt.pip3-8
```


### Using deadsnakes PPA

For an overview of all Python versions included in the PPA repository for different Ubuntu distributions, visit [deadsnakes](https://launchpad.net/%7Edeadsnakes/+archive/ubuntu/ppa). Note that builds are only provided for LTS versions of Ubuntu.

To enable the `deadsnakes` PPA:

```none
sudo add-apt-repository ppa:deadsnakes/ppa
```

:::{admonition} Enabling `deadsnakes` PPA on non-LTS Ubuntu
To enable the `deadsnakes` PPA on a non-LTS Ubuntu release, edit the {file}`/etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-<release>.sources` file, and modify the `Suites:` line to specify the LTS release closest to the one you're using. For example, when using Ubuntu 25.10 Oracular Oriole, edit the file to look like this:

```{prompt} text $ auto
$ cat /etc/apt/sources.list.d/deadsnakes-ubuntu-ppa-oracular.sources
Types: deb
URIs: https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/
Suites: noble
Components: main
[snip]
```

Visit [Ubuntu releases](https://www.releases.ubuntu.com/) for an overview of Ubuntu versions.
:::

To list all Python versions available for installation after enabling the PPA, use, for example, the {command}`apt-cache` tool {install it with {command}`sudo apt install -y apt-cache`). Running {command}`apt-cache` with the {command}`madison` sub-command yields an output similar to this:

```{prompt} text $ auto
$ apt-cache madison python3.{0..20}
 python3.7 | 3.7.17-1+noble2 | https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main amd64 Packages
 python3.8 | 3.8.20-1+noble1 | https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main amd64 Packages
 python3.9 | 3.9.22-1+noble1 | https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main amd64 Packages
python3.10 | 3.10.17-1+noble1 | https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main amd64 Packages
python3.11 | 3.11.12-1+noble1 | https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main amd64 Packages
python3.12 | 3.12.7-1ubuntu2 | http://archive.ubuntu.com/ubuntu oracular-updates/main amd64 Packages
python3.12 | 3.12.7-1ubuntu2 | http://security.ubuntu.com/ubuntu oracular-security/main amd64 Packages
python3.12 |   3.12.7-1 | http://archive.ubuntu.com/ubuntu oracular/main amd64 Packages
python3.13 | 3.13.3-1+noble1 | https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main amd64 Packages
python3.13 |   3.13.0-1 | http://archive.ubuntu.com/ubuntu oracular/universe amd64 Packages
python3.14 | 3.14.0~a7-1+noble1 | https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main amd64 Packages
N: Unable to locate package python3.0
N: Unable to locate package python3.2
N: Unable to locate package python3.3
N: Unable to locate package python3.4
[snip]
```

To install, for example, Python 3.9 (including the complete class library and support for Python virtual environments, `venv`), run:

```none
sudo apt-install -y python3.9-full
```

:::{warning}
The default system Python package symlinks {command}`python3` to the currently installed Python binary. For example:

```{prompt} text $ auto
$ ls -l $(which python3)
lrwxrwxrwx 1 root root 10 Sep 12  2024 /usr/bin/python3 -> python3.12
```

Do not change this symlink to any other Python version you install. System functions that rely on the default system version of Python could malfunction.
:::


## Setting up a Python development environment

Numerous Ubuntu system tools make use of the system Python installation. To avoid interfering with this setup and isolate project dependencies, use virtual environments for development and testing.

While the system installation uses Python modules packaged as `.deb` packages that are available from system repositories, for installing dependencies within Python virtual environments, use the {command}`pip` Python package manager.

Install with:

```none
sudo apt install -y python3-pip python3-pip-whl
```


## Editing and debugging

While it is possible to write and edit Python code using any plain-text editor, various integrated development environments (IDEs) offer features to simplify the development process.

Advanced text editors can also be extended using Language Server Protocol plugins to enhance the user experience.


### Integrated development environments and editors

Some of the most common IDEs for Python are:

[IDLE (Integrated Development and Learning Environment)](https://docs.python.org/3/library/idle.html)
: The Python editor and shell is maintained by the Python project and bundled as a dependency of the {pkg}`python3-full` package. It is basic but can serve for learning purposes. It includes a simple debugger and a **Stack Viewer** for tracing errors or exceptions.

[Spyder](https://www.spyder-ide.org/)
: A community-developed IDE (written in Python) with a special focus on scientific applications.

  Install with:

  ```none
  sudo apt install -y spyder
  ```

[Vim with Python LSP](https://www.vim.org/)
: A mode-driven text editor with powerful editing features. Combined with an LSP, such as [Python LSP Server](https://github.com/python-lsp/python-lsp-server), it offers code completion, linting, navigation, and others. It can also integrate with other tools, such as [Flake8](https://github.com/pycqa/flake8) for error checking.

  Install with:

  ```none
  sudo apt install -y vim python3-pylsp flake8
  ```

[Codium](https://vscodium.com/)
: The freely-licensed binary distribution of Microsoft’s Visual Studio Code. Numerous extensions available from the open-source [Open VSX](https://open-vsx.org/) registry provide support for coding with Python. For example, [Python](https://open-vsx.org/extension/ms-python/python) and [Python Debugger](https://open-vsx.org/extension/ms-python/debugpy).

  Install with:

  ```none
  sudo snap install codium --classic
  ```

[Visual Studio Code](https://code.visualstudio.com/)
: The popular editor from Microsoft with an extensive range of extensions for Python development, including [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy).

  Install with:

  ```none
  sudo snap install code --classic
  ```

[PyCharm](https://www.jetbrains.com/pycharm/)
: A Python IDE based on the JetBrains platform with open-source and proprietary versions.

  Install with:

  ```none
  sudo snap install pycharm-community --classic
  ```

  (Or use the {pkg}`pycharm-professional` snap.)

[PyDev](https://www.pydev.org/)
: A Python plugin for the [Eclipse IDE](https://eclipseide.org/).

  Install with:

  ```none
  sudo snap install eclipse --classic
  ```

  From within Eclipse, install PyDev by going to {menuselection}`Help --> Install New Software...` and use `http://www.pydev.org/updates` for the {guilabel}`Work with:` field. See [Installing](https://www.pydev.org/manual_101_install.html) in the PyDev [Getting started guide](https://www.pydev.org/manual_101_root.html).

