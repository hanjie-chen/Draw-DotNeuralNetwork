# Create a drawing of a feed-forward neural network.

This is a simple Python script to generate pictures of a feed-forward neural network using Python and Graphviz. This is heavily inspired by Thiago G. Martins [How to draw neural network diagrams using Graphviz](https://tgmstat.wordpress.com/2013/06/12/draw-neural-network-diagrams-graphviz/).

improvement by Plain

# Requiremnets

your system should have `make` and `graphviz` installed

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

```powershell
make               		: Use default layers [3, 5, 4, 2]"
make layers=[5,3,2,1] 	: Specify custom layers"
```

`make clean` will delete .dot and .png file



