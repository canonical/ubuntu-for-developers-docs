# How to set up development environment for Go on Ubuntu

Go is a popular language for backend web development,
microservices and CLI tools. This how-to guide outlines
how to install a Go distribution and set up a development
environment on Ubuntu.

## Installing and setting up Go

Go includes the `go` command, a compiler and other tools and can be
installed with the default Ubuntu package manager

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
See [Precompiled Go binaries](#precompiled-go-binaries) for instructions
on how to install specific versions of Go without a package manager.
:::

### Adding Go binary to path

If you are not using a package manager to install Go, you need
to add the Go binary to your `$PATH`.

1. To temporarily add Go to your `$PATH`, run:

```none
export PATH=$PATH:/path/to/your/go/bin
```

2. To persist the change and make go available in new terminal sessions and across reboots, 
append the above line to `$HOME/.profile` (or `/etc/profile`) and source the file:

```none
source $HOME/.profile
```

:::{note}
The files to modify and commands to use when modifying the `$PATH` may vary
depending on your shell environment.
:::

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

Sometimes it may be necessary to run multiple Go versions
on the same machine.

The general command to install a specific version of Go is:

```none
sudo apt install golang-<version>
```

1. To install versions `1.21` and `1.23`, run:

```none
sudo apt install golang-1.21 golang-1.23
```

Each `go` binary will be installed in `/usr/lib/go-<version>/bin/`

2. Test the `go` binaries with:

```none
/usr/lib/go-1.21/bin/go version
/usr/lib/go-1.23/bin/go version
```

3. Optional: add binary to `$PATH`.

Make the name of the binary unique so that there is no
naming collision with any default `go` installation:

```none
sudo mv /usr/lib/go-1.21/bin/go /usr/lib/go-1.21/bin/go1.21
```

Then add it to your path `$PATH`:

```none
export PATH=$PATH:/usr/lib/go-1.21/bin
```

Test with:

```none
go1.21 version
```

4. Optional: create aliases for different Go versions.

For example, in a `.bashrc` file, add the lines:

```none
alias go1.21='/usr/lib/go-1.21/bin/go'
alias go1.23='/usr/lib/go-1.23/bin/go'
```

These can now be called separately:

```none
go1.21 version
```

```none
go1.23 version
```

## Editing and debugging

### Integrated Development Environments and editors

Some of the most common Integrated Development Environments (IDEs) used for Go are:

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

An overview of basic Delve usage is included in our [how to develop with Go](./go-use.md) guide.


A Go language server [gopls](https://pkg.go.dev/golang.org/x/tools/gopls) is actively maintained, which has helped ensure that Go is widely supported across many editors, including Emacs, (Neo)Vim and others. 

You can install gopls from the Ubuntu archive:

```none
sudo apt install gopls
```

:::{note}
If you have Go installed and `go` on your `$PATH` then
the latest version of many Go tools like gopls and Delve can be installed with:

	go install url/of/tool/<name-of-tool>@latest

This can be useful if you need a version of a tool that is not yet available
through the package manager.
:::

## Cross-compilation

Go has excellent cross-platform build capabilities.
To build a program called `hello.go`, containing valid Go code, run:

```none
go build hello.go
```

This builds a binary that can be run on your Ubuntu system.
Different target systems can be set for the compiler.

To set the environment for a Windows amd64 build, run:

```none
export GOOS=windows GOARCH=amd64
```

This causes `go build` to create a `hello.exe` binary that runs on Windows.

To test the (Linux) binary, execute it by running:

```none
./hello
```

:::{note}
For the basics of writing and testing a Hello World program in Go
see our [how to develop with Go](./go-use.md) guide.
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

Create a makefile that automatically sets
the build environment and creates executable binaries for
both Windows and Linux platforms:

```make
EXE=heygo
WINDOWS=$(EXE)_win_amd64.exe
LINUX=$(EXE)_linux_amd64

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

Generate the builds and test the Linux build:

```none
make all
./hello_linux_amd64
```

