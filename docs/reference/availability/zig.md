---
myst:
  html_meta:
    description: "Zig versions available via the Zig snap and Ubuntu packages across Ubuntu releases."
---

(zig-toolchain-availability)=
# Available Zig versions

This page lists Zig versions available via the Zig snap and Ubuntu packages.


## Ubuntu Zig (deb) packages

Zig packages are available in the Ubuntu archive from Ubuntu 25.10 onward. They are in the `universe` component.

| Ubuntu version | Available Zig versions | {lpsrc}`zig-defaults` version |
| --- | --- | --- |
| 26.04 LTS (Resolute Raccoon) | 0.14, 0.15 | 4ubuntu2 |
| 25.10 (Questing Quokka)      | 0.14        | 4ubuntu1 |

:::{note}
Zig packages are not available in Ubuntu releases before 25.10 (Questing Quokka). On older releases, install Zig using the snap or download a pre-built binary from [ziglang.org/download](https://ziglang.org/download/).
:::

| Zig version | Source package |
|-------------|----------------|
| 0.15 | {lpsrc}`zig0.15` |
| 0.14 | {lpsrc}`zig0.14` |


## Zig snap

The [`zig` snap](https://snapcraft.io/zig) is a community-maintained package. It does not publish a `latest/stable` channel; the `latest/beta` channel tracks Zig stable releases.

| Zig version | Snap channel |
|-------------|--------------|
| 0.17.0-dev  | `latest/edge` |
| 0.16.0      | `latest/beta` |
