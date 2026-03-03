(install-clang)=
# How to set up a development environment for Clang on Ubuntu

Clang is a popular C and C++ compiler, and a part of the [LLVM project](https://llvm.org/). This article guides you in getting it installed on Ubuntu.

## Install the default version of Clang

To compile C and C++ code, you don't need to install all of the LLVM tooling, just Clang itself. Each Ubuntu release has a designated default version of Clang, which can be installed by running:

```bash
sudo apt install clang
```

This will give you access to the `clang` and `clang++` executables and the corresponding documentation.

### Alternative Clang versions

If the default version does not meet your needs, you can find which other versions have already been packaged for your Ubuntu release by doing a package search:

```bash
sudo apt search -n ^clang-[0-9]+
```

You will see a list of clang packages with explicit version numbers as part of their names, such as `clang-20`. You can install one of these the same way you would the default version, for example:

```bash
sudo apt install clang-20
```

However, in order to support parallel installations of multiple clang versions without conflicts, packages other than the default will not install a `clang` nor `clang++` executable. Instead, they will contain the explicit version number that you selected, such as `clang-20` or `clang++-20`. For the sake of stability, changing the default via something like `update-alternatives` is not recommended.

## C and C++ IDEs

There are also a number of IDEs available for C and C++ programming on Ubuntu, all of which can be configured to use Clang as the compiler:

[Visual Studio Code](https://code.visualstudio.com/) with [C/C++ Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
: `sudo snap install code --classic`

[CLion](https://www.jetbrains.com/clion/)
: `sudo snap install clion --classic`

[Qt Creator](https://www.qt.io/development/tools/qt-creator-ide)
: `sudo apt install qt-creator`

For developers who prefer a text editor to an IDE, you can set up `clangd` as an LSP server for your project. The full setup of that is out of scope here. Install it with:

```bash
sudo apt install clangd
```

## What next

See the tutorial introducing the use of C/C++ and related tooling: {ref}`use-clang`.
