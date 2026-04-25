---
myst:
  html_meta:
    description: "Build, run, and test Zig programs on Ubuntu using zig build and zig build-exe."
---

(use-zig)=
# Develop with Zig on Ubuntu

This tutorial shows how to create, build, run, and test a Zig program on Ubuntu. For instructions on how to install Zig and set up editor tooling, see the dedicated guide on {ref}`install-zig`. This article assumes that tooling suggested in that article has been installed.


## Creating a Zig project

1. Create a project directory and change into it:

    ```{terminal}
    :dir: ~
    :user: dev
    :host: ubuntu

    mkdir -p ~/zig/hello && cd ~/zig/hello
    ```

1. Initialize the project:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    zig init
    ```

   {command}`zig init` creates the following project structure:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    tree

    .
    ├── build.zig
    ├── build.zig.zon
    └── src
        ├── main.zig
        └── root.zig
    ```

   * {file}`build.zig` - the build script, written in Zig itself
   * {file}`build.zig.zon` - package manifest (name, version, dependencies)
   * {file}`src/main.zig` - the executable entry point
   * {file}`src/root.zig` - a library module stub

1. Inspect the generated {file}`src/main.zig`:

    ```{code-block} zig
    :caption: `src/main.zig`

    const std = @import("std");

    pub fn main() !void {
        std.debug.print("All your {s} are belong to us.\n", .{"codebase"});
    }
    ```

   :::{note}
   {command}`zig init` generates the {file}`main.zig` file with copious comments, as well as other logic, including example tests and an import of the `hello_lib` library that was also created; above is just the bare minimum needed for the example program.

   The project would still compile and run if you stripped all the extra code and only left what we're showing here.
   :::


## Building and running

1. Build and run the project using {command}`zig build run`:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    zig build run

    All your codebase are belong to us.
    ```

1. Replace the message in {file}`src/main.zig` with 'Hello, world!':

    ```{code-block} zig
    :caption: `src/main.zig`

    const std = @import("std");

    pub fn main() !void {
        std.debug.print("Hello, world!\n", .{});
    }
    ```

1. Build and run again:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    zig build run

    Hello, world!
    ```


## Compiling a single file

Use {command}`zig build-exe` to compile a single source file without a project structure.

1. Create a standalone source file:

    ```{code-block} zig
    :caption: `hello.zig`

    const std = @import("std");

    pub fn main() !void {
        std.debug.print("Hello, world!\n", .{});
    }
    ```

1. Compile it:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    zig build-exe hello.zig
    ```

   This produces an executable named {file}`hello` in the current directory.

1. Run the executable:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    ./hello

    Hello, world!
    ```


## Testing Zig code

Zig has a built-in test runner. Test blocks are declared with the `test` keyword and use the `std.testing` namespace for assertions.

The generated {file}`src/root.zig` already contains an example test.

1. Review the {file}`src/root.zig` example test:

    ```{code-block} zig
    :caption: `src/root.zig`

    const std = @import("std");
    const testing = std.testing;

    pub export fn add(a: i32, b: i32) i32 {
        return a + b;
    }

    test "basic add functionality" {
        try testing.expect(add(3, 7) == 10);
    }
    ```

