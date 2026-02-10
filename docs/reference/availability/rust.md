(rust-toolchain-availability)=
# Available Rust versions

## Rustup snap

The [`rustup` snap](https://snapcraft.io/rustup) provides an installer for the programming language Rust. It releases Rust to three different "channels": `stable`, `beta`, and `nightly`.

| Rustup channel | Description |
|----------------|-------------|
| `stable` | releases are made every 6 weeks (with occasional point releases) |
| `beta` | the version that will appear in the next stable release |
| `nightly` | releases are made every night |

See the [user guide for rustup](https://rust-lang.github.io/rustup/concepts/channels.html) for more details about  available Rust versions.

## Ubuntu Rust (deb) packages

| Ubuntu version | available Rust versions | {lpsrc}`rust-defaults` version | 
| --- | --- | --- |
| 26.04 LTS (Resolute Raccoon)| **1.88** | 1.88 |
| 25.10 (Questing Quokka)     | **1.85**, 1.88 | 1.85 |
| 25.04 (Plucky Puffin)       | 1.81, 1.82, 1.83, **1.84** | 1.84 |
| 24.04 LTS (Noble Numbat)    | 1.74, **1.75**, 1.76, 1.77, 1.78, 1.79, 1.80, 1.81, 1.82 | - |
| 22.04 LTS (Jammy Jellyfish) | 1.62, **1.75**, 1.76, 1.77, 1.78, 1.79, 1.80, 1.81, 1.82 | - |
| 20.04 LTS (Focal Fossa)     | 1.75, 1.76, 1.77, 1.78, 1.79, 1.80, 1.82 | - |
| 18.04 LTS (Bionic Beaver)   | 1.75 | - |
| 16.04 LTS (Xenial Xerus)    | 1.75 | - |
| 14.04 LTS (Trusty Tahr)     | 1.75 | - |

<!-- Do not forget to add 4 spaces at the end of line to keep future diffs more readable -->
**bold** -- package is in main    

| Rust version | Source package | 
|--------------|----------------|
| 1.88 | {lpsrc}`rustc-1.88` |
| 1.85 | {lpsrc}`rustc-1.85` |
| 1.84 | {lpsrc}`rustc-1.84` |
| 1.83 | {lpsrc}`rustc-1.83` |
| 1.82 | {lpsrc}`rustc-1.82` |
| 1.81 | {lpsrc}`rustc-1.81` |
| 1.80 | {lpsrc}`rustc-1.80` |
| 1.79 | {lpsrc}`rustc-1.79` |
| 1.78 | {lpsrc}`rustc-1.78` |
| 1.77 | {lpsrc}`rustc-1.77` |
| 1.76 | {lpsrc}`rustc-1.76` |
| 1.75 | {lpsrc}`rustc-1.75` |
| 1.74 | {lpsrc}`rustc-1.74` |
| 1.62 | {lpsrc}`rustc-1.62` |

## Ubuntu Rust package removal policy

Before the current devel series gets released, certain Rust toolchain packages may be removed from the devel archive.

Currently, the policy is to keep the **three most recent** Rust toolchain versions in a given Ubuntu series' archive. However, if specific older releases are needed by kernels or important packages in main, then older toolchain versions may be retained.

## Ubuntu Rust package backport policy

The Rust team prepares backports for the previous two LTS releases. Currently, they are not uploaded to the backports pocket unless they are required by something specific.

For example, Rust 1.90 was added during the 26.04 development cycle, and backports to 24.04 and 22.04 have been built and tested, but the backports won't be added to the 24.04 and 22.04 archives unless something else requires them.
