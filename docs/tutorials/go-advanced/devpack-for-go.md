---
myst:
  html_meta:
    description: "Use devpack-for-go to install Go development tools, configure command aliases, and set up VS Code on Ubuntu."
---

(devpack-for-go)=
# Devpack for Go

This tutorial shows how to use {pkg}`devpack-for-go` to install a set of Go development tools, configure command aliases, and integrate the tools with VS Code on Ubuntu. The devpack packages the tools in a single snap that works alongside the official Go snap.

For background on devpacks, see {ref}`devpacks`. For manual instructions on installing the Go toolchain, see {ref}`install-golang`.


## Installing the devpack

{pkg}`devpack-for-go` is a companion snap for the official Go snap. It packages commonly used Go development tools while using the Go toolchain from the Go snap. Install both snaps with:

```{terminal}
:copy:
:user: dev
:host: ubuntu

sudo snap install go --classic
```

```{terminal}
:copy:
:user: dev
:host: ubuntu

sudo snap install devpack-for-go --classic
```

The devpack includes the following tools:

- [Delve](https://github.com/go-delve/delve) -- a debugger for Go programs
- [`gopls`](https://pkg.go.dev/golang.org/x/tools/gopls) -- the official Go language server
- [`golangci-lint`](https://github.com/golangci/golangci-lint) -- a fast linter
- [`govulncheck`](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck) -- a vulnerability checker
- [`gotests`](https://github.com/cweill/gotests) -- a test generator
- [`gofumpt`](https://github.com/mvdan/gofumpt) -- a stricter formatter


## Running the setup guide

The {command}`setup-guide` command prints instructions for configuring command aliases and VS Code. Run it with:

```{terminal}
:copy:
:user: dev
:host: ubuntu

devpack-for-go.setup-guide
```

The guide covers two tasks.

### Enabling command aliases

Without aliases, each tool is available under its snap-qualified name, such as {command}`devpack-for-go.gopls`. To run the tools directly, create aliases with {command}`snap alias`:

```{terminal}
:copy:
:user: dev
:host: ubuntu

sudo snap alias devpack-for-go.delve dlv
sudo snap alias devpack-for-go.gopls gopls
sudo snap alias devpack-for-go.golangci-lint golangci-lint
sudo snap alias devpack-for-go.govulncheck govulncheck
sudo snap alias devpack-for-go.gotests gotests
sudo snap alias devpack-for-go.gofumpt gofumpt
```

### Configuring VS Code

To integrate the tools into VS Code, add the following block to your {file}`settings.json` file, usually at {file}`~/.config/Code/User/settings.json`:

```{code-block} json
:caption: `~/.config/Code/User/settings.json`

{
  "go.alternateTools": {
    "dlv": "/snap/bin/devpack-for-go.delve",
    "gopls": "/snap/bin/devpack-for-go.gopls",
    "golangci-lint": "/snap/bin/devpack-for-go.golangci-lint",
    "govulncheck": "/snap/bin/devpack-for-go.govulncheck",
    "gotests": "/snap/bin/devpack-for-go.gotests",
    "gofumpt": "/snap/bin/devpack-for-go.gofumpt"
  },
  "go.useLanguageServer": true,
  "go.lintTool": "golangci-lint",
  "go.formatTool": "gofumpt"
}
```

After updating the settings, restart VS Code or run **Developer: Reload Window**.


## Using the tools

The tools installed by the devpack work on any Go project. To try them, create a small project:

```{terminal}
:copy:
:user: dev
:host: ubuntu

mkdir heygo && cd heygo
```

```{terminal}
:copy:
:user: dev
:host: ubuntu
:dir: ~/heygo

go mod init youruser.github.com/heygo
```

Create a source file with a deliberate formatting issue:

```{code-block} go
:caption: `heygo.go`

package main

import "fmt"

func greeting() string {
return "Hey Go!"
}

func main() {
fmt.Println(greeting())
}
```

### Formatting with `gofumpt`

{command}`gofumpt` is a stricter formatter than the standard {command}`gofmt`. To reformat the file in place, run:

```{terminal}
:copy:
:user: dev
:host: ubuntu
:dir: ~/heygo

gofumpt -w heygo.go
```

The indentation of the {command}`return` and {command}`fmt.Println` statements is corrected.

### Linting with `golangci-lint`

To lint the project, run:

```{terminal}
:copy:
:user: dev
:host: ubuntu
:dir: ~/heygo

golangci-lint run
```

### Checking for vulnerabilities with `govulncheck`

To scan the project for known vulnerabilities, run:

```{terminal}
:copy:
:user: dev
:host: ubuntu
:dir: ~/heygo

govulncheck ./...
```

### Generating tests with `gotests`

To generate a test stub for the {command}`greeting` function, run:

```{terminal}
:copy:
:user: dev
:host: ubuntu
:dir: ~/heygo

gotests -all -w heygo.go
```

This creates a {file}`heygo_test.go` file with a generated test.

For a full guide to building, running, and debugging Go programs, including the Delve debugger, see {ref}`use-go`.


## What next

- {ref}`install-golang`
- {ref}`use-go`
- {ref}`devpacks`


## Additional resources

- [devpack-for-go source repository](https://github.com/canonical/devpack-for-go)
