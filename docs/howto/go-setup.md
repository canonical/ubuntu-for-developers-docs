(install-golang)=
# How to set up a development environment for Go on Ubuntu

Go is a popular language for back-end web development, microservices and CLI tools. This how-to guide outlines how to install a Go distribution and set up a development environment on Ubuntu.


## Installing and setting up Go

Go includes the `go` command, a compiler and other tools. You can install Go as a Debian package or as a snap. Snap provides a larger number of Go versions but — unlike a Debian package — these cannot be installed in a Docker container.

:::{note}
See [Precompiled Go binaries](#precompiled-go-binaries) for instructions on how to install Go without a package manager.
:::


### Debian package

1. Update the list of available packages:

    ```none
    sudo apt update
    ```

2. Install the latest version of Go:

    ```none
    sudo apt install golang-go
    ```

3. Confirm successful installation with:

    ```none
    go version
    ```

:::{note}
To install a specific version of Go use:

```none
sudo apt install golang-<version>
```
:::


### Snap package

1. Install the latest Go snap:

    ```none
    sudo snap install go --classic
    ```

2. Confirm successful installation:

    ```none
    go version
    ```

:::{note}
To install a specific version of Go, specify the channel; for example:

```none
sudo snap install go --channel=1.22/stable --classic
```
:::


### Adding the Go binary to `$PATH`

When not using a package manager to install Go, you need to add the Go binary to your `$PATH` environment variable.

* To temporarily add `go` to your `$PATH`, run:

    ```none
    export PATH=$PATH:/path/to/your/go/bin
    ```

* To persist the change and make `go` available in new terminal sessions and across reboots, append the above line to `$HOME/.profile` (or `/etc/profile`) and source the file:

    ```none
    source $HOME/.profile
    ```

:::{note}
The files to modify and commands to use when modifying the `$PATH` may vary depending on your shell environment.
:::


(precompiled-go-binaries)=
### Precompiled Go binaries

Precompiled Go binaries are available in a compressed format on the [release page](https://go.dev/dl/) of the official Go website.

1. Fetch a specific Go version with `wget`:

    ```none
    wget https://go.dev/dl/go<version>.linux-amd64.tar.gz 
    ```

2. Extract the files into an appropriate directory:

    ```none
    sudo tar -C /usr/local -xzf go<version>.linux-amd64.tar.gz
    ```

3. Add the `go` binary to your `$PATH` environment variable:

    ```none
    export PATH=$PATH:/usr/local/go/bin
    ```

### Downloading and using multiple Go versions

Sometimes it may be necessary to run multiple Go versions on the same machine.

1. To install Go versions 1.21 and 1.23, run:

    ```none
    sudo apt install golang-1.21 golang-1.23
    ```

   Each `go` binary is installed in `/usr/lib/go-<version>/bin/`

2. Test the `go` binaries by calling them with their full paths:

    ```none
    /usr/lib/go-1.21/bin/go version
    /usr/lib/go-1.23/bin/go version
    ```


## Editing and debugging

While it is possible to write and edit Go code using any plain-text editor, various Integrated Development Environments (IDEs) offer features to simplify the development process.

Advanced text editors can also be extended using Language Server Protocol plugins to enhance the user experience.


### Integrated Development Environments and editors

Some of the most common IDEs used for Go are:

- [Visual Studio Code](https://code.visualstudio.com/): a free editor with a dedicated [Go extension](https://marketplace.visualstudio.com/items?itemName=golang.Go) maintained by the Go Team
- [GoLand](https://www.jetbrains.com/go/): a paid editor developed specifically for the Go programming language

Both can be installed as snaps:

```none
sudo snap install code --classic
```

```none
sudo snap install goland --classic
```

### Delve debugger and official Go language server

IDEs used for Go development commonly rely on [Delve](https://github.com/go-delve/delve) for debugging.
Delve can also be installed as a standalone program and run [on the command line](https://github.com/go-delve/delve/blob/master/Documentation/cli/getting_started.md).

To install Delve, run:

```none
sudo apt install delve
```

An overview of basic Delve use is included in our {ref}`use-go` tutorial.

A Go language server, [gopls](https://pkg.go.dev/golang.org/x/tools/gopls), is actively maintained, which has helped ensure that Go is widely supported across many editors, including Emacs, (Neo)Vim, and others.

To install gopls from the Ubuntu archive:

```none
sudo apt install gopls
```

:::{note}
If you have Go installed and `go` in your `$PATH`, then the latest version of many Go tools like `gopls` and Delve can be installed with:

```none
go install url/of/tool/<name-of-tool>@latest
```

This is useful when you need a version of a tool that is not yet available through the package manager.
:::


## Cross-compilation

Go has excellent cross-platform build capabilities. To build a program called `hello.go`, containing valid Go code, run:

```none
go build hello.go
```

This builds a binary that can be run on your Ubuntu system.Different target systems can be set for the compiler.

To set the environment for a Windows AMD64 build, run:

```none
export GOOS=windows GOARCH=amd64
```

This causes `go build` to create a `hello.exe` binary that runs on Windows.

To test the (Linux) binary, execute it by running:

```none
./hello
```

:::{note}
For the basics of writing and testing a 'Hello, world~' program in Go, see our {ref}`use-go` tutorial.
:::


### Building for multiple targets

For a full list of targets, run:

```none
go tool dist list
```

For this example, filter the output to Windows and Linux on `amd`:

```none
go tool dist list | grep 'amd' | grep -E 'windows|linux'
```

Create a Makefile that automatically sets the build environment and creates executable binaries for both Windows and Linux platforms:

```make
EXE=heygo
WINDOWS=$(EXE)_win_amd64.exe
LINUX=$(EXE)_linux_amd64

.PHONY: all clean

all: windows linux

windows: $(WINDOWS)
linux: $(LINUX)

$(WINDOWS):
  env GOOS=windows GOARCH=amd64 go build -v -o $(WINDOWS) -ldflags="-s -w" ./heygo.go

$(LINUX):
  env GOOS=linux GOARCH=amd64 go build -v -o $(LINUX) -ldflags="-s -w" ./heygo.go

clean:
  rm -f $(WINDOWS) $(LINUX)
```

Generate the builds and test the Linux build:

```none
make all
./hello_linux_amd64
```


## What next

See the tutorial introducing the use of Go and related tooling: {ref}`use-go`.
