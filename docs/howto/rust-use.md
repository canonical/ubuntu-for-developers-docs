# How to develop using Rust on Ubuntu

This article provides guidance on basic use of the Rust toolchain for development on Ubuntu. It shows how to create a 'hello world' programme and explains how to compile Rust programmes using `rustc` and build projects using `cargo`.

<!--

This how-to article should contain a tiny explanation of the difference
between `cargo` and `rustc` plus links to

  - https://doc.rust-lang.org/rustc/index.html
  - https://doc.rust-lang.org/stable/cargo/guide/why-cargo-exists.html

An example of cargo use is already here, so we need to add

  - rustc vs cargo paragraph
  - short rustc example

-->


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

By default, the nightly Rust builds are not selected for use. Use the `+nightly` parameter to to build your project with the nightly Rust version:

```
cargo +nightly build
```

To run the project, use:

```
cargo +nightly run
```
