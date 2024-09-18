# How to develop using Rust on Ubuntu

This article provides guidance on basic use of the Rust toolchain for development on Ubuntu. It shows how to create a 'Hello World' programme and explains how to compile Rust programmes using {command}`rustc` and build projects using {command}`cargo`.

[`rustc` is the actual compiler](https://doc.rust-lang.org/rustc/index.html), and {command}`cargo` is the build system and also the project management tool.

In most cases, there is no reason to use {command}`rustc` directly. Instead, use {command}`cargo` as the build system to call {command}`rustc` indirectly. Refer to Rust documentation for an explanation [Why Cargo Exists](https://doc.rust-lang.org/stable/cargo/guide/why-cargo-exists.html).

If you want to use {command}`rustc` without {command}`cargo`, refer to the example [Using `rustc` directly](#how-to-use-rustc-directly).

## Creating a Rust project using Cargo

1. Create a new Rust project using the {command}`new` Cargo sub-command:

    ```none
    cargo new hello_world
    ```

2. Change to the project directory:

    ```none
    cd hello_world
    ```

    Notice that Cargo has already set up a Git repository with a skeleton project inside (which includes the basic 'hello world' programme):

    ```none
    cat src/main.rs
    ```

    ```rust
    fn main() {
        println!("Hello, world!");
    }
    ```

3. Build and run the programme:

    ```none
    cargo run
    ```


## Building programmes with nightly Rust

A nightly toolchain can be useful if the new Rust language feature you want to try has yet to land in the stable channel, or if you want to know how the latest Rust compiler optimises your code.

By default, the nightly Rust builds are not selected for use. Use the `+nightly` parameter to build your project with the nightly Rust version:

```none
cargo +nightly build
```

To run the project, use:

```none
cargo +nightly run
```

(how-to-use-rustc-directly)=
## How to Use `rustc` Directly

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

You need to compile the Rust code first using:

```none
rustc answer.rs --emit obj --crate-type=lib -Copt-level=3 -o answer.o
```

Then compile and link the final program:

```none
gcc -O3 c_main.c answer.o -o main
```

When you execute this program, you should see:

```none
./main
The answer is 42
```
