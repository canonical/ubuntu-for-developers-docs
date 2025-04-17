# Toolchain availability

## .NET

### Availability

| Ubuntu version              | `amd64` | `arm64` | `s390x` | `ppc64el` |
|-----------------------------|---------|---------|---------|-----------|
| 25.04 (Plucky Puffin)       | **8**, 9 | **8**, 9 | **8**, 9 | **8**, 9 |
| 24.10 (Oracular Oriole)     | **8**, 9 | **8**, 9 | **8**, 9 | **8**, 9 |
| 24.04 LTS (Noble Numbat)    | 6¹ ², 7¹ ², **8**, 9¹ | 6¹ ², 7¹ ², **8**, 9¹ | **8**, 9¹ | **8**, 9¹ |
| 22.04 LTS (Jammy Jellyfish) | **6**, 7, **8**, 9¹ | **6**, 7, **8**, 9¹ | **8**, 9¹ | **8**, 9¹ |


**bold** -- package is in main    
¹ -- available in the backports PPA only    
² -- version is no longer supported (End of Life)

### Packages

| Version      | Source package                                          | End of Life (Upstream) | 
|--------------|---------------------------------------------------------|------------------------|
| .NET 9 (STS) | [dotnet9](https://launchpad.net/ubuntu/+source/dotnet9) | 12 May 2026          |
| .NET 8 (LTS) | [dotnet8](https://launchpad.net/ubuntu/+source/dotnet8) | 10 November 2026     |
| .NET 7 (STS) | [dotnet7](https://launchpad.net/ubuntu/+source/dotnet7) | 14 May 2024          |
| .NET 6 (LTS) | [dotnet6](https://launchpad.net/ubuntu/+source/dotnet6) | 12 November 2024     |

## LLVM / Clang

### Availability

| Ubuntu version              | available LLVM/Clang versions |
|-----------------------------|-------------------------------|
| 25.04 (Plucky Puffin)       | 14, 15, 17, **18**, **19** (current default), **20** (planned default) |
| 24.10 (Oracular Oriole)     | 14, 15, 16, 17, **18**, **19** (default) |
| 24.04 LTS (Noble Numbat)    | 14, 15, 16, **17**, **18** (default), 19 |
| 22.04 LTS (Jammy Jellyfish) | 11, 12, **13**, **14** (default), **15** |
| 20.04 LTS (Focal Fossa)     | 6, 7, 8, **9**, **10** (default), **11**, **12**, 18 |
| 18.04 LTS (Bionic Beaver)   | 3.7, **3.9**, 4, 5, **6** (default), **7**, **8**, **9**, **10** |
| 16.04 LTS (Xenial Xerus)    | **3.6**, 3.7, **3.8** (default), 3.9, **4**, **5**, **6**, 8 |
| 14.04 LTS (Trusty Tahr)     | 3.3, **3.4** (default), 3.5, **3.6**, **3.8**, 3.9 |

**bold** -- package is in main    

### Packages

- [llvm-defaults](https://launchpad.net/ubuntu/+source/llvm-defaults) 
- [llvm-toolchain-20](https://launchpad.net/ubuntu/+source/llvm-toolchain-20) 
- [llvm-toolchain-19](https://launchpad.net/ubuntu/+source/llvm-toolchain-19) 
- [llvm-toolchain-18](https://launchpad.net/ubuntu/+source/llvm-toolchain-18) 
- [llvm-toolchain-17](https://launchpad.net/ubuntu/+source/llvm-toolchain-17) 
- [llvm-toolchain-16](https://launchpad.net/ubuntu/+source/llvm-toolchain-16) 
- [llvm-toolchain-15](https://launchpad.net/ubuntu/+source/llvm-toolchain-15) 
- [llvm-toolchain-14](https://launchpad.net/ubuntu/+source/llvm-toolchain-14) 
- [llvm-toolchain-13](https://launchpad.net/ubuntu/+source/llvm-toolchain-13) 
- [llvm-toolchain-12](https://launchpad.net/ubuntu/+source/llvm-toolchain-12) 
- [llvm-toolchain-11](https://launchpad.net/ubuntu/+source/llvm-toolchain-11) 
- [llvm-toolchain-10](https://launchpad.net/ubuntu/+source/llvm-toolchain-10) 
- [llvm-toolchain-9](https://launchpad.net/ubuntu/+source/llvm-toolchain-9) 
- [llvm-toolchain-8](https://launchpad.net/ubuntu/+source/llvm-toolchain-8) 
- [llvm-toolchain-7](https://launchpad.net/ubuntu/+source/llvm-toolchain-7) 
- [llvm-toolchain-6.0](https://launchpad.net/ubuntu/+source/llvm-toolchain-6.0) 
- [llvm-toolchain-5.0](https://launchpad.net/ubuntu/+source/llvm-toolchain-5.0) 
- [llvm-toolchain-4.0](https://launchpad.net/ubuntu/+source/llvm-toolchain-4.0)
- [llvm-toolchain-3.9](https://launchpad.net/ubuntu/+source/llvm-toolchain-3.9)
- [llvm-toolchain-3.8](https://launchpad.net/ubuntu/+source/llvm-toolchain-3.8)
- [llvm-toolchain-3.7](https://launchpad.net/ubuntu/+source/llvm-toolchain-3.7)
- [llvm-toolchain-3.6](https://launchpad.net/ubuntu/+source/llvm-toolchain-3.6)
- [llvm-toolchain-3.5](https://launchpad.net/ubuntu/+source/llvm-toolchain-3.5)
- [llvm-toolchain-3.4](https://launchpad.net/ubuntu/+source/llvm-toolchain-3.4)
- [llvm-toolchain-3.3](https://launchpad.net/ubuntu/+source/llvm-toolchain-3.3)
