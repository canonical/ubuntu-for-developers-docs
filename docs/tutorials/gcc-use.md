(use-gcc)=
# Develop with GCC on Ubuntu

This tutorial shows how to build and debug C programs on Ubuntu using GCC and GDB. For instructions on installing GCC and related tooling (including IDEs, debuggers, and the build system), see the dedicated guide on {ref}`install-gcc`. This article assumes that the tooling suggested in that article has been installed.

The GNU Compiler Collection (GCC) provides support for several programming languages. Working with the GCC toolchain in Ubuntu is straightforward, so this tutorial is limited to showing a basic 'Hello, world!' program in the C language and an introductory debugging session.


(writing-a-sample-c-program)=
## Writing a sample C program

1. Create a project directory:

    ```none
    mkdir -p ~/c-projects/hello-world
    cd ~/c-projects/hello-world
    ```

2. Write a 'Hello, world!' program that includes setting a variable. Create a {file}`hello.c` file with the following content:

    ```{code-block} c
    :caption: `hello.c`

    #include <stdio.h>

    int main() {
        int number = 42;
        printf("Hello, world!\nThe answer to everything is %d.\n", number);
        return 0;
    }
    ```

3. Build the source code using the {command}`gcc` compiler, specifying {file}`hello` as the file name of the resulting executable:

    ```none
    gcc hello.c -o hello
    ```

    This command incorporates the intermediate steps of preprocessing, compiling, and linking to generate an executable in one go. Use the `-v` option to display detailed information on how {command}`gcc` invokes the individual tools that handle the intermediate steps.

    :::{note}
    {command}`gcc` can compile source code in many programming languages, including C, C++, and Assembly. The compiler guesses the language based on the file extension (for example, `.c`, `.cpp`, or `.s`). You can explicitly specify the language using the `-x` option as well.
    :::

4. Run the program executable:

    ```{terminal}
    :dir: ~/projects/hello-world
    :user: dev
    :host: ubuntu
    :input: ./hello

    Hello, world!
    The answer to everything is 42.
    ```


## Fixing simple bugs

The {command}`gcc` compiler provides helpful output when encountering a problematic part of the source code.

1. Modify the 'Hello, world!' program source to omit an expected argument. Note the missing `number` argument on line 5:

    ```{code-block} c
    :caption: `hello.c`
    :linenos:

    #include <stdio.h>

    int main() {
        int number = 42;
        printf("Hello, world!\nThe answer to everything is %d.\n");
        return 0;
    }
    ```

2. Build the source:

    :::{raw} html
    <div class="highlight-default notranslate"><div class="highlight"><pre>$ gcc hello.c -o hello
    <span style="font-weight:bold;">hello.c:</span> In function ‘<span style="font-weight:bold;">main</span>’:
    <span style="font-weight:bold;">hello.c:5:57:</span> <span style="font-weight:bold;color:purple;">warning: </span>format ‘<span style="font-weight:bold;">%d</span>’ expects a matching ‘<span style="font-weight:bold;">int</span>’ argument [<span style="font-weight:bold;color:purple;">-Wformat=</span>]
        5 |     printf(&quot;Hello, world!\nThe answer to everything is <span style="font-weight:bold;color:purple;">%d</span>.\n&quot;);
          |                                                        <span style="font-weight:bold;color:purple;">~^</span>
          |                                                         <span style="font-weight:bold;color:purple;">|</span>
          |                                                         <span style="font-weight:bold;color:purple;">int</span></pre></div></div>
    :::

    {command}`gcc` displays a warning, but still compiles the source code.

3. Run the program to see how it behaves without the integer argument specified:

    ```{terminal}
    :dir: ~/projects/hello-world
    :user: dev
    :host: ubuntu
    :input: ./hello

    Hello, world!
    The answer to everything is -1350680728.
    ```


## Using the Make build system

Compiling manually by invoking {command}`gcc` directly can be useful to understand the build process or for simple projects like 'Hello, world!'. For larger projects, use a build system to simplify and automate the process.

See below for a simple example of the use of the GNU Make build system to build the 'Hello, world!' program from {ref}`writing-a-sample-c-program`.


1. Create a basic Makefile (a file named {file}`Makefile` in the project directory) with the following content:

    ```makefile
    ## Variables:

    # Compiler
    CC = gcc

    # Target executable
    TARGET = hello

    # Source files
    SRCS = hello.c

    # Object files
    OBJS = $(SRCS:.c=.o)

    ## Targets:

    # Default target
    all: $(TARGET)

    # Linking
    $(TARGET): $(OBJS)
    	$(CC) -o $@ $^

    # Compiling
    %.o: %.c
    	$(CC) -c $< -o $@

    # Cleaning
    clean:
    	rm -f $(OBJS) $(TARGET)

    .PHONY: all clean
    ```

    Note that the {file}`Makefile` divides the build process into separate compilation and linking steps. It also makes use of "automatic variables" that allow for writing the compilation rules without specifying absolute file names. For an overview, see [Automatic Variables](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html) in the GNU Make manual.

    :::{important}
    Makefile rules must start with the tab character. See [Rule Syntax](https://www.gnu.org/software/make/manual/html_node/Rule-Syntax.html).
    :::

2. Compile the program using {command}`make`:

    ```{terminal}
    :dir: ~/projects/hello-world
    :user: dev
    :host: ubuntu
    :input: make

    gcc -c hello.c -o hello.o
    gcc -o hello hello.o
    ```

    Checking the resulting files would show:

    ```{terminal}
    :dir: ~/projects/hello-world
    :user: dev
    :host: ubuntu
    :input: ls -1

    hello
    hello.c
    hello.o
    Makefile
    ```

4. Run the program executable:

    ```{terminal}
    :dir: ~/projects/hello-world
    :user: dev
    :host: ubuntu
    :input: ./hello

    Hello, world!
    The answer to everything is 42.
    ```


## Debugging with GDB

GDB is the standard debugger accompanying GNU GCC. While you can use debugging capabilities of your preferred IDE, GDB offers adequate debugging support for the command line.

See the example below for a quick introduction to GDB use with the 'Hello, world!' program from {ref}`writing-a-sample-c-program`.

1. Recompile the program with the `-g` option, which produces debugging information specifically for GDB:

    ```none
    gcc -g hello.c -o hello
    ```

2. Run the debugger:

    ```{code-block} bash
    :linenos:

    $ gdb hello

    #[snip]

    Reading symbols from hello...
    (gdb) start
    Temporary breakpoint 1 at 0x1155: file hello.c, line 4.
    Starting program: /home/rkratky/c-projects/hello-world/hello 

    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

    Temporary breakpoint 1, main () at hello.c:4
    4     int number = 42;
    (gdb) print number
    $1 = 32767
    (gdb) next
    5     printf("Hello, world!\nThe answer to everything is %d.\n", number);
    (gdb) print number
    $2 = 42
    (gdb)
    ```

    In the above example:

    1. Line 6: the {command}`hello` program is started.
    2. Line 15: the `number` variable is queried before being assigned.
    3. Line 17: the program execution is stepped forward.
    4. Line 19: the `number` variable is queried again after being assigned.

3. Press {kbd}`Ctrl+X+A` to switch to the text user interface (TUI) of GDB for a more interactive experience:

    ::::{include} /reuse/tutorials/gcc-use/gdb.md
    ::::

    Type `help` at any point to see available commands.

4. Press {kbd}`Ctrl+D` to quit the debugging session.
