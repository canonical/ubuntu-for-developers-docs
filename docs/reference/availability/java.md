(java-toolchain-availability)=
# Available Java versions

## Ubuntu OpenJDK (deb) packages

| Ubuntu version | available Java versions | {lpsrc}`java-common` version |
| --- | --- | --- |
| 25.10 (Questing Quokka)     | 8, 11, 17, **21**, 24, 25 | 21 |
| 25.04 (Plucky Puffin)       | 8, 11, 17, **21**, 24, 25 | 21 |
| 24.10 (Oracular Oriole)     | 8, 11, 17, **21**, 22, 23, 24 | 21 |
| 24.04 LTS (Noble Numbat)    | 8, 11, **17**, **21** | 21 |
| 22.04 LTS (Jammy Jellyfish) | 8, **11**, 17, 18, 19, 21 | 11 |
| 20.04 LTS (Focal Fossa)     | 8, **11**, 13, 16, 17, 21 | 11 |
| 18.04 LTS (Bionic Beaver)   | 8, **11**, 17 | 11 |
| 16.04 LTS (Xenial Xerus)    | **8**, 9 | 8 |
| 14.04 LTS (Trusty Tahr)     | 6, **7** | 7 |

<!-- Do not forget to add 4 spaces at the end of line to keep future diffs more readable -->
**bold** -- package is in main    

| Java Version | Source package | 
| --- | --- |
| 25 | {lpsrc}`openjdk-25` |
| 24 | {lpsrc}`openjdk-24` |
| 23 | {lpsrc}`openjdk-23` |
| 22 | {lpsrc}`openjdk-22` |
| 21 | {lpsrc}`openjdk-21` |
| 19 | {lpsrc}`openjdk-19` |
| 18 | {lpsrc}`openjdk-18` |
| 17 | {lpsrc}`openjdk-17` |
| 16 | {lpsrc}`openjdk-16` |
| 13 | {lpsrc}`openjdk-13` |
| 11 | {lpsrc}`openjdk-lts` |
| 9 | {lpsrc}`openjdk-9` |
| 8 | {lpsrc}`openjdk-8` |
| 7 | {lpsrc}`openjdk-7` |
| 6 | {lpsrc}`openjdk-6` |

## Ubuntu OpenJDK: {abbr}`CRaC (Coordinated Restore at Checkpoint)` (deb) packages

| Ubuntu version | available Java versions |
| --- | --- |
| 25.10 (Questing Quokka) | 17, 21 |
| 25.04 (Plucky Puffin)   | 17, 21 |
| 24.10 (Oracular Oriole) | 17, 21 |

| Java Version | Source package | 
| --- | --- |
| 21 | {lpsrc}`openjdk-21-crac` |
| 17 | {lpsrc}`openjdk-17-crac` |


## GraalVM snap

The [`graalvm-jdk` snap](https://snapcraft.io/graalvm-jdk) provides an advanced JDK with ahead-of-time Native Image compilation.

| Java Version | Snap Channel |
| --- | --- |
| 25 | latest/stable |
| 24 | latest/edge |
| 21 | v21/stable |
