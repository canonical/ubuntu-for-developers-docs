# Ubuntu for Developers

This repository contains the sources for the [Ubuntu Desktop as a Developer Platform](https://canonical-ubuntu-for-developers.readthedocs-hosted.com/) documentation. The docs are hosted on Read the Docs:
[![Documentation Status](https://app.readthedocs.com/projects/canonical-ubuntu-for-developers/badge/?version=latest](https://app.readthedocs.com/projects/canonical-ubuntu-for-developers/builds/?version__slug=latest)


## About the documentation

The documentation provides guidance for using the [Ubuntu Desktop](https://ubuntu.com/desktop) distribution as a developer platform. The guide focuses on setting up the system as a workstation for developers, with an emphasis on the following toolchains:

* Java
* .NET
* Golang
* Python
* Rust
* GCC


## Contributing to documentation

To contribute to the documentation, follow these steps to get started:

1. Fork the repository and clone the resulting fork:
    ```
    git clone git@github.com:<your_user_name>/ubuntu-for-developers-docs.git
    ```

2. Create a new branch:
    ```
    git checkout -b <your_branch_name>
    ```

3. Change to the `docs/` directory and make your contribution:
    ```
    cd docs
    ```

4. Build a live preview of the documentation from within the `docs/` directory:
    ```
    make run
    ```

5. Review your contribution in a web browser by navigating to [127.0.0.1:8000](http://127.0.0.1:8000/).

6. Push your contribution to GitHub and create a pull request against the original repository.

For more details, refer to the [comprehensive contribution guide](https://canonical-ubuntu-for-developers.readthedocs-hosted.com/en/latest/howto/contribute-docs/).
