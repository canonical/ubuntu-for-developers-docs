---
myst:
  html_meta:
    description: 'Use the Rust Workshop SDK to build, test, and run Rust applications on Ubuntu.'
---

(rust-workshop-sdk)=
# Develop with the Rust Workshop SDK on Ubuntu

This tutorial provides guidance on using the Rust Workshop SDK for development environments on Ubuntu with the [Workshop](https://ubuntu.com/workshop) tool. It explains how the SDK manages Rust toolchains for your project and shows how to create a "Hello, world!" program, then goes in-depth with an example that builds a web service and exposes it to your host machine.

For instructions on how to install Workshop and related tooling, see the dedicated guide on how to [Get started with workshops](https://ubuntu.com/workshop/docs/). There is no need to install Rust or related tooling directly, as they are installed through the SDK.


## The Rust Workshop SDK

The Rust ecosystem has a single, canonical Workshop SDK: the {pkg}`rust` SDK, which automates the installation and configuration of [rustup](https://rust-lang.github.io/rustup/), Rust's official toolchain installer.

Where other ecosystems provide separate SDKs for each build tool, the Rust SDK bundles the whole standard toolchain, so one SDK is all a Rust project needs:

| Tool             | Description                                       |
| :--------------- | :------------------------------------------------- |
| `cargo`          | Build system and package manager                   |
| `rustc`          | The Rust compiler                                  |
| `clippy`         | Linter that catches common mistakes                |
| `rustfmt`        | Code formatter                                     |
| `rust-analyzer`  | Language server for IDE support                    |

The SDK itself does not pin a compiler version. Instead, it defers to rustup, which selects a toolchain using the following precedence:

1. A {file}`rust-toolchain.toml` or {file}`rust-toolchain` file in your project directory, if present. See [the rustup documentation](https://rust-lang.github.io/rustup/overrides.html#the-toolchain-file) for details.
1. Your personal `rustup default` selection.
1. The `stable` toolchain.

Dependency caches are stored on the host and survive workshop refreshes, while installed toolchains live inside the workshop container. See the {ref}`SDK reference <rust-sdk-reference>` section at the end of this tutorial for the details.


## Getting started with the Rust Workshop SDK

Before using the SDK, install Workshop and its prerequisite, LXD. For more details, see the [Workshop getting-started tutorial](https://ubuntu.com/workshop/docs/tutorial/part-1-get-started/).

```{terminal}
:copy:
:user: dev
:host: ubuntu

sudo snap install --channel=6/stable lxd
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

sudo snap install --classic workshop
```

Before initializing a workshop, search the SDK Store to confirm that the SDK exists and get information about the publisher and the available versions.

* Confirm/search for available SDKs:

    ```{terminal}
    :copy:
    :user: dev
    :host: ubuntu

    sdk find rust

    NAME  VERSION  PUBLISHER    SUMMARY
    rust  1.99.1   Canonical**  The Rust toolchain installer
    ```

* Inspect SDK release information:

    ```{terminal}
    :copy:
    :user: dev
    :host: ubuntu

    sdk info rust

    name:       rust
    publisher:  Canonical✓
    license:    Apache-2.0 OR MIT
    website:    https://github.com/canonical/rust-sdk

    This SDK provides rustup and the Rust toolchain for Rust development.
    Toolchains and Cargo configuration are persisted on the host across
    workshop updates. Automatically detects project toolchain requirements
    via rust-toolchain.toml.

    CHANNELS
      CHANNEL           VERSION  BUILD       BASE          REV    SIZE
      latest/stable     1.99.1   2026-10-16  ubuntu@26.04   50  4.75MB
                                             ubuntu@24.04   49  4.75MB
                                             ubuntu@22.04   51  4.78MB
      latest/candidate  ↑
      latest/beta       ↑
      latest/edge       ↑
    ```

The `rust` SDK is published by Canonical and tracks a single channel, `latest/stable`, with builds for the Ubuntu 22.04, 24.04, and 26.04 bases. The `CHANNELS` table in the `sdk info rust` output lists the supported bases for your machine.

:::{note}
The output you see depends on the version of the SDK available at the time you run these commands. When a newer release is published, the version number, build date, and revision shown above differ. The `CHANNELS` table may also list a different set of Ubuntu bases, since it reflects the builds available for your machine.
:::


## Creating a Rust workshop

Let's create a "Hello, world!" program and build it with tools from the {pkg}`rust` workshop SDK.

1. Create a project directory for your work. Everything you handle with your workshop goes here: your Rust code, the workshop definition, and so on.

    ```{terminal}
    :copy:
    :user: dev
    :host: ubuntu

    mkdir hello-workshop
    ```

    ```{terminal}
    :copy:
    :user: dev
    :host: ubuntu

    cd hello-workshop
    ```

1. Initialize the applications workshop definition with the {pkg}`rust` SDK:

    ```{terminal}
    :copy:
    :dir: ~/hello-workshop
    :user: dev
    :host: ubuntu

    workshop init rust-example --sdks rust/latest/stable
    ```

    This command writes the definition to the {file}`.workshop/rust-example.yaml` file with the {pkg}`rust` SDK pinned to the `latest/stable` channel:

    ```{code-block} yaml
    :caption: `.workshop/rust-example.yaml`

    name: rust-example
    base: ubuntu@24.04
    sdks:
      - name: rust
        channel: latest/stable
    ```

    :::{note}
    When the project directory contains a single workshop definition, you can omit the workshop name from every {command}`workshop` command that accepts one: {command}`workshop launch` is equivalent to {command}`workshop launch rust-example`. The examples in this tutorial use this shorter form from here on. If your project defines multiple workshops, name them explicitly in the commands to disambiguate.
    :::

1. To get the workshop ready for use, launch it and confirm the runtime information matches the definition file:

   1. Prepare workshop after initialization:

      ```{terminal}
      :copy:
      :dir: ~/hello-workshop
      :user: dev
      :host: ubuntu

      workshop launch

      "rust-example" launched
      ```

      This prepares the workshop by automatically pulling and installing the defined SDKs, after which it starts the workshop container.

   1. View information about the workshop:

      ```{terminal}
      :copy:
      :dir: ~/hello-workshop
      :user: dev
      :host: ubuntu

      workshop info

      name:      rust-example
      base:      ubuntu@24.04
      project:   ~/hello-workshop
      hostname:  rust-example.hello-workshop.wp
      status:    ready
      runtime:   lxd-container
      notes:     –
      sdks:
        system:
          installed:  (2)
        rust:
          tracking:   latest/stable
          installed:  1.99.1  2026-10-16  (49)
          mounts:
            cargo-registry:
              host-source:      …/e5faec78/rust-example/mount/rust/cargo-registry
              workshop-target:  /home/workshop/.cargo/registry
      ```

       The `rust` SDK installs rustup and the default `stable` toolchain inside the workshop, alongside a mount that caches downloaded dependencies on the host between workshop updates. For more information, refer to [`workshop info`](https://ubuntu.com/workshop/docs/reference/cli/workshop/#ref-workshop-info).

    :::{note}
    To stop the workshop environment from running, use {command}`workshop stop`. To then make the workshop ready for use again, start it with the {command}`workshop start` command.
    :::

1. Initialize a Cargo package at the root of the project directory, from within the workshop:

    ```{terminal}
    :copy:
    :dir: ~/hello-workshop
    :user: dev
    :host: ubuntu

    workshop exec -- cargo init --name hello-workshop
    ```

    The project directory is mounted as {file}`/project` inside the workshop, so files created on either side (the host or the workshop) appear in both.

    Cargo generates a package with a {file}`Cargo.toml` manifest and a {file}`src/main.rs` file that already contains a "Hello, world!" program:

    ```{code-block} rust
    :caption: `src/main.rs`

    fn main() {
        println!("Hello, world!");
    }
    ```

1. Build and run the program from within the workshop:

    ```{terminal}
    :copy:
    :dir: ~/hello-workshop
    :user: dev
    :host: ubuntu

    workshop exec -- cargo run

    Compiling hello-workshop v0.1.0 (/project)
     Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.48s
      Running `target/debug/hello-workshop`
    Hello, world!
    ```

    You should see "Hello, world!" printed in your terminal — and the best part is where it came from. Everything happened inside the workshop container: the toolchain installed by the SDK did the scaffolding, compiling, and running, and your host machine does not need Rust at all.


## Managing your Rust toolchain

Rust projects often need to control exactly which Rust version they build with: a project may require an older toolchain for compatibility, or you may want nightly features for development. The {pkg}`rust` SDK manages this through rustup, giving you two complementary mechanisms.


:::
### Pinning a toolchain for the project
:::

Rust's mechanism for signaling a project's toolchain requirement is to write the configuration into a {file}`rust-toolchain.toml` file in the project directory, called [the toolchain file](https://rust-lang.github.io/rustup/overrides.html#the-toolchain-file).

For example, to pin your project to Rust 1.85.0, create a {file}`rust-toolchain.toml` file with the following content:

```{code-block} toml
:caption: `rust-toolchain.toml`

[toolchain]
channel = "1.85.0"
```

The Rust Workshop SDK listens for this file. Rust commands run in the project directory automatically pick up the pinned toolchain: rustup selects the pinned version and installs it on first use.

Confirm that the workshop uses the pinned toolchain:

```{terminal}
:copy:
:dir: ~/hello-workshop
:user: dev
:host: ubuntu

workshop exec -- rustc --version

rustc 1.85.0 (4d91de4e4 2025-02-17)
```

:::{note}
The toolchain file takes precedence over your personal rustup settings. Even if you have selected a different default toolchain, commands run in the project directory use the version pinned in {file}`rust-toolchain.toml`. Commit the file to your repository, so that every contributor builds the project with the same Rust version.
:::

To stop using the pinned version, remove the file to fall back to the default toolchain.

:::
### Selecting a toolchain with rustup
:::

To pick a toolchain version without a project file, use rustup from within the workshop:

```{terminal}
:copy:
:dir: ~/hello-workshop
:user: dev
:host: ubuntu

workshop exec -- rustup default nightly

info: using existing install for nightly-x86_64-unknown-linux-gnu
info: default toolchain set to nightly-x86_64-unknown-linux-gnu

  nightly-x86_64-unknown-linux-gnu unchanged - rustc 1.101.0-nightly (1a2c4797e 2026-10-21)
```

Your selection is stored inside the workshop container, so it survives restarts. To confirm this, stop and start the workshop, then check the toolchain again:

```{terminal}
:copy:
:dir: ~/hello-workshop
:user: dev
:host: ubuntu

workshop stop

"rust-example" stopped
```

```{terminal}
:copy:
:dir: ~/hello-workshop
:user: dev
:host: ubuntu

workshop start

"rust-example" started
```

```{terminal}
:copy:
:dir: ~/hello-workshop
:user: dev
:host: ubuntu

workshop exec -- rustc --version

rustc 1.101.0-nightly (1a2c4797e 2026-10-21)
```

The workshop reports the nightly toolchain even after the restart, demonstrating that your selection persisted. To switch back to the `stable` toolchain:

```{terminal}
:copy:
:dir: ~/hello-workshop
:user: dev
:host: ubuntu

workshop exec -- rustup default stable

info: using existing install for stable-x86_64-unknown-linux-gnu
info: default toolchain set to stable-x86_64-unknown-linux-gnu

  stable-x86_64-unknown-linux-gnu unchanged - rustc 1.99.1 (58cf8f9c3 2026-10-13)
```

:::{note}
Refreshing the workshop re-runs the SDK setup, which resets the default toolchain back to `stable` and removes any toolchains installed since the last setup. Downloaded dependencies, however, persist across refreshes through the SDK's `cargo-registry` mount, so builds pick up where they left off.
:::


## Daily workflow with actions

Typing the full {command}`workshop exec` command for every build soon gets tedious. [Workshop actions](https://ubuntu.com/workshop/docs/how-to/customize-workshops/add-actions/) let you name the commands you run often and invoke them as targets of {command}`workshop run`: {command}`workshop run build` runs the `build` action. To list the actions of a workshop, use {command}`workshop actions`.

Add an `actions` section to the workshop definition:

```{code-block} yaml
:caption: `.workshop/rust-example.yaml`

name: rust-example
base: ubuntu@24.04
sdks:
  - name: rust
    channel: latest/stable

actions:
  build: cargo build "$@"
  test: cargo test "$@"
  lint: cargo clippy "$@"
  doc: cargo doc "$@"
```

Each action is a Bash command, and the `"$@"` expansion forwards every argument supplied after the action name into the command. For instance, `workshop run build --release` becomes `cargo build --release` inside the workshop.

Run the actions:

```{terminal}
:copy:
:dir: ~/hello-workshop
:user: dev
:host: ubuntu

workshop run build
```

```{terminal}
:copy:
:dir: ~/hello-workshop
:user: dev
:host: ubuntu

workshop run test
```

:::{note}
Actions are parsed on every {command}`workshop run`, so there is no need to refresh the workshop after editing them. In non-interactive scripts, where {command}`workshop run` cannot infer whether its argument names a workshop or an action, use the explicit {command}`workshop run -- build` form instead.
:::

The same pattern works for any command you run often; see [How to add actions to your workshop](https://ubuntu.com/workshop/docs/how-to/customize-workshops/add-actions/) for more ideas.


(rust-webapi-example)=
## Advanced example: expose a Rust web API to your host

So far, everything has run inside the workshop. In this section, you build a web service with the [`axum`](https://github.com/tokio-rs/axum) web framework and expose it to your host machine with a *tunnel* interface, so you can open it in a browser on the host.


:::
### Prerequisites
:::

- Workshop and LXD, installed as described in the [Workshop getting-started tutorial](https://ubuntu.com/workshop/docs/tutorial/part-1-get-started/).
- The {file}`hello-workshop` project directory from the previous sections.


:::
### Procedure
:::

1. Add the web framework dependencies to your package:

    ```{terminal}
    :copy:
    :dir: ~/hello-workshop
    :user: dev
    :host: ubuntu

    workshop exec -- cargo add axum
    ```

    ```{terminal}
    :copy:
    :dir: ~/hello-workshop
    :user: dev
    :host: ubuntu

    workshop exec -- cargo add tokio --features full
    ```

    ```{terminal}
    :copy:
    :dir: ~/hello-workshop
    :user: dev
    :host: ubuntu

    workshop exec -- cargo add serde_json
    ```

    Cargo resolves the latest compatible versions and records them in the {file}`Cargo.toml` manifest.

1. Replace the stub {file}`src/main.rs` program with a small web service:

    ```{code-block} rust
    :caption: `src/main.rs`

    use axum::{routing::get, Json, Router};

    async fn health() -> Json<serde_json::Value> {
        Json(serde_json::json!({ "status": "ok" }))
    }

    #[tokio::main]
    async fn main() {
        let app = Router::new()
            .route("/", get(|| async { "Hello from a Rust workshop!" }))
            .route("/health", get(health));

        let listener = tokio::net::TcpListener::bind("0.0.0.0:8080")
            .await
            .unwrap();
        axum::serve(listener, app).await.unwrap();
    }
    ```

1. Extend the {file}`.workshop/rust-example.yaml` configuration to include a slot and plug pair that exposes the application over the `localhost:8080` endpoint, and a `start` action to manage the application:

    ```{code-block} yaml
    :caption: `.workshop/rust-example.yaml`

    name: rust-example
    base: ubuntu@24.04
    sdks:
      - name: rust
        channel: latest/stable
        slots:
          webapp:
            interface: tunnel
            endpoint: localhost:8080
      - name: system
        plugs:
          webapp:
            interface: tunnel
            endpoint: localhost:8080
    actions:
      build: cargo build "$@"
      test: cargo test "$@"
      lint: cargo clippy "$@"
      doc: cargo doc "$@"
      start: cargo run "$@"
    ```

    Because the workshop runs in an isolated container, a service listening inside it is not reachable from your host by default. Workshop connects the two sides through interfaces: a slot offers a resource, and a plug consumes it. The tunnel interface forwards network traffic from one endpoint to another.

    In our example, we first define a slot for the {pkg}`rust` SDK, which provides the capability to expose a desired network endpoint through the tunnel interface. We then define a tunnel plug that consumes the capability provided by the Rust slot. Since the plug is defined for the `system` SDK, this routes the application endpoint to the host endpoint and allows us to access the application from the host.

1. Refresh the workshop to apply the new interfaces, and confirm the tunnel is in place:

   1. Refresh the environment:

      ```{terminal}
      :copy:
      :dir: ~/hello-workshop
      :user: dev
      :host: ubuntu

      workshop refresh

      "rust-example" refreshed
      ```

   1. View information about the workshop:

      ```{terminal}
      :copy:
      :dir: ~/hello-workshop
      :user: dev
      :host: ubuntu

      workshop info

      name:      rust-example
      base:      ubuntu@24.04
      project:   ~/hello-workshop
      hostname:  rust-example.hello-workshop.wp
      status:    ready
      runtime:   lxd-container
      notes:     –
      sdks:
        system:
          installed:  (2)
          tunnels:
            webapp:
              from:  127.0.0.1:8080/tcp
              to:    127.0.0.1:8080/tcp
        rust:
          tracking:   latest/stable
          installed:  1.99.1  2026-10-16  (49)
          mounts:
            cargo-registry:
              host-source:      …/e5faec78/rust-example/mount/rust/cargo-registry
              workshop-target:  /home/workshop/.cargo/registry
      ```

      The output now includes the `webapp` tunnel, forwarding `localhost:8080` on the host to `localhost:8080` inside the workshop. You can also inspect interface connections with the {command}`workshop connections` command:

      ```{terminal}
      :copy:
      :dir: ~/hello-workshop
      :user: dev
      :host: ubuntu

      workshop connections

      INTERFACE  PLUG                              SLOT                       NOTES
      mount      rust-example/rust:cargo-registry  rust-example/system:mount  -
      tunnel     rust-example/system:webapp        rust-example/rust:webapp   -
      ```

1. Start the application using the new action:

    ```{terminal}
    :copy:
    :dir: ~/hello-workshop
    :user: dev
    :host: ubuntu

    workshop run start
    ```

    The command keeps running while the server serves requests. Since we have exposed the application through the configured slot/plug pairing, we can then see the application in any browser on the host machine at the `http://localhost:8080` endpoint.

    To verify from the command line instead, run the following on the host:

    ```{terminal}
    :copy:
    :dir: ~/hello-workshop
    :user: dev
    :host: ubuntu

    curl http://localhost:8080/health

    {"status":"ok"}
    ```

    This confirms that the application is running correctly, and is accessible from your host. When you are done, stop the server by pressing {kbd}`Ctrl+C`.


## SDK reference

(rust-sdk-reference)=
The {pkg}`rust` SDK is published by Canonical and installs rustup together with the standard Rust toolchain. This section documents the interfaces the SDK defines.

### Plugs (resources this SDK consumes)

#### `cargo-registry`

- Interface: `mount`
- Workshop target: `/home/workshop/.cargo/registry`
- Purpose: Persists downloaded crate sources and registry caches on the host
  between workshop updates.

Installed toolchains and rustup configuration live inside the workshop container, under `/home/workshop/.rustup`. They survive stopping and starting the workshop, while a refresh re-runs the SDK setup and returns the toolchain state to the SDK defaults.

### Slots (resources this SDK provides)

This SDK doesn't define any slots out of the box. As shown in the {ref}`advanced example <rust-webapi-example>`, you can declare custom slots in your workshop definition to expose services, such as web applications, from the workshop to the host.


## For more information

The source code for the Rust SDK for Workshop is publicly available on GitHub: [rust-sdk](https://github.com/canonical/rust-sdk).