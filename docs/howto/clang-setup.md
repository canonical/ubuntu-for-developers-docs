(install-clang)=
# How to set up a development environment for Clang on Ubuntu

Clang is a popular C and C++ compiler, and a part of the [LLVM project](https://llvm.org/). This article guides you in getting it installed on Ubuntu.

## Install the default version of Clang

To compile C and C++ code, you don't need to install all of the LLVM tooling, just Clang itself. Each Ubuntu release has a designated default version of Clang, which can be installed by running:

```none
sudo apt install clang
```

This installs the {command}`clang` and {command}`clang++` executables and the corresponding documentation.

### Alternative Clang versions

To find which other versions have been packaged for your Ubuntu release, do a package search:

```none
sudo apt search -n ^clang-[0-9]+
```

The output is a list of {pkg}`clang` packages with explicit version numbers as part of their names, such as {pkg}`clang-20`. You can install one of these the same way you would the default version, for example:

```none
sudo apt install clang-20
```

:::{note}
To support parallel installations of multiple Clang versions without conflicts, packages other than the default do not install a {command}`clang` nor {command}`clang++` executable. Instead, they contain the explicit version number that you selected, such as {command}`clang-20` or {command}`clang++-20`. For the sake of stability, changing the default via a mechanism like {command}`update-alternatives` is not recommended.
:::

## C and C++ IDEs

There are also a number of IDEs available for C and C++ programming on Ubuntu, all of which can be configured to use Clang as the compiler:

[Visual Studio Code](https://code.visualstudio.com/) with [C/C++ Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
: `sudo snap install code --classic`

[CLion](https://www.jetbrains.com/clion/)
: `sudo snap install clion --classic`

[Qt Creator](https://www.qt.io/development/tools/qt-creator-ide)
: `sudo apt install qt-creator`

For developers who prefer a text editor to an IDE, you can set up `clangd` as an LSP server for your project. Install it with:

```none
sudo apt install clangd
```

To configure the LSP, follow instructions in the official [`clangd` documentation](https://clangd.llvm.org/config).

## What next

See the tutorial introducing the use of C/C++ and related tooling: {ref}`use-clang`.
