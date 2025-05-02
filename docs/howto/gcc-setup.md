(install-gcc)=
# How to set up a development environment for GCC on Ubuntu

GCC (GNU Compiler Collection) is a set of compilers that supports a number of programming languages, including C, C++, Assembler, and others. It is the {spellexception}`de facto` standard in Linux environments and is used to compile both the GNU toolchain and the Linux kernel.

This guide shows how to install GCC and related tooling, including a build system and debuggers, on Ubuntu Desktop.


## Installing GCC

The GCC toolchain, including past versions and cross-compilers for different architectures, is included in the Ubuntu package repository. The {pkg}`gcc` package always depends on the currently default version of GCC for your platform.

1. Install GCC compilers for C and C++:

    ```none
    sudo apt install gcc g++
    ```

2. Confirm the version of the installed compiler:

    ```{terminal}
    :user: dev
    :host: ubuntu
    :input: gcc --version

    gcc (Ubuntu 14.2.0-4ubuntu2) 14.2.0
    Copyright (C) 2024 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    ```


## Installing editing and debugging tools

A number of Integrated Developer Environments (IDEs) that are available from Ubuntu DEB and snap repositories provide support for developing C/C++ applications. Many developers also opt for using advanced text editors with language-specific extensions based on Language Server Protocol (LSP), such Vim or Visual Studio Code (or its


### Text editors and Language Server Protocol (LSP)

Advanced text editors can be extended using LSP plugins to enhance the user experience with C/C++.

[Vim with Python LSP](https://www.vim.org/)
: A mode-driven text editor with powerful editing features. Combined with an LSP, such as [ccls](https://github.com/MaskRay/ccls), it offers code completion, linting, navigation, and others.

  Install with:

  ```none
  sudo apt install -y vim ccls
  ```

[Codium](https://vscodium.com/)
: The freely-licensed binary distribution of Microsoft’s Visual Studio Code. It includes extensive C/C++ support out of the box, and numerous extensions available from the open-source [Open VSX](https://open-vsx.org/) registry provide support for additional functionality for coding with C. For example, the all-in-one [C/C++ Extension Pack](https://open-vsx.org/extension/franneck94/vscode-c-cpp-dev-extension-pack).

  Install with:

  ```none
  sudo snap install codium --classic
  ```

[Visual Studio Code](https://code.visualstudio.com/)
: The popular editor from Microsoft with an extensive range of extensions for C/C++ development, including the [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) extension also from Microsoft.

  Install with:

  ```none
  sudo snap install code --classic
  ```


### Integrated development environments

Some of the most common IDEs for Python are:

[Code::Blocks)](https://www.codeblocks.org/)
: A dedicated C, C+, and Fortran IDE. For its ease of use, it's often featured in C/C++ programming tutorials.

  Install with:

  ```none
  sudo apt install -y codeblocks
  ```

[Eclipse CDT™ C/C++ Development Tools](https://github.com/eclipse-cdt/cdt)
: An C/C++ IDE based on the Eclipse IDE platform.

  Install with:

  ```none
  sudo snap install eclipse --classic
  ```

  From within Eclipse, install CDT by going to {menuselection}`Help --> Install New Software...` and use `https://download.eclipse.org/tools/cdt/releases/latest/` for the {guilabel}`Work with:` field.

  Install with:

[Apache NetBeans](https://netbeans.apache.org/front/main/index.html)
: The [NetBeans C/C++ Development Pack](https://netbeans.info/products/cplusplus.html) adds support for C/C++ to NetBeans.

  Install with:

  ```none
  sudo apt install default-jre
  sudo snap install netbeans --classic
  ```

  From within NetBeans, install the C/C++ Pack by going to {menuselection}` Tools --> Plugins --> Available Plugins --> Install`.


### Debuggers, profilers, and other tooling

The standard debugger developed for GCC is GDB. Other tools, such as gprof (part of {pkg}`binutils`) and Valgrind provide support for profiling and advanced dynamic analysis.

Install with:

```none
sudo apt install -y gdb valgrind
```

(The {pkg}`binutils` package is installed automatically with {pkg}`gcc`.)


### Build systems

The standard for GNU software is GNU Make. For larger projects and a more modern experience, consider CMake.

Install with:

```none
sudo apt install -y make cmake
```


## What next

See the tutorial introducing the use of GCC and related tooling: {ref}`use-gcc`.
