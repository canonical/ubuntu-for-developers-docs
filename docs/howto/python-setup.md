(install-python)=
# How to set up a development environment for Python on Ubuntu

Python is an ubiquitous, object-oriented scripting language with an extensive ecosystem. This guide outlines how to install the Python interpreter and developer tooling on Ubuntu.


## Installing Python runtime environment

In the Ubuntu package repository, the {pkg}`python3` package always depends on the currently default version of Python (from the 3.x series) in Ubuntu. It is a part of the default system installation, and it ensures that your Python environment is continuously updated as new versions are introduced. The package installs the {pkg}`python3-minimal` dependency, which only includes the Python interpreter.

:::{warning}
Do not remove the default system installation of Python (the {pkg}`python3` package), as that would break system tooling.
:::

To get a more useful runtime environment, use the special dependency package, {pkg}`python3-full`, which automatically installs the interpreter with the complete class library, support for Python virtual environments (`venv`), and the basic Python IDE (IDLE). Similarly to {pkg}`python3`, the {pkg}`python3-full` is a meta package that always depends on the currently default version of Python in Ubuntu.

```none
sudo apt install -y python3-full
```

When installed, the {file}`/usr/bin/python3` file is a symbolic link always pointing to the currently default version of the Python interpreter binary. For example:

```{terminal}
:user: dev
:host: ubuntu
:input: ls -l /usr/bin/python3

lrwxrwxrwx 1 root root 10 Sep 12  2024 /usr/bin/python3 -> python3.12
```

:::{note}
Python 3 is the default, and Python 2 is no longer officially supported on Ubuntu. As a convenience, consider installing the {pkg}`python-is-python3` package, which provides a symbolic link from {file}`/usr/bin/python` to {file}`/usr/bin/python3`.
:::


## Installing Python package manager

Numerous Ubuntu system tools make use of the system Python installation. To avoid interfering with this setup and isolate project dependencies, use virtual environments for development and testing.

While the system installation uses Python modules packaged as `.deb` packages that are available from system repositories, for installing dependencies within Python virtual environments, use the {command}`pip` Python package manager.

Install with:

```none
sudo apt install -y python3-pip python3-pip-whl
```


## Installing editing and debugging tools

While it is possible to write and edit Python code using any plain-text editor, various integrated development environments (IDEs) offer features to simplify the development process.


### Text editors and Language Server Protocol (LSP)

Advanced text editors can be extended using LSP plugins to enhance the user experience with Python.

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


### Integrated development environments

Some of the most common IDEs for Python are:

[IDLE (Integrated Development and Learning Environment)](https://docs.python.org/3/library/idle.html)
: The Python editor and shell is maintained by the Python project and bundled as a dependency of the {pkg}`python3-full` package. It is basic but can serve for learning purposes. It includes a simple debugger and a **Stack Viewer** for tracing errors or exceptions.

[{spellexception}`Spyder`](https://www.spyder-ide.org/)
: A community-developed IDE (written in Python) with a special focus on scientific applications.

  Install with:

  ```none
  sudo apt install -y spyder
  ```

[PyCharm](https://www.jetbrains.com/pycharm/)
: A Python IDE based on the JetBrains platform with open-source and proprietary versions.

  Install with:

  ```none
  sudo snap install pycharm-community --classic
  ```

[PyDev](https://www.pydev.org/)
: A Python plugin for the [Eclipse IDE](https://eclipseide.org/).

  Install with:

  ```none
  sudo snap install eclipse --classic
  ```

  From within Eclipse, install PyDev by going to {menuselection}`Help --> Install New Software...` and use `http://www.pydev.org/updates` for the {guilabel}`Work with:` field. See [Installing](https://www.pydev.org/manual_101_install.html) in the PyDev [Getting started guide](https://www.pydev.org/manual_101_root.html).

[Apache NetBeans](https://netbeans.apache.org/front/main/index.html)
: The [{spellexception}`netbeansPython` plugin](https://github.com/albilu/netbeansPython) adds support for Python to NetBeans (it is based on the [python-lsp-server](https://github.com/python-lsp/python-lsp-server).

  Install with:

  ```none
  sudo apt install default-jre
  sudo snap install netbeans --classic
  ```

  From within NetBeans, install {spellexception}`netbeansPython` by going to {menuselection}` Tools --> Plugins --> Available Plugins --> Install`.


### Linting and code-quality tools

To check and improve code style, formatting, and quality, use, for example, the following tools (while these tools often integrate with text editors and IDEs, they can also be used stand-alone):

[Black](https://github.com/psf/black)
: The self-styled 'uncompromising' code formatter automatically formats Python code to follow [PEP 8 guidelines](https://peps.python.org/pep-0008/) -- the official Python style guide.

  Install with:

  ```none
  sudo apt install black
  ```

[Flake8](https://flake8.pycqa.org/)
: Code checker. Flake8 is a wrapper for several other tools: `PyFlakes`, `pycodestyle`, and the `mccabe` script.

  Install with:

  ```none
  sudo apt install flake8
  ```


### Testing and debugging tools

Python has the built-in `pdb` debugger and `unittest` testing framework, but you can also install additional tools that provide more features and offer more user-friendly controls.

[pytest](https://pytest.org/)
: A flexible testing framework for writing "small, readable" tests.

  Install with:

  ```none
  sudo apt install python3-pytest
  ```

[tox](https://tox.wiki/)
: A tool for automating running tests within Python virtual environments using either the {file}`tox.toml` or {file}`tox.ini` configuration files.

  Install with:

  ```none
  sudo apt install tox
  ```


## What next

See the tutorial introducing the use of Python and related tooling: {ref}`use-python`.
