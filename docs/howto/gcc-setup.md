(install-gcc)=
# How to set up a development environment for GCC on Ubuntu

The [GNU Compiler Collection (GCC)](https://gcc.gnu.org/) is a set of compilers for programming languages, including C, C++, Assembly, and many more. It is the {spellexception}`de facto` standard in Linux environments and is used to compile both the GNU toolchain and the Linux kernel.

This guide shows how to install GCC and related tooling, including a build system and debuggers, on Ubuntu Desktop.


## Installing GCC

The GCC toolchain, including past versions and cross-compilers for different architectures, is included in the Ubuntu package repository. The {pkg}`gcc` package provides the default version of GCC for your platform. `gcc` runs the C compiler and `g++` runs the C++ compiler.

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

:::{note}
You may see a different version number from the one listed here.  That is not a problem.
:::

## Installing editing and debugging tools

### Text editors and Language Server Protocol (LSP) servers

Some developers prefer advanced text editors such as Vim, Codium, or Visual Studio Code with [Language Server Protocol (LSP)](https://langserver.org/) plug-ins for a lightweight and streamlined development experience.

[Vim with LSP](https://www.vim.org/)
: A mode-driven text editor with powerful editing features. Combined with an LSP, such as [ccls](https://github.com/MaskRay/ccls), it offers code completion, linting, navigation, and more.

  Install with:

  ```none
  sudo apt install -y vim ccls
  ```
  Refer to the [ccls editor configuration instructions](https://github.com/MaskRay/ccls/wiki/Editor-Configuration) for Vim LSP setup.

[Codium](https://vscodium.com/)
: The freely-licensed binary distribution of Microsoft’s Visual Studio Code. It includes extensive C/C++ support out of the box, and numerous extensions available from the open-source [Open VSX](https://open-vsx.org/) registry provide support for additional functionality for coding with C. For example, the all-in-one [C/C++ Extension Pack](https://open-vsx.org/extension/franneck94/vscode-c-cpp-dev-extension-pack).

  Install with:

  ```none
  sudo snap install codium --classic
  ```

[Visual Studio Code](https://code.visualstudio.com/)
: The popular editor from Microsoft with an extensive range of extensions for C/C++ development, including the [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) also from Microsoft.

  Install with:

  ```none
  sudo snap install code --classic
  ```


### Integrated development environments

Other developers enjoy the full support offered by Integrated Development Environments (IDEs). Several IDEs available in the Ubuntu `.deb` and `snap` repositories are excellent choices for developing C and C++ applications:

[Code::Blocks](https://www.codeblocks.org/)
: A dedicated and easy-to-use C, C+, and Fortran IDE that is often featured in C/C++ programming tutorials.

  Install with:

  ```none
  sudo apt install -y codeblocks
  ```

[Eclipse CDT™ C/C++ Development Tools](https://github.com/eclipse-cdt/cdt)
: A C/C++ IDE based on the [Eclipse IDE](https://eclipseide.org/) platform.

  Install with:

  ```none
  sudo snap install eclipse --classic
  ```

  From within Eclipse, install CDT by going to {menuselection}`Help --> Install New Software...` and use `https://download.eclipse.org/tools/cdt/releases/latest/` for the {guilabel}`Work with:` field.


[Apache NetBeans](https://netbeans.apache.org/front/main/index.html)
: The [NetBeans C/C++ Development Pack](https://www.netbeans.info/products/cplusplus.html) adds support for C/C++ to NetBeans.
  Install with:

  ```none
  sudo apt install default-jre
  sudo snap install netbeans --classic
  ```

  From within NetBeans, install the C/C++ Pack by going to {menuselection}` Tools --> Plugins --> Available Plugins --> Install`.


### Debuggers, profilers, and other tooling

The standard debugger developed for GCC is the [GNU Debugger (GDB)](https://sourceware.org/gdb/). Other tools, such as [`gprof`](https://sourceware.org/binutils/docs/gprof/) (part of {pkg}`binutils`) and [Valgrind](https://valgrind.org/) provide support for profiling and advanced dynamic analysis.

Install with:

```none
sudo apt install -y gdb valgrind
```

(The {pkg}`binutils` package is installed automatically with {pkg}`gcc`.)

See the [GDB manual](https://sourceware.org/gdb/current/onlinedocs/gdb.html/) and [Valgrind documentation](https://valgrind.org/docs/manual/quick-start.html) for more information about how to troubleshoot your programs.

### Build systems

The standard for GNU software is [GNU Make](https://www.gnu.org/software/make/). For larger projects and a more modern experience, consider [CMake](https://cmake.org/).

Install with:

```none
sudo apt install -y make cmake
```

See the [GNU Make manual](https://www.gnu.org/software/make/manual/make.html) and the [CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html) for more information about these build systems.

## What next

See the tutorial introducing the use of GCC and related tooling: {ref}`use-gcc`.
