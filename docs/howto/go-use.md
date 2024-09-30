# How to develop using Go on Ubuntu

This how-to guide will show you how to build and run a "hello world" program
using the Go toolchain on Ubuntu.
It will demonstrate some builtin tooling that is bundled with the default Go installation.
Lastly, it will cover some basic usage of the Delve debugger.

## Creating a Go module

Create a project directory and change into it:

```none
mkdir heygo && cd heygo
```

Create a file to be the main entry point of the program:

```none
touch heygo.go
```

Initialise the project as a Go module, giving the address of an online repo 
where you will host the source; alternatively, just use a temporary url for testing:

```none
go mod init youruser.github.com/heygo
```

## Writing the code

Open `heygo.go` in a text editor and add the following text:

```{code-block} go
:caption: `heygo.go`
package main

import "fmt"

func main() {
    fmt.Println("Hey Go!")
}
```

Here, the name of the package — `main` — is identified and the `fmt`
package is imported from Go's standard library.
A `main()` function is defined and a method is called from `fmt`
to print a line of text that is passed as an argument.

To compile and run your program use the `go run` command.
If you pass the current directory as an argument the Go compiler
will automatically find the main package and main function during
the build:

```none
go run .
```

This should output:

```none
Hey Go!
```

## Go tooling

The default Go installation includes several useful tools,
including tools for formatting (`gofmt`) and vetting (`go vet`) code.

In the same directory where you initialised the module,
delete `heygo.go` and replace it with a new file `heygoV2.go`:

```{code-block} go
:caption: `heygoV2.go`
package main;

import "fmt";

func main() {
fmt.Println(greeting);
}
```

This code contains a bug and is poorly formatted.
Let's fix those issues with the tooling provided
with a Go install.

### Go vet

Running `go vet hello.go` will output the following error:

```none
vet: ./hello.go:6:14: undefined: greeting
```

To fix the error define the `greeting` variable:

```{code-block} diff
:caption: `heygoV2.go`
package main

import "fmt";

+var greeting="Hey Go!"

func main() {
fmt.Println(greeting)
}
```

### Gofmt

Running `go -w fmt hello.go` will identify formatting
issues and write necessary changes to the file:

```{code-block} diff
:caption: `heygoV2.go`
package main

- import "fmt";
+ import "fmt"

var greeting="Hey Go!"

func main() {
-fmt.Println(greeting)
+	fmt.Println(greeting)
}
```

In this case, unneeded semicolons were removed
from the import line and the call to the print
method in the main function was indented correctly.

### Delve

[Delve](https://github.com/go-delve/delve) is a popular debugger for Go code.
There is Delve-support in editors like VSCode and GoLang.
In this guide Delve will be used as a command-line debugging tool.

You will need to have the Go toolchain set up to install Delve.
Delve can be installed by cloning the repo, changing to the cloned
directory and invoking `go instal`:

```none
git clone https://github.com/go-delve/delve
cd delve
go install github.com/go-delve/delve/cmd/dlv
```

Create a file to debug called `main.go` in a new folder where you have initialised a Go module.
This program is intended to calculate the average value from an array of integers.
However, there is a bug in the for-loop that needs to be investigated:

```{code-block} go
:caption: `main.go`
:linenos:
:emphasize-lines: 7,8,9
package main

import "fmt"

func calculateAverage(numbers []int) float64 {
	sum := 0
	for i := 0; i <= len(numbers); i++ {
		sum += numbers[i]
	}
	return float64(sum) / float64(len(numbers))
}

func main() {
	numbers := []int{10, 45, 30}
	average := calculateAverage(numbers)

	fmt.Printf("Average value of  is: %.2f\n", average)
}

```

To initiate a debugging session with Delve run `dlv debug` on the file:

```none
dlv debug main.go
```

This output will indicate that you are in an interactive debugging session.
You can interact with the debugger by entering commands after the `(dlv)` prompt:

```none
Type 'help' for list of commands.
(dlv)
```

To test the `calculateAverage` function set a break point at line 6:

```none
(dlv) break main.go:7
```

If the break point has been set successfully you will get the following message:

```none
Breakpoint 1 set at 0x49cee9 for main.calculateAverage() ./main.go:6
```

Next you can continue to the for-loop:

```none
(dlv) continue
```

Delve will show visually where you are in the code; in this case, at the start of the for-loop:

```none
> [Breakpoint 1] main.calculateAverage() ./main.go:7 (hits goroutine(1):1 total:1) (PC: 0x49cee9)
     2:	
     3:	import "fmt"
     4:	
     5:	func calculateAverage(numbers []int) float64 {
     6:		sum := 0
=>   7:		for i := 0; i <= len(numbers); i++ {
     8:			sum += numbers[i]
     9:		}
    10:		return float64(sum) / float64(len(numbers))
    11:	}
    12:	
```

The value of `sum` can be checked with the `print` command:

```none
(dlv) print sum
```

As expected, it has been initialised to `0`.

Now step through the for-loop with:

```none
(dlv) step
```

Again, your position in the code will be shown:

```none
> main.calculateAverage() ./main.go:8 (PC: 0x49cf09)
     3:	import "fmt"
     4:	
     5:	func calculateAverage(numbers []int) float64 {
     6:		sum := 0
     7:		for i := 0; i <= len(numbers); i++ {
=>   8:			sum += numbers[i]
     9:		}
    10:		return float64(sum) / float64(len(numbers))
    11:	}
    12:	
    13:	func main() {
```

```{note}
This output showing the code position is truncated for the remainder of this guide.
```

Checking the value of the index:

```none
(dlv) print i
```

This outputs `0`.
After another step you can confirm that the `sum` value has been incremented
with the first element in the `numbers` array:

```none
(dlv) step
...
...
(dlv) print sum
10
(dlv) print numbers
[]int len: 3, cap: 3, [10,45,30]
```

So far so good, the sum is equal to the first element of the list.

Let's step through the code a few more times until we find the bug:

```none
(dlv) step
...
...
(dlv) print i
1
(dlv) step
...
...
(dlv) print sum
55
(dlv) step
...
...
(dlv) print i
2
(dlv) step
...
...
(dlv) print sum
85
(dlv) step
...
...
(dlv) print i
3
(dlv) step

```

The last step causes a panic:

```none
> [unrecovered-panic] runtime.fatalpanic() /usr/local/go/src/runtime/panic.go:1217 (hits goroutine(1):1 total:1) (PC: 0x43a604)
Warning: debugging optimized function
	runtime.curg._panic.arg: interface {}(string) "runtime error: index out of range [3] with length 3"
```

The array has a length of 3 but the index is initialised at 0.
This means the loop will attempt to run four times on three values.
There is an off-by-one error.

Changing the code as follows will fix the error:

```{code-block} diff
func calculateAverage(numbers []int) float64 {
	sum := 0
-	for i := 0; i <= len(numbers); i++ {
+	for i := 0; i < len(numbers); i++ {
		sum += numbers[i]
	}
	return float64(sum) / float64(len(numbers))
}
```
