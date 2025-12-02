(use-git)=
# Using Git version control on Ubuntu

Version control systems (VCS) track and manage code changes, enabling teams to collaborate efficiently, revert to previous versions, and maintain a history of modifications. Git is the most widely used version control system; however, others including [Concurrent Version System (CVS)](https://www.nongnu.org/cvs/), [Apache Subversion (SVN)](https://subversion.apache.org/), [Mercurial](https://www.mercurial-scm.org/), and Bazaar are also available for those who require them for specific use cases.

This article focuses on Git -- the {spellexception}`de facto` standard in software development.


## Git

Git is a decentralized source-code management system that provides for efficient branch use, ability to perform complex merges, and archive integrity. To read more about the system, see its official website at [Git SCM](https://git-scm.com/).

:::{tip}
Git documentation can also be installed for local viewing in a web browser.

To get it:

```none
sudo apt install -y git-doc
```

To view it using Firefox:

```none
firefox /usr/share/doc/git-doc/index.html
```
:::


### Getting Git

To install Git on Ubuntu Desktop, use the regular package management system (package {pkg}`git`). If your specific use case requires it, there is also a snap package, [`git-scm`](https://snapcraft.io/git-scm).

To install the DEB package, run:

```none
sudo apt install -y git
```

To install the snap package, run:

```none
sudo snap install git-scm
```


### Configuring Git

Initial Git configuration is described in detail in official documentation at [First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

When using Git for both personal and professional development, consider conditioning some settings based on repository properties. For example, to configure multiple email addresses for commit logs depending a given repository, use one or more keywords with the `includeIf` variable.

**Example: conditional include based on a local directory**

1. Add the following variable definition to the {pkg}`~/.gitconfig` configuration file:

    ```{code-block} ini
    :caption: `~/.gitconfig`

    ; configuration file to use for repositories under $HOME/git/example-com/
    [includeIf "gitdir:~/git/example-com/"]
        path = ~/.gitconfig_example
    ```

2. Provide specific configuration in the file included above:

    ```{code-block} ini
    :caption: `~/.gitconfig_example`

    ; configuration differing from global settings
    [user]
        email = user@example.com
    ```

See the reference documentation for the {command}`git config` command (including examples of configuration files) at [`git-config`](https://git-scm.com/docs/git-config).


### Git and hosting providers

To collaborate with others using Git, connect your local Git instance to a remote Git-hosting provider. This can be a Git server instance provided by your organization, or one of the publicly available Git-hosting services, such as GitLab, GitHub, or Launchpad.

A commonly used method of facilitating secure repository authentication is based on SSH keys. See {ref}`Ubuntu Server documentation on using SSH <openssh-server>` for instructions on how to work with SSH keys on Ubuntu.

To generate and use an SSH key pair:

1. Install the {pkg}`openssh-client` package:

    ```none
    sudo apt install -y openssh-client
    ```

2. Run the {command}`ssh-keygen` command:

    ```none
    ssh-keygen -t ed25519 -C "user@example.com"
    ```
3. Add the generated public key to your Git provider.

   For information on how to add an SSH key to various Git-hosting providers, see:

    * GitLab: [Adding an SSH key to your GitLab account](https://docs.gitlab.com/user/ssh/#add-an-ssh-key-to-your-gitlab-account)

    * GitHub: [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux)

    * Launchpad: {ref}`Registering an SSH key with Launchpad <import-your-ssh-keys>`


### Launchpad considerations

Launchpad is suite of tools for collaborating on software projects. Among other functions, it provides:

* Backend services for processes critical to the development of the Ubuntu Linux distribution.
* Git-hosting service for teams and individuals.

To participate in the development and maintenance of the Ubuntu Linux distribution, Launchpad is essential. See the official [Launchpad documentation](https://documentation.ubuntu.com/launchpad/user/).


### Suggestions for using Git

Below are some best practices you can consider when using Git:

Writing meaningful commit messages
: Ensure that your commit messages are meaningful and consistent to provide context to the changes your commit introduces. Consider adopting a common standard, such as [Conventional Commits](https://www.conventionalcommits.org/).

Using Git aliases
: Git aliases allow you to configure shorthand alternatives to longer Git commands. For example, if you set `ci` as the alias for the `commit` command, running {command}`git ci` would perform the same function as running {command}`git commit`. For more information on Git aliases, see Git documentation: [Git aliases](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases).

Using {file}`.gitignore` files
: Not all files need to be tracked by version control. You can use a {file}`.gitignore` file to specify files you want Git to ignore. Find a list of standard {file}`.gitignore` templates in [GitHub gitignore repository](https://github.com/github/gitignore).

Pulling before pushing
: Always pull the latest changes from a remote repository before pushing to avoid conflicts and keep your local branch up to date. For an overview of recommended workflows to use with Git, see the {manpage}`gitworkflows(7)` manual page, and especially its `DISTRIBUTED WORKFLOWS` section (available locally through {command}`git help workflows`).


### Useful tooling for Git

For a more productive development experience with Git, consider these tools:

Git shell helpers
: Using a Git shell helper, such as the bundled `git-prompt.sh`, can improve your Git workflow with features including auto-completion and branch names with repository status displayed as part of the command prompt in the terminal. To set it up, read the instructions in the {file}`/usr/lib/git-core/git-sh-prompt` file. See also [Git in Other Environments - Git in Bash](https://git-scm.com/book/id/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Bash).

Text user interfaces (TUI)
: Git TUIs, such as [Tig](https://jonas.github.io/tig/), provide a visual way to interact with Git in the terminal, making it easier to navigate commits and branches. Install with {command}`sudo apt install -y tig`.

Graphical user interfaces (GUI)
: Git GUIs, such as the basic [gitk](https://git-scm.com/docs/gitk) or GNOME-native [gitg](https://wiki.gnome.org/Apps/Gitg/), provide a graphical interface to manage repositories instead of using the command line. Install with {command}`sudo apt install -y gitk gitg`. See [GUI Clients](https://git-scm.com/downloads/guis?os=linux) for an overview of available applications (includes TUIs).

Git hooks
: Git hooks are scripts that trigger actions at specific Git events (e.g., before a commit, after a push). This enables you to enforce coding standards, prevent commits with errors or unformatted code, and automate tasks such as linting, formatting, and commit-message validation. See [Customizing Git - Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).


## Additional resources

- [First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
- [Writing meaningful commit messages](https://www.conventionalcommits.org/en/v1.0.0/#summary)
- [Getting started with Git Hooks](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks)
- [GUI Clients](https://git-scm.com/downloads/guis?os=linux)
- [Git in Other Environments - Git in Bash](https://git-scm.com/book/id/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Bash)
- [GitHub gitignore repository](https://github.com/github/gitignore)
- [Git aliases](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases)
