# Introduction to the .NET toolchain

The .NET platform (pronounced "dot net") is a fast, lightweight, and modular framework, enabling the creation of cross-platform applications that work on GNU/Linux, macOS, and Windows.

It particularly focuses on creating console applications, web applications, and micro-services.

```{note}
Do **NOT** confuse *.NET Framework* with *.NET (Core)*

See the {ref}`dotnet-history` section for more details.
```

## Programming languages

The .NET platform supports multiple programming languages, the primary ones are:

- [**C#**](https://learn.microsoft.com/en-us/dotnet/csharp/) (pronounced "C sharp") most popular .NET language – simple, modern, object-oriented, and type-safe
- [**F#**](https://learn.microsoft.com/en-us/dotnet/fsharp/) (pronounced "F sharp") functional, imperative, and type-safe
- [**Visual Basic**](https://learn.microsoft.com/en-us/dotnet/visual-basic/) (abbreviated "VB") oldest .NET language; straightforward and approachable language with a stable design

```{note}
We recommend not to use Visual Basic for new projects. It is mostly used by legacy projects nowadays. While Microsoft is committed to maintaining it for the foreseeable future, the .NET team focuses on supporting existing scenarios. It's unlikely that support for new workloads or runtime features will be added.
```
 
## Architecture

The .NET platform contains a runtime, a set of framework libraries, an SDK containing compilers and developer tools, and a `dotnet` CLI application to drive everything.

```{figure} /images/Overview_of_the_Common_Language_Infrastructure_2015.png
   :height: 30em
   :alt: diagram of the .NET components and how they interact

   Diagram of the Common Language Infrastructure

   Credit: {spellexception}`Deviousasti` (License: CC BY-SA 4.0 Deed)
```

### Software Development Kit (SDK)

A collection of tools, including compilers, libraries, and templates, that enable developers to build and develop .NET applications and libraries.

### Common Intermediate Language (CIL)

A low-level, platform-agnostic language into which .NET languages are compiled. This gets translated into native machine code by the Just-In-Time (JIT) compiler of the runtime.

### Common Language Runtime (CLR)

The execution environment of .NET that manages memory, handles garbage collection, enforces security, and converts CIL into native code. It enables cross-language interoperability.

### Host / Command Line Interface (CLI)

The .NET host (the `dotnet` command) contains the logic to resolve and select the right version of the .NET SDK or runtime to use. This has the advantage that you can use one command to interact with multiple versions of .NET.


## NuGet Package Manager

```{figure} /images/NuGet_project_logo.svg.png
   :height: 4em
   :alt: Logo of NuGet
   :align: left

   Logo of NuGet
```

The primary mechanism for sharing code, assets, and libraries in the .NET toolchain are NuGet packages. A NuGet package is a single ZIP file with the `.nupkg` file extension that contains compiled code ({spellexception}`DLLs`), other files related to that code, and a descriptive manifest that includes information like the package version number.

NuGet is also the name of the the package manager for .NET. The NuGet client tools provide the ability to produce and consume packages.

The [NuGet Gallery](https://www.nuget.org/) is the central package repository used by almost all package authors and consumers.

Learn more about NuGet [here](https://learn.microsoft.com/en-us/nuget/what-is-nuget).

## Release cycle & support policies

A major new release of .NET is published every November, alternating between a long-term support (LTS) release and a standard-term support (STS) release:

- **LTS releases**: Get free support and patches for three years by the .NET team. These releases usually have an even major version number and are released in an odd-numbered year.
- **STS releases:** Get free support and patches for 18 months by the .NET team. These releases usually have an odd major version number and and are released in an even-numbered year.

The quality of all releases is the same. The only difference is the length of support provided by upstream.

Patch updates are released monthly on the second Tuesday of each month, also known as Patch Tuesday. Within a release's support life-cycle, systems must remain current on released patch updates. Patches to releases are compatible, which eliminates the risk of adversely affecting applications.

```{figure} /images/dotnet-release-schedule.svg
   :alt: release & support timeline of .NET 7, 8, 9, 10, and 11 that visualizes the release cycle and (upstream) support policy

   .NET release and (upstream) support schedule
```

See the [support policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) of the .NET team for more information.

### .NET SDK feature bands

To learn about feature bands, see the .NET documentation: [Feature bands (SDK only)](
https://learn.microsoft.com/en-us/dotnet/core/releases-and-support#feature-bands-sdk-only).

Canonical only builds the x.x.1xx feature band for Ubuntu. Higher feature bands are usually short lived, less stable, and are more complex to build from source.

<!-- The Microsoft .NET team is working on reducing complexity for building these feature bands from source and Canonical may provide higher feature bands in the future via a PPA. -->

(dotnet-history)=
## .NET implementations and history

In the .NET community, you may encounter the terms ".NET Framework", ".NET Core", ".NET", or "Mono". These terms have different meanings and carry a vastly different context.

### .NET Framework

**.NET Framework** refers to the original .NET implementation by Microsoft. It is a proprietary, closed-source, and Windows-only implementation. The development started in the late 1990s with its first release in early 2000s. Microsoft still maintains .NET Framework due to the many still actively used business applications but no longer develops new features.

### The Mono Project

The [**Mono Project**](https://www.mono-project.com/) is an open-source implementation of Microsoft's .NET Framework and based on the .NET ECMA standards. It started development in the early 2000s. The Mono Project has been ported to many platforms, which enabled developers to run their .NET Framework applications cross-platform. It was the first .NET implementation on Android, iOS, Linux, and other operating systems.

Microsoft became the steward of the Mono Project when it acquired Xamarin in 2016. Microsoft maintains a modern fork of the Mono runtime in the [dotnet/runtime GitHub repository](https://github.com/dotnet/runtime/tree/main/src/mono) and has been progressively moving workloads to that fork. That work is now complete, and it is recommended that active Mono users and maintainers of Mono-based application frameworks migrate to .NET, which includes work from this fork.

The Mono Project has announced that the WineHQ organization has taken over as the stewards of the Mono Project upstream at the [mono/mono WineHQ GitLab repository](https://gitlab.winehq.org/mono/mono).

Similar to the .NET Framework, the Mono project is maintained but no longer receives new feature development.

### .NET (Core)

At the end of 2014, Microsoft announced **.NET Core**, an open-source, cross-platform successor to the .NET Framework. Alongside this, Microsoft adopted an open-source development model under the stewardship of the .NET Foundation.

In November 2020, Microsoft released .NET 5.0, discontinuing the "Core" branding. The version number 4.0 was deliberately skipped to prevent confusion with .NET Framework, whose major releases had consistently followed the 4.x versioning pattern since 2010.

The table below illustrates the transition timeline and the versioning conflict between .NET Framework and .NET (Core):

```{list-table}
   :header-rows: 1
* - Year
  - .NET Framework
  - .NET (Core)
* - 2002 
  - .NET Framework **1.0**
  -  
* - 2003 
  - .NET Framework **1.1**
  -  
* - 2006 
  - .NET Framework **2.0**, **3.0**
  -  
* - 2007 
  - .NET Framework 3.5
  -  
* - 2010 
  - .NET Framework 4
  -  
* - 2012 
  - .NET Framework 4.5
  -  
* - 2014 
  - .NET Framework 4.5.1, 4.5.2
  - .NET Core First Announcement
* - 2015 
  - .NET Framework 4.6 & 4.6.1
  -  
* - 2016 
  - .NET Framework 4.6.2
  - .NET Core **1.0**, **1.1**
* - 2017 
  - .NET Framework 4.7, 4.7.1
  - .NET Core **2.0**
* - 2018 
  - .NET Framework 4.7.2
  - .NET Core 2.1, 2.2
* - 2019
  - .NET Framework 4.8
  - .NET Core **3.0**, 3.1
* - 2020 
  -  
  - .NET 5
* - 2021
  -  
  - .NET 6
* - 2022
  - .NET Framework 4.8.1
  - .NET 7
* - 2023
  -  
  - .NET 8
```

See more .NET release information on [{spellexception}`versionsof.net`](https://versionsof.net/).
