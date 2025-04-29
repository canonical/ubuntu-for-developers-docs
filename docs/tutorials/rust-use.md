(use-rust)=
# Develop with Rust on Ubuntu

This tutorial provides guidance on basic use of the Rust toolchain for development on Ubuntu. It shows how to create a 'Hello, world!' program and explains how to compile Rust programs using {command}`rustc` and build projects using {command}`cargo`.

For instructions on how to install Rust and related tooling, including IDEs and debuggers, see the dedicated guide on {ref}`install-rust`. This article assumes that tooling suggested in that article has been installed.


## `cargo` vs `rustc`

[`rustc`](https://doc.rust-lang.org/stable/rustc/index.html) is the actual compiler, and [`cargo`](https://doc.rust-lang.org/stable/cargo/index.html) is the build system and project management tool.

In most cases, there is no reason to use {command}`rustc` directly. Instead, use {command}`cargo` as the build system to call {command}`rustc` indirectly. Refer to the Rust documentation for an explanation: [Why Cargo Exists](https://doc.rust-lang.org/stable/cargo/guide/why-cargo-exists.html)

If you want to use {command}`rustc` without {command}`cargo`, refer to the example {ref}`using-rustc-directly`.


## Creating a Rust project using Cargo

1. Create a new Rust project using the {command}`new` Cargo sub-command:

    ```none
    cargo new hello_world
    ```

2. Change to the project directory:

    ```none
    cd hello_world
    ```

    Notice that Cargo has already set up a Git repository with a skeleton project inside (which includes the basic 'hello world' program):

    ```none
    cat src/main.rs
    ```

    ```rust
    fn main() {
        println!("Hello, world!");
    }
    ```

3. Build and run the program:

    ```{terminal}
    :input: cargo run
    :user: dev
    :host: ubuntu

    Hello, world!
    ```

:::{attention}
When building and running the program, if you get an error message related to a missing linker, then you are missing some essential build tools. Install them with:

```none
sudo apt install build-essential
```
:::


## Building programs with nightly Rust

A nightly toolchain can be useful if the new Rust language feature you want to try has yet to land in the stable channel, or if you want to know how the latest Rust compiler optimizes your code.

By default, the nightly Rust builds are not selected for use. Use the `+nightly` parameter to build your project with the nightly Rust version:

```none
cargo +nightly build
```

To run the project, use:

```none
cargo +nightly run
```


(using-rustc-directly)=
## Using `rustc` directly

Consider the following Rust code in a file called {file}`answer.rs`:

```rust
#![no_std]
#[no_mangle]
pub extern "C" fn the_answer() -> usize {
    42
}
```

Then you have a C program that calls this Rust function in a file called {file}`c_main.c`:

```c
#include <stdio.h>
#include <unistd.h>

extern size_t the_answer();

int main() {
  printf("The answer is %lu\n", the_answer());
  return 0;
}
```

Compile the Rust code first:

```none
rustc answer.rs --emit obj --crate-type=lib -Copt-level=3 -o answer.o
```

Compile and link the final program:

```none
gcc -O3 c_main.c answer.o -o main
```

When you execute this program, you should see the following:

```{terminal}
:input: ./main
:user: dev
:host: ubuntu

The answer is 42
```
