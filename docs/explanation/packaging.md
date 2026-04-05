---
myst:
  html_meta:
    description: "Package software as a Debian package, snap, or container image on Ubuntu."
---

(packaging)=
# Packaging software

This article describes how to package software as a Debian package, snap, or container image.

There are different ways to distribute an application. It is possible to directly send
the source code to users, who will then have to build it themselves. It is also possible
to give out pre-compiled binaries that the users will download, copy to the right place and use.
Those methods are not very convenient.

The best way to distribute an application is to have it
**packaged**. This way, the package manager handles installation, so everything is transparent to
the user (no additional work required), and it can also handle updates.

An application can be made into different kinds of packages:
- Operating system package, like Debian/Ubuntu `.deb` package
- Universal package, for distribution across the whole Linux ecosystem, like snaps
- OCI images, to be used in container format by a container runtime (e.g. cloud environments)

| Packaging type    | Example format/tools | Target                       |
|-------------------|----------------------|------------------------------|
| OS package        | .deb                 | OS integration               |
| Universal package | .snap                | Universal Linux distribution |
| OCI image         | Docker               | Cloud deployment             |

## Making a Debian/Ubuntu package

There are two cases in which you may want to make a Debian package:

Direct integration into the Debian and Ubuntu operating systems
: This is a complex process that requires the involvement of Debian Developers or Ubuntu core developers. Usually, it is not the upstream developer who makes a package for Debian/Ubuntu directly, unless they are a Debian/Ubuntu developer themselves.

Distributing the Debian package using your own channels
: This can be a [Personal Package Archive (PPA)](https://documentation.ubuntu.com/project/how-ubuntu-is-made/concepts/glossary/#term-PPA) or a direct download. The PPA is preferred as users would be able to add your PPA to their package management system and receive automatic updates.

### Packaging

[Create a new package](https://documentation.ubuntu.com/project/contributors/new-package/create-a-new-package/) from the Ubuntu project documentation explains the process. There are many ways of creating a Debian/Ubuntu package; the Debian documentation, as well as external tutorials and how-tos, are available, each presenting different tools and methods.

### Building and distributing with a PPA

To make a PPA and build your package inside, follow [Build packages in a PPA](https://documentation.ubuntu.com/project/contributors/bug-fix/build-packages-in-a-ppa/).

Then, your users will be able to add your PPA to install your software:
```
sudo add-apt-repository ppa:<user>/<ppa_name>
sudo apt update
sudo apt install <your-software>
```

## Crafting a Snap package

For a tutorial on crafting a fully-functional snap of a Python application, see [Craft a snap](https://documentation.ubuntu.com/snapcraft/stable/tutorials/craft-a-snap/). The Snapcraft documentation also includes information about every part of the crafting process.

For more generic information about snap packages, from a user perspective, see the [Snap documentation](https://snapcraft.io/docs/).

## Containerizing

Docker is one of the most commonly used container runtimes, and their documentation includes resources on containerization:
- [Docker workshop: containerize an application](https://docs.docker.com/get-started/workshop/02_our_app/)
- [Docker concepts: building images](https://docs.docker.com/get-started/docker-concepts/building-images/)

Canonical, the creator of Ubuntu, also has a tool to create production-grade container images: [Rockcraft](https://documentation.ubuntu.com/rockcraft/stable/). Rockcraft allows to make efficient container images, called *rocks*, which are based on Ubuntu. This has the benefits of Ubuntu support, while being smaller in footprint than regular images.

For guidance on how to use Rockcraft, see [Rockcraft tutorial](https://documentation.ubuntu.com/rockcraft/latest/tutorial/#tutorial).

