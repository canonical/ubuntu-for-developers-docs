# How to set up development environment for Java™ on Ubuntu

Java™ is a popular programming language supported on many platforms. This article provides guidance on how to install Java™ toolchain and development environment on Ubuntu.

## Eclipse

The quickest way to start developing Java™ code on Ubuntu is to install Eclipse. This will provide a latest Java™ LTS and an IDE.

```
snap install eclipse --classic
```

 Run ``eclipse`` to start it.

## Long Term Support Java™ Releases

Ubuntu Archive provides packages for all supported LTS releases of [OpenJDK](https://openjdk.org/) - an open-source implementation of [Java Platform, Standard Edition](https://www.oracle.com/technetwork/java/javase/overview/index.html).
OpenJDK 17 and 21 TCK certified in Ubuntu 24.04.

Run ``apt install openjdk-<version>-jdk`` to install OpenJDK.

For example ``apt install openjdk-21-jdk`` will install OpenJDK 21.

## Short Term Support Java™ Releases

Latest or early access releases are available in the latest development release of Ubuntu.
For instance `apt install openjdk-24-jdk` will install the early access Ubuntu archive version of OpenJDK 24.

Latest or early access releases are also available through the community maintained [openjdk](https://snapcraft.io/openjdk) snap.

Run `snap install openjdk --channel=edge` to install the latest early access release.
Run `snap install openjdk --channel=stable` to install the latest release.

## Java Development IDEs

A number of IDEs are available for the Java development on Ubuntu:
- [Eclipse](https://www.eclipse.org/): `snap install eclipse --classic`
- [IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/) `snap install intellij-idea-community --classic`
- [Visual Studio Code](https://code.visualstudio.com/): `snap install code --classic` with [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack).
- [Android Studio](https://developer.android.com/studio): `snap install android-studio --classic`