1. Run the test:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    zig build --summary all test
    ```

    :::{raw} html
    <div class="highlight-default notranslate"><div class="highlight"><pre><span style="color:#18b2b2;">Build Summary:</span><span style="color:#b2b2b2;"> 5/5 steps succeeded; 1/1 tests passed</span><span style="color:#b2b2b2;">
    </span><span style="color:#b2b2b2;">test</span><span style="color:#18b218;"> success</span><span style="color:#b2b2b2;">
    </span><span style="color:#b2b2b2;">├─ run test</span><span style="color:#18b218;"> 1 passed</span><span style="color:#656565;"> 635us MaxRSS:1M</span><span style="color:#b2b2b2;">
    </span><span style="color:#b2b2b2;">│ &#160;└─ zig test Debug native</span><span style="color:#18b218;"> success</span><span style="color:#656565;"> 1s MaxRSS:260M</span><span style="color:#b2b2b2;">
    </span><span style="color:#b2b2b2;">└─ run test</span><span style="color:#18b218;"> success</span><span style="color:#656565;"> 191us MaxRSS:1M</span><span style="color:#b2b2b2;">
    </span><span style="color:#b2b2b2;"> &#160;&#160;└─ zig test Debug native</span><span style="color:#18b218;"> success</span><span style="color:#656565;"> 1s MaxRSS:261M</span></pre></div></div>
    :::


### Testing STDOUT output

To test the actual "Hello, world!" function of the program, you can use a special feature of Zig: duck-typing at compile time. In this example, we create a `hello()` function that accepts any object that provides a `.print()` method.

This separates the output destination of the function from its logic, which makes it testable. In this way, the function can write to STDOUT, and the test is able to capture the output by directing it somewhere else where it can check it.

Modify the {file}`src/main.zig` file:

```{code-block} zig
:caption: `src/main.zig`

const std = @import("std");

// Duck-typing the 'writer' parameter
pub fn hello(writer: anytype) !void {
    try writer.print("Hello, world!\n", .{});
}

// Sending output to STDOUT
pub fn main() !void {
    try hello(std.io.getStdOut().writer());
}

// Sending output to an array
test "hello writes 'Hello, world!' to stdout" {
    var output = std.ArrayList(u8).init(std.testing.allocator);
    defer output.deinit();
    try hello(output.writer());
    try std.testing.expectEqualStrings("Hello, world!\n", output.items);
}
```

:::{note}
`defer` ensures that `output.deinit()` (which frees the allocated memory) is called automatically when the test ends (regardless of whether the function succeeds or not).
:::


## Cross-compiling with `zig cc`

Zig includes a built-in C (Clang LLVM) compiler, `zig cc`, which works as a drop-in replacement for C compilers with first-class cross-compilation support. No separate cross-toolchain installation is required.


### Compiling C code natively

1. Create a C source file:

    ```{code-block} c
    :caption: `hello.c`

    #include <stdio.h>

    int main(void) {
        printf("Hello, world!\n");
        return 0;
    }
    ```

1. Compile and run:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    zig cc hello.c -o hello && ./hello

    Hello, world!
    ```


### Compiling for other architectures

The `zig cc` command compiles for any supported target without additional toolchain packages.

1. Cross-compile for 64-bit ARM Linux (statically linked against the [musl](https://musl.libc.org/) libc implementation):

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    zig cc hello.c -target aarch64-linux-musl -o hello-arm64
    ```

1. Verify the binary targets ARM64:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    file hello-arm64

    hello-arm64: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV),
                 statically linked, not stripped
    ```

1. Install QEMU user-mode emulation. Ubuntu's `qemu-user-binfmt` package registers `binfmt_misc` handlers automatically, so foreign-architecture binaries run transparently:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    sudo apt install qemu-user-binfmt
    ```

   Ubuntu's {pkg}`qemu-user-binfmt` package registers `binfmt_misc` handlers automatically, so foreign-architecture binaries run transparently.

1. Run the Aarch64 executable:

    ```{terminal}
    :dir: ~/zig/hello
    :user: dev
    :host: ubuntu

    ./hello-arm64

    Hello, world!
    ```

:::{note}
Similarly, cross-compile for 64-bit Windows and run with [Wine](https://www.winehq.org/):

```{terminal}
:dir: ~/zig/hello
:user: dev
:host: ubuntu

zig cc hello.c -target x86_64-windows-gnu -o hello.exe
```

```{terminal}
:dir: ~/zig/hello
:user: dev
:host: ubuntu

sudo apt install wine
```

```{terminal}
:dir: ~/zig/hello
:user: dev
:host: ubuntu

wine hello.exe

Hello, world!
```
:::
