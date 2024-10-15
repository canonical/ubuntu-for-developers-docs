# How to set up development environment for Go on Ubuntu

Go is a popular language for backend web development,
microservices and CLI tools. This how-to guide outlines
how to install a Go distribution and set up a development
environment on Ubuntu.

## Installing and setting up Go

A Go installation includes the `go` command,
a compiler and other tools. 

There are multiple ways to install the Go toolchain on Ubuntu.

After using any installation method, confirm that
you have installed a specific version of Go with:

```none
go version
```

### Package managers

Installing Go with a package manager is a convenient option.
This method does not require manually adding the `go` binary
to your `$PATH` and future updates can be handled through the package manager.

```{note}
Depending on the package manager used, the latest version of Go
may not be available.
See [Precompiled Go binaries](#precompiled-go-binaries) for instructions
on how to install the latest version of Go without a package manager.
```

#### Snap

Go can be installed as a snap:

```none
sudo snap install go --classic
```

You can print a list of available Go releases with:

```none
snap info go
```

To switch between release versions use `refresh`:

```none
sudo snap refresh go --channel=1.22/stable --classic
```

#### Debian package

To install Go using the default Ubuntu package manager:

```
sudo apt install golang-go
```

### Precompiled Go binaries

Precompiled Go binaries are available in a compressed format on the [release page](https://go.dev/dl/) of the official Go website and can be fetched with `wget`:

```none
wget https://go.dev/dl/go<version>.linux-amd64.tar.gz 
```

Extract the files into an appropriate directory:

```none
sudo tar -C /usr/local -xzf go<version>.linux-amd64.tar.gz
```

Add the `go` binary to your `$PATH` environment variable:

```none
export PATH=$PATH:/usr/local/go/bin
```

### Downloading and using different Go versions

Multiple Go versions can be installed on the same machine.

```{note}
Go must be installed to use `go install` and `go build`.
```

Fetch a specific version from the Go website:

```none
go install golang.org/dl/go{version-number}@latest
```

Ensure that Go binaries are available in your `$PATH`:

```none
export PATH=$PATH:$HOME/go/bin
```

Download a specific Go version:

```none
go{version-number} download
```

To use the version of Go that you downloaded, append
the version number to the `go` command:

```none
go{version-number} version
```

### Building from source

```{note}
To build Go from source, you need a Go compiler installed on your machine.
```

#. Clone the Go repository, then change into the cloned repository:

```none
git clone https://github.com/golang/go build-go-from-source
cd build-go-from-source
```

Change into the subdirectory containing the source code and run the script to build the Go binary:

```none
cd src/
./all.bash 
```

```{note}
Building Go from source may take several minutes.
```

If successful, the output indicates where the binary has been installed on your machine.
Add this to your ``PATH`` to enable calling the version of Go that you have compiled.

```none
ALL TESTS PASSED
---
Installed Go for linux/amd64 in /home/username/build-go-from-source
Installed commands in /home/username/build-go-from-source/bin
*** You need to add /home/ubuntu/build-go-from-source/bin to your PATH.

```

To update Go to the latest version, pull the latest changes into the repository and rebuild the binary.

## Editing and debugging

Some of the most common Integrated Development Environments used for Go are:

- Visual Studio Code: a free editor with a dedicated [Go extension](https://marketplace.visualstudio.com/items?itemName=golang.Go) maintained by the Go Team
- GoLand: [GoLand](https://www.jetbrains.com/go/) is a paid editor developed specifically for the Go programming language

Both Visual Studio Code and GoLand rely on [Delve](https://github.com/go-delve/delve) for debugging.
Delve can also be installed as a standalone program and run [on the command line](https://github.com/go-delve/delve/blob/master/Documentation/cli/getting_started.md).

A Go language server [gopls](https://pkg.go.dev/golang.org/x/tools/gopls) is actively maintained, which has helped ensure that Go is widely supported across many editors, including Emacs, (Neo)Vim and others. Install it by running:

```none
go install golang.org/x/tools/gopls@latest
```

## Cross-compilation

```{note}
For the basics of writing and testing Go code see
our [how to develop with Go](./go-use.md) guide.
```

Go has excellent cross-platform build capabilities.
To build a Go program called `hello.go`, run:

```none
go build hello.go
```

This builds a binary that can be run on your Ubuntu system.
Different target systems can be set for the compiler.
To set the environment for a Windows amd64 build, run:

```none
export GOOS=windows GOARCH=amd64
```

Running `go build` creates a `hello.exe` binary that runs on Windows.

To test the (Linux) binary, execute it by running:

```none
./hello
```

### Building for multiple targets

For a full list of targets, run:

```none
go tool dist list
```

For this example, filter the output to Windows and Linux on `amd`:

```none
go tool dist list | grep 'amd' | grep -E 'windows|linux'
```

Create a makefile that automatically sets
the build environment and creates executable binaries for
both Windows and Linux platforms:

```make
EXE=heygo
WINDOWS=$(EXE)_win_amd64.exe
LINUX=$(EXE)_lin_amd64

.PHONY: all clean

all: windows linux

windows: $(WINDOWS)
linux: $(LINUX)

$(WINDOWS):
	env GOOS=windows GOARCH=amd64 go build -v -o $(WINDOWS) -ldflags="-s -w"  ./heygo.go

$(LINUX):
	env GOOS=linux GOARCH=amd64 go build -v -o $(LINUX) -ldflags="-s -w"  ./heygo.go

clean:
	rm -f $(WINDOWS) $(LINUX)
```

Test the builds on your code:

```none
make all
./hello_lin_amd64
```

