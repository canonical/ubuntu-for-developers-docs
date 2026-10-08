---
myst:
  html_meta:
    description: 'Use the Rust Workshop SDKs to build and run a Rust application on Ubuntu.'
---

(rust-workshop-sdks)=
# Develop with Rust Workshop SDKs on Ubuntu

The Rust Workshop SDK automates the process of installing and configuring `rustup`.

As a minimum starting example, [install Workshop](https://ubuntu.com/workshop/docs/tutorial/part-1-get-started), then create the following `workshop.yaml` file:

```{code-block} yaml
:caption: `workshop.yaml`
name: rust-app
base: ubuntu@24.04
sdks:
  - name: rust
    channel: latest/stable

actions:
  build: cargo build "$@"
  doc: cargo doc "$@"
  lint: cargo clippy "$@"
  test: cargo test "$@"
```

That's it; you can now develop Rust applications from inside the safety of your container.

## Configuring your Rust version

Certain projects may need a specific toolchain configuration; Rust's mechanism for signaling this is to write the configuration into a file named `rust-toolchain.toml` or `rust-toolchain`.
[Documentation about that file can be found here.](https://rust-lang.github.io/rustup/overrides.html#the-toolchain-file)
The Rust Workshop SDK listens for this file; if found, it will override any configuration in `workshop.yaml` and automatically install the correct version of Rust.

If you would like to pick a toolchain version using Rustup, Rustup settings persist across workshop updates via the `rustup-and-toolchains` mount.

```{code-block} shell
$ workshop shell
$ rustup default nightly
$ exit
$ workshop shell
# Still have nightly rust
```

## Plugs (resources this SDK consumes)

### `rustup-and-toolchains`

- Interface: `mount`
- Workshop target: `/home/workshop/.rustup`
- Purpose: Persists installed Rust toolchains, components, and rustup
  configuration between workshop updates.

### `cargo-global-config`

- Interface: `mount`
- Workshop target: `/home/workshop/.cargo`
- Purpose: Persists Cargo global configuration and registry caches between
  workshop updates.

## Slots (resources this SDK provides)

This SDK doesn't define any slots.

## For More Information

[The source code for Rust SDK for Workshop is publicly available on GitHub.](https://github.com/canonical/rust-sdk)
