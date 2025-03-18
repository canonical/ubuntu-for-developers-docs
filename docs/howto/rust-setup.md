# How to set up a development environment for Rust on Ubuntu

Rust is a relatively new and secure programming language supported on many platforms. This article provides guidance on how to install the Rust toolchain and set up a development environment for Rust on Ubuntu.


## Installing Rust

There are two (main) options for installing Rust on Ubuntu:

* Using Ubuntu packages from the Ubuntu archive: Official packages maintained by the Ubuntu team and installed through the Ubuntu package-management system. Use this method if you are an **Ubuntu package developer or maintainer** familiar with the archive toolchain model.

* Using Rustup, the Rust toolchain installer: Available as a snap package. Use this method if you **develop Rust applications for business or general use**. The Rustup snap allows for installing the latest releases of Rust ecosystem tools, as well as installing multiple versions of Rust in parallel.


### Installing the Rust toolchain from Ubuntu packages

Install the {pkg}`cargo` package, which automatically pulls required dependencies, including the `rustc` compiler.

1. In a terminal, run:

    ```none
    sudo apt-get install cargo
    ```


### Installing the latest Rust toolchain using Rustup

Install the Rustup manager from the Snap Store [snapcraft.io: Rustup](https://snapcraft.io/rustup) and the Rust toolchain using {command}`rustup`.

1. In a terminal, run:

    ```none
    snap install --classic rustup
    ```

2. After installing Rustup, use it to install the latest stable Rust version:

    ```none
    rustup install stable
    ```

3. Optional: If your project needs unstable Rust features that are not present in the latest stable toolchain, try the nightly Rust toolchain builds:

    ```none
    rustup install nightly
    ```

:::{note}
Many external Rust libraries on [crates.io](https://crates.io) contain C/C++ code, which requires a working C/C++ compiler to be installed on your system.

Use the following command to install them:

```none
sudo apt-get install build-essential
```
:::


## IDE integrations

Many editors and IDEs (Integrated Development Environment) come with various degrees of Rust support. Here are some popular ones:

- [Visual Studio Code](https://snapcraft.io/code): Install the [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) extension from the VSCode Marketplace.

- [Helix Editor](https://helix-editor.com/) and [Zed Editor](https://zed.dev/): Install rust-analyzer using Rustup:

    ```none
    rustup component add rust-analyzer
    ```

- [JetBrains RustRover](https://snapcraft.io/rustrover) (paid): Comes with full Rust support by default.


## Building for other platforms

To develop Rust applications for other platforms on Ubuntu, install the necessary tools and libraries for each platform.

To see a list of platforms that you can build on Ubuntu, use the following command:

```none
rustup target list
```

:::{attention}
Some targets on that list require installing additional packages or downloading SDKs from third-party websites. Refer to the official [Rust documentation](https://doc.rust-lang.org/rustc/platform-support.html) for details.
:::


### Example: Setup for building for Windows

1. To target Windows, install the following packages:

    ```none
    sudo apt-get install binutils-mingw-w64 g++-mingw-w64 gcc-mingw-w64
    ```

2. Add the Windows target to the toolchain:

    ```none
    rustup target add x86_64-pc-windows-gnu
    ```

3. Build your project:

    ```none
    cargo build --target x86_64-pc-windows-gnu
    ```


### Example: Setup for building for web browsers

Many Rust applications can run inside a web browser. To build a Rust project for web browsers, use the WebAssembly (`wasm`) target.

1. Install the required packages:

    ```none
    sudo apt-get install clang lld
    ```

2. Add the `wasm` target to the toolchain:

    ```none
    rustup target add wasm32-unknown-unknown
    ```

3. Build your project:

    ```none
    cargo build --target wasm32-unknown-unknown
    ```


## Installing debugging tooling

Your code editor or IDE probably already has debugging functionalities tailored for Rust applications. If not, you can also debug Rust applications on Ubuntu using familiar debugging tools such as GDB and LLDB.

To install the corresponding debugging support packages, run:

```none
sudo apt-get install gdb lldb rust-gdb rust-lldb
```

You can then use {command}`gdb` or {command}`lldb` to debug your Rust applications.
