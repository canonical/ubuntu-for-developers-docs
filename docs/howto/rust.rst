Setup Development Environment for Rust on Ubuntu
================================================

Rust is a relatively new and secure programming language supported on many platforms.
This guide will walk you through setting up a development environment for Rust on Ubuntu.

The easiest way to get started is to install `rustup` manager from Snap Store: https://snapcraft.io/rustup.
If you prefer to use a terminal, here is the command-line version:

.. code-block:: bash

    snap install rustup

After installing `rustup`, you can use it to install the latest stable Rust version:

.. code-block:: bash

    rustup install stable

Next, you can create a new Rust project using Cargo:

.. code-block:: bash

    cargo new hello_world

Now, change to the project directory:

.. code-block:: bash

    cd hello_world

You will notice that Cargo has already set up a Git repository with a skeleton project inside.
To build and run the program, use the following commands:

.. code-block:: bash

    cargo run

.. note::
    Many external Rust libraries on `crates.io <https://crates.io>`_  contain C/C++ code, which require a 
    working C/C++ compiler to be installed on your system.

    You can use the following command to install them:

    .. code-block:: bash

        sudo apt-get install build-essential


If your project needs unstable Rust features that are not present in the latest stable toolchain, try the nightly Rust toolchain builds.
To install the nightly toolchain, use:

.. code-block:: bash

    rustup install nightly

By default, the nightly builds are not selected; you will need to build your project using a special command:

.. code-block:: bash

    cargo +nightly build

To run the project, use the following command:

.. code-block:: bash

    cargo +nightly run


IDE Integrations
----------------

Many editors and IDEs (Integrated Development Environment) come with various degrees of Rust support.
Here are some popular ones:

- `Visual Studio Code <https://snapcraft.io/code>`_: Install the ``rust-analyzer`` extension from the `VSCode Marketplace <https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer>`_.
- `JetBrains RustRover <https://snapcraft.io/rustrover>`_ (Paid): Comes with full Rust support by default.
- `Helix Editor <https://helix-editor.com/>`_: Comes with full Rust support if you have already done ``rustup component add rust-analyzer``.
- `Zed Editor <https://zed.dev/download>`_: Comes with full Rust support if you have already done ``rustup component add rust-analyzer``.

Build for Other Platforms
-------------------------

You can also develop Rust applications for other platforms on Ubuntu.
To do this, you must install the necessary tools and libraries for each platform.

For example, to target Microsoft Windows (R), you might want to do a setup like this:

.. code-block:: bash

    sudo apt-get install binutils-mingw-w64 g++-mingw-w64 gcc-mingw-w64
    rustup target add x86_64-pc-windows-gnu

Then, you can build your project using the following command:

.. code-block:: bash

    cargo build --target x86_64-pc-windows-gnu


A lot of Rust applications can run inside a web browser.
You can build your Rust project for web browsers using the WebAssembly (``wasm``) target.

.. code-block:: bash

    sudo apt-get install clang lld # for wasm linkers
    rustup target add wasm32-unknown-unknown
    cargo build --target wasm32-unknown-unknown

To see a list of platforms that you can build on Ubuntu, use the following command:

.. code-block:: bash

    rustup target list

.. warning::

    Some targets on that list will require installing additional packages or download SDKs from third-party websites.
    See `Rust's official documentation <https://doc.rust-lang.org/rustc/platform-support.html>`_ for details.

Debugging Tooling
-----------------

Your code editor or IDE probably already has debugging functionalities tailored for Rust applications.
If not, you can easily debug Rust applications on Ubuntu using familiar debugging tools like ``gdb`` and ``lldb``.
Install the corresponding debugging support packages from Ubuntu archive:

.. code-block:: bash

    sudo apt-get install gdb lldb rust-gdb rust-lldb

You can then use ``gdb`` or ``lldb`` to debug your Rust application like normal.
