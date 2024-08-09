# How to develop using Rust on Ubuntu

This article provides guidance on basic use of the Rust toolchain for development on Ubuntu. It shows how to create a 'hello world' programme and explains how to compile Rust programmes using `rustc` and build projects using `cargo`.

[`rustc` is the actual compiler](https://doc.rust-lang.org/rustc/index.html), and `cargo` is the build system and also the project management tool.

Usually you don't want to use `rustc` directly, but rather use `cargo` as the build system to use `rustc` indirectly.
You can find Rust upstream explaining why you should use `cargo` here: <https://doc.rust-lang.org/stable/cargo/guide/why-cargo-exists.html>.

If you still insist that you want to use `rustc` directly for some reason, we still provide an example of how to use `rustc` directly at the end of this article.

## Creating a Rust project using Cargo

1. Create a new Rust project using the `new` Cargo sub-command:

    ```
    cargo new hello_world
    ```

2. Change to the project directory:

    ```
    cd hello_world
    ```

    Notice that Cargo has already set up a Git repository with a skeleton project inside (which includes the basic 'hello world' programme):

    ```
    cat src/main.rs
    ```
    ```rust
    fn main() {
        println!("Hello, world!");
    }
    ```

3. Build and run the programme:

    ```
    cargo run
    ```


## Building programmes with nightly Rust

A nightly toolchain can be useful if the shiny new Rust language feature you want to try has yet to land in the stable channel or if you want to know how the latest Rust compiler will optimize your code.

By default, the nightly Rust builds are not selected for use. Use the `+nightly` parameter to to build your project with the nightly Rust version:

```
cargo +nightly build
```

To run the project, use:

```
cargo +nightly run
```

## How to Use `rustc` Directly

Consider the following Rust code in a file called `answer.rs`:

```rust
#![no_std]
#[no_mangle]
pub extern "C" fn the_answer() -> usize {
    42
}
```

Say, you have a C program that calls this Rust function in a file called `c_main.c`:

```c
#include <stdio.h>
#include <unistd.h>

extern size_t the_answer();

int main() {
  printf("The answer is %lu\n", the_answer());
  return 0;
}
```

You will need to compile the Rust code first using:

```bash
rustc answer.rs --emit obj --crate-type=lib -Copt-level=3 -o answer.o
```

... then compile and link the final program:

```bash
gcc -O3 c_main.c answer.o -o main
```

When you execute this program, you should see

```
The answer is 42
``` 
