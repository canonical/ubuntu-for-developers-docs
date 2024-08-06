# How to contribute documentation

This guide provides information necessary to contribute to the Ubuntu for Developers documentation, especially if you're contributing for the first time.


## Reporting an issue

To report a mistake in or make request for the documentation, [file an issue](https://github.com/canonical/ubuntu-for-developers-docs/issues) about it in our bug tracker on GitHub.
to it.


## Modifying documentation online

Each documentation page rendered on the web contains an **Edit this page** link in the top-right corner. Clicking this button leads you to the GitHub web editor where you can propose changes to the corresponding page.

Remember to first check the [latest version](https://netplan.readthedocs.io/en/latest/) of our documentation and make your proposal based on that revision.


## Contributing on GitHub

To follow a Git development workflow, `checkout` the [Ubuntu for Developers repository](https://github.com/canonical/ubuntu-for-developers-docs/) and contribute your changes as [pull requests](https://github.com/canonical/netplan/pulls).


## Directory structure

All the documentation files are located in the `docs/` directory. The `docs/` directory contains sub-directories corresponding to different [Diátaxis](https://diataxis.fr/) sections:

* `explanation/`
* `howto/`
* `reference/`
* `tutorial/`

Add new articles in the appropriate directory. You can read about [how Ubuntu implements Diátaxis for documentation](https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation).


## Building the documentation

Follow these steps to build the documentation on your local machine.


### Prerequisites

* Git
* The `make` tool
    :::{note}
    The `make` command is compatible with Unix systems. If you're on Windows, you can [install Ubuntu with WSL to follow along](https://github.com/canonical/open-documentation-academy/blob/main/getting-started/start_with_WSL.md).
    :::


### Procedure

1. Fork the [Ubuntu for Developers repository](https://github.com/canonical/ubuntu-for-developers-docs/). Visit [Fork a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) for instructions.

2. Clone the repository to your machine:
    ```none
    git clone git@github.com:<your_user_name>/ubuntu-for-developers-docs.git
    ```

3. Create a new branch:
    ```none
    git checkout -b <your_branch_name>
    ```

4. Change to the `docs/` directory and make your contribution:
    ```
    cd docs
    ```

5. Build a live preview of the documentation from within the `docs/` directory:
    ```
    make run
    ```
    You can find all the HTML files in the `.build/` directory.

    `make run` uses the Sphinx `autobuild` module, so that any edits you make (and save) as you work are applied, and the built HTML files refresh immediately.

6. Review your contribution in a web browser by navigating to [127.0.0.1:8000](http://127.0.0.1:8000/).

7. Push your contribution to GitHub and create a pull request against the original repository.


## Documentation format

The Ubuntu for Developers documentation is built with Sphinx using the MyST flavour of the Markdown mark-up language. If you're new to Markdown or MyST, read our [MyST style guide](https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide-myst/).


## Testing the documentation

Test the documentation before submitting a pull request. Run the following commands from within the `docs/` directory to test the documentation locally:

| command  | use |
|---------|-----|
| `make spelling` | Check for spelling errors; this command checks the HTML files in the `_build` directory. Fix any errors in the corresponding Markdown file |
| `make linkcheck` | Check for broken links |
| `make woke` | Check for non-inclusive language |
| `make pa11y` | Check for accessibility issues |

:::{note}
For the `make spelling` command to work, you must have the `aspell` spellchecker installed. You can install it with `sudo apt-get install aspell`.
:::
