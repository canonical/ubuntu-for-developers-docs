(use-clang)=
# Develop C and C++ with Clang on Ubuntu

This tutorial provides basic guidance on developing C and C++ projects using Clang on Ubuntu. It demonstrates a classic 'Hello, world!' program as well as tips for building more complex projects using a build system like CMake.

## Clang vs build systems

Clang itself is a compiler, but building complex C and C++ projects typically requires more sophisticated steps to cache builds, track file dependencies, handle data files, and more. Rather than doing that manually, most developers use a build system that knows how to invoke Clang to handle those additional steps.

Popular build system choices for C and C++ include these, all of which can be configured to use Clang:
- **CMake** - Cross-platform build generator, most popular for modern C/C++ (`sudo apt install cmake`)
- **Meson** - Fast, user-friendly build system (`sudo apt install meson ninja-build`)
- **Make** - Traditional build automation (`sudo apt install make`)
- **{spellexception}`Autotools`** - Traditional GNU build system for legacy projects (`sudo apt install autoconf automake libtool`)

This tutorial shows how to use Clang directly, as well as a simple CMake project.

### Prerequisites

- Clang itself: refer to {ref}`install-clang`.
- CMake: `sudo apt install cmake`
- Any text editor or IDE

### Creating your source file

1. Create a project directory:

   ```none
   mkdir hello-world && cd hello-world
   ```

1. Create a source directory within your project:

   ```none
   mkdir src
   ```

1. Create a new source file using your preferred editor or IDE. For this example, we'll be using C++, so name your file `hello.cpp` and add the following contents:

   ```{code-block} cpp
   :caption: `hello-world/src/hello.cpp`
   #include <iostream>

   int main() {
       std::cout << "Hello, world!\n";
   }
   ```

:::
### Building with Clang directly
:::

With clang installed, you can build your hello world program easily. From within the `hello-world` directory you created, run:

```bash
clang -o hello src/hello.cpp
```

And now you should be able to run your program!

```bash
./hello
```

:::
### Building with CMake
:::

Suppose you plan to grow your `hello-world` project into something significant. You can use CMake right from the start to orchestrate your builds.

Start by creating a file named `CMakeLists.txt` inside the `hello-world` directory. Add the following contents:

```{code-block} cpp
:caption: `hello-world/CMakeLists.txt`
cmake_minimum_required(VERSION 3.10)
project(hello-world LANGUAGES CXX)

add_executable(hello
    src/hello.cpp
)
```

There are three commands we're using in this definition. The first sets a minimum version of CMake that your project is compatible with. Using version 3.10 is a reasonable starting point, because it's sufficiently modern to have newer CMake features, but not so modern that developers you work with won't have access to it. You may need to adjust this as you choose to use particular features.

The next line defines your project name, and you can optionally specify some other helpful information. In this case we tell CMake that the implementation language is C++, so it will not bother checking for any tooling related to C.

Finally, we define an executable output of our project by calling `add_executable`. The first argument is the name of the executable we want to produce. Following that is a list of the source files that need to be compiled to create it.

We're just about ready to run the build, but notice that we have not yet mentioned Clang anywhere. By default, the order that CMake uses when searching for compilers will result in GCC being detected first. Since we want to use clang, we can specify that directly when we configure the build.

CMake is a two-stage build system, where the first stage generates lower-level build files (by default, GNU {spellexception}`makefiles` on Ubuntu), and the second executes those. During the first stage is when we can specify extra configuration options for the build. To tell CMake to use Clang, do the following.

```bash
cmake -DCMAKE_CXX_COMPILER=clang++ -B build
```

In the output, you should be able to spot a line that shows which compiler CMake found, something like this:

```none
-- The CXX compiler identification is Clang 18.1.3
```

This places the build files in the {file}`build/` directory, nicely isolated from your project files. Now execute the actual build with another {command}`cmake` command:

```none
cmake --build build
```

You should now have your {file}`hello` executable, and can run it directly:

```none
./build/hello
```
