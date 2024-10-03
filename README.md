# Create a drawing of a feed-forward neural network.

This is a simple Python script to generate pictures of a feed-forward neural network using Python and Graphviz. This is heavily inspired by Thiago G. Martins [How to draw neural network diagrams using Graphviz](https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/).

improvement by Plain

# Requiremnet

your system should have `make` and `graphviz`

if you use windows system you can use `choco` command to install these 2 package:

```powershell
choco install graphviz
choco install make
```

if you don't have `choco` you can use following command to install in administrator powershell

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

more details about the Chocolatey in here:

https://github.com/chocolatey/choco

# Usage

just type `make` and then it will generate the network.dot and according to the network.dot to generate the network.png.

`make clean` will delete these 2 files

the configure of the dot network should change in the code.

# Next step

try to improve the usage

try to contract the repository author tell him the improve

