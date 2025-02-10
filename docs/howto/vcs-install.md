# How-to install & configure Version Control System (VCS) for development on Ubuntu

Version control systems (VCS) track and manage code changes, enabling teams to collaborate efficiently, revert to previous versions, and maintain a history of modifications. Git is the most widely used version control system; however, others like [Concurrent Version System (CVS)](https://www.nongnu.org/cvs/), [Apache Subversion (SVN)](https://subversion.apache.org/), [Mercurial](https://www.mercurial-scm.org/), and Bazaar are also available for those who require them for specific use cases.

## Configuring Git

1. Ubuntu comes with Git pre-installed; you can run the command below to check your Git version:

  ```bash
  git --version
  ```

2. Add your username and email to your Git account to configure your identity, which will be attached to your commits.

  Set your username:

  ```jsx
  git config --global user.name "Your Name"
  ```

  Set your email address:

  ```jsx
  git config --global user.email "youremail@example.com"
  ```

  :::{note}

  You can override your previously set username and email by rerunning the command.

  :::

3. To collaborate with others using Git, you need to connect your local Git instance to a remote Git repository like GitHub or GitLab. You can connect to them securely using an SSH key.

Generate an SSH key pair (if you don’t have one already):

  ```jsx
  ssh-keygen -t ed25519 -C "youremail@example.com"
  ```

  :::{note}

  For information on how to add an SSH to GitHub, refer to GitHub’s documentation on [_Adding a new SSH key to your GitHub account_](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux). For GitLab, refer to GitLab’s documentation on [_Adding an SSH key to your GitLab account_](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account).

  :::

## Launchpad considerations

Launchpad is the remote repository manager Ubuntu uses for various distribution purposes. You do not need it for normal development. However, if you want to participate in developing the Ubuntu distro, you have to [set up and use Launchpad](https://documentation.ubuntu.com/launchpad/en/latest/how-to/running-quickstart/).

## Best practices for using Git

Below are some best practices you can consider when using Git.

- **Writing meaningful commit messages**: Ensure that your commit messages are meaningful and consistent to provide context to the changes your commit introduces.
- **Using Git Aliases**: Git aliases allow you to configure shorthand alternatives to longer Git commands. For example, if you set `ci` as the alias for the `commit` command, running `git ci` would perform the same function as running `git commit`. For more information on Git aliases, refer to Git’s documentation on [_Git aliases_](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases).
- **Using .gitignore files**: Not all files need to be tracked by version control. You can use a **.gitignore** file to specify files you want Git to ignore. You can find a list of standard **.gitignore** templates in [_GitHub’s gitignore repository_](https://github.com/github/gitignore).
- **Pulling before pushing**: Always pull the latest changes from a remote repository before pushing to avoid conflicts and keep your local branch up to date.

## Useful tooling for Git

For a more productive development experience with Git, consider these tools:

- **Dedicated Git Shells**: Using a dedicated Git shell like Git bash can improve your Git workflow with features like auto-completion and colour-coded branches.
- **Text User Interfaces (TUI)**: Git TUIs like Tig provide a visual way to interact with Git in the terminal, making it easier to navigate commits and branches.
- **Graphical User Interfaces (GUI)**: Git GUIs like GitKraken provide a graphical interface to manage repositories instead of using the command line.
- **Git Hooks**: Git hooks are scripts that trigger actions at specific Git events (e.g., before a commit, after a push). This enables you to enforce coding standards, prevent commits with errors or unformatted code, and automate tasks such as linting, formatting, and commit message validation.

## Additional Resources

- [Writing meaningful commit messages](https://www.conventionalcommits.org/en/v1.0.0/#summary)
- [Getting started with Git Hooks](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks)
