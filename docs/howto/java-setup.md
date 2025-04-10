# How to set up development environment for Java on Ubuntu

Java is a popular programming language supported on many platforms. This article provides guidance on how to install the Java toolchain and development environment on Ubuntu.


## Installing Eclipse IDE

The quickest way to start developing Java code on Ubuntu is to install Eclipse IDE -- the {spellexception}`de facto` standard integrated development environment for Java development. This also provides the latest Java LTS (long-term support) version:

```none
snap install eclipse --classic
```

Run {command}`eclipse` to start the IDE.


(installing-java-development-kit)=
## Installing Java Development Kit

To install the default Java Development Kit for your Ubuntu release, run:

```none
sudo apt install default-jdk
```

### Short Term Support Java releases

Latest or early access releases are available in the latest development release of Ubuntu. For example, to install the early access Ubuntu archive version of OpenJDK 24, use:

```none
sudo apt install openjdk-24-jdk
```

Latest or early-access releases are also available through the community maintained [OpenJDK](https://snapcraft.io/openjdk) snap package.

- To install the latest early-access release, run:

   ```none
   sudo snap install openjdk --channel=edge
   ```

- To install the latest release, run:

   ```none
   sudo snap install openjdk --channel=stable
   ```


### Long Term Support Java releases

The Ubuntu Archive provides packages for all supported LTS releases of [OpenJDK](https://openjdk.org/) - an open-source implementation of [Java Platform, Standard Edition](https://www.oracle.com/technetwork/java/javase/overview/index.html). OpenJDK 17 and 21 TCK (Technology Compatibility Kit) is certified on Ubuntu 24.04.

To install OpenJDK, run:

```none
sudo apt install openjdk-<version>-jdk
```

For example, to install the latest LTS release, use:

```none
sudo apt install openjdk-21-jdk
```


## Java IDEs

A number of IDEs are available for Java development on Ubuntu:

[Eclipse](https://www.eclipse.org/)
: ```none
  sudo snap install eclipse --classic
  ```

[IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/)
: ```none
  sudo snap install intellij-idea-community --classic
  ```

[Visual Studio Code](https://code.visualstudio.com/) with [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)
: ```none
  sudo snap install code --classic
  ```

[Android Studio](https://developer.android.com/studio)
: ```none
  sudo snap install android-studio --classic
  ```
