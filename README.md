# FemLinux Downloader

*(Scroll down for the English version)*

Un gestor automático de descargas de YouTube diseñado para recuperar tus propios archivos de forma rápida y sencilla. Permite extraer audio en formato MP3 o descargar el video completo en formato MP4, mapeando todas las resoluciones disponibles.

## ⚠️ Descargo de Responsabilidad (Disclaimer)

Esta aplicación fue creada como una herramienta de utilidad personal, orientada principalmente a que los creadores puedan descargar y recuperar sus propios videos en caso de haber perdido los archivos originales. 

**No me hago responsable por el uso que se le dé a esta aplicación.** La descarga de contenido de terceros sin autorización y su posterior distribución constituye una violación a los derechos de autor (copyright), una práctica con la cual no estoy de acuerdo ni fomento bajo ninguna circunstancia. El uso de este software para descargar material protegido corre bajo la exclusiva y total responsabilidad del usuario final.

---

# FemLinux Downloader (English)

An automatic YouTube download manager designed to recover your own files quickly and easily. It allows you to extract audio in MP3 format or download the full video in MP4 format, mapping all available resolutions.

## ⚠️ Disclaimer

This application was created as a personal utility tool, primarily intended to allow creators to download and recover their own videos in the event of losing the original files.

**I am not responsible for how this application is used.** Downloading unauthorized third-party content and its subsequent distribution constitutes a copyright violation, a practice I do not agree with nor encourage under any circumstances. The use of this software to download copyrighted material is the sole and strict responsibility of the end user.


Guía de Instalación / Installation Guide

(Scroll down for English)

A continuación, se detallan los pasos para instalar FemLinux Downloader v3.1 dependiendo de tu distribución de Linux. Todos los archivos necesarios se encuentran en la pestaña Releases de este repositorio.

🐧 Para Debian, Ubuntu, antiX y derivados (.deb)

Si utilizás un sistema basado en Debian, la forma más limpia de instalar la aplicación y sus dependencias es utilizando el paquete .deb.

1. Descargar el instalador:
Descargá el archivo llamado femlinux-downloader_3.1-1_amd64.deb desde la sección Releases.

2. Instalar desde la terminal:
Abrí una terminal en la carpeta donde descargaste el archivo (generalmente ~/Descargas) y ejecutá los siguientes comandos:
Bash

sudo apt update
sudo apt install ./femlinux-downloader_3.1-1_amd64.deb

(Nota: Usar apt install ./paquete.deb es recomendable porque resuelve e instala automáticamente dependencias como ffmpeg y python3-tk si te faltan).

3. Ejecutar:
¡Listo! Ya podés buscar "FemLinux Downloader" en el menú de aplicaciones de tu sistema o escribir femlinux-downloader en la terminal.

🦅 Para Arch Linux, Manjaro y derivados (.pkg.tar.zst)
Si utilizás Arch Linux, armamos un paquete nativo comprimido con zstd, compatible directamente con el gestor pacman.

1. Descargar el paquete:
Descargá el archivo llamado femlinux-downloader-3.1-2-x86_64.pkg.tar.zst desde la sección Releases.

2. Instalar con pacman:
Abrí la terminal en el directorio de descarga e instalá el paquete localmente ejecutando:
Bash

sudo pacman -U femlinux-downloader-3.1-2-x86_64.pkg.tar.zst

3. Ejecutar:
La aplicación ya está integrada en tu sistema. Buscala en el menú de tu entorno de escritorio o lanzala desde la terminal con femlinux-downloader.

🛠️ Método Universal (Binario Portable)
Si usás otra distribución (como Fedora, Void Linux, Puppy Linux, etc.) o simplemente no querés instalar nada en el sistema, podés usar el archivo binario independiente.

1. Descargar el ejecutable:
Descargá el archivo que se llama simplemente femlinux-downloader (pesa alrededor de 29 MB).

2. Dar permisos de ejecución:
Abrí la terminal donde descargaste el archivo y dale permisos para ejecutarse:
Bash

chmod +x femlinux-downloader

3. Requisitos previos:
Asegurate de tener instalados ffmpeg y tk (o python3-tk) usando el gestor de paquetes de tu distribución, ya que el motor de descarga los necesita para procesar el audio y el video.

4. Ejecutar:
Hacé doble clic sobre el archivo o ejecutalo desde la terminal con:
Bash

./femlinux-downloader

Installation Guide (English)

Below are the steps to install FemLinux Downloader v3.1 depending on your Linux distribution. All necessary files can be found in the Releases tab of this repository.

🐧 For Debian, Ubuntu, antiX, and derivatives (.deb)
If you use a Debian-based system, the cleanest way to install the application and its dependencies is by using the .deb package.

1. Download the installer:
Download the file named femlinux-downloader_3.1-1_amd64.deb from the Releases section.

2. Install from the terminal:
Open a terminal in the folder where you downloaded the file (usually ~/Downloads) and run the following commands:
Bash

sudo apt update
sudo apt install ./femlinux-downloader_3.1-1_amd64.deb

(Note: Using apt install ./package.deb is recommended because it automatically resolves and installs dependencies like ffmpeg and python3-tk if they are missing).

3. Run:
Done! You can now search for "FemLinux Downloader" in your system's application menu or launch it by typing femlinux-downloader in the terminal.

🦅 For Arch Linux, Manjaro, and derivatives (.pkg.tar.zst)
If you use Arch Linux, we have built a native zstd-compressed package that is directly compatible with the pacman package manager.

1. Download the package:
Download the file named femlinux-downloader-3.1-2-x86_64.pkg.tar.zst from the Releases section.

2. Install with pacman:
Open a terminal in the download directory and install the local package by running:
Bash

sudo pacman -U femlinux-downloader-3.1-2-x86_64.pkg.tar.zst

3. Run:
The application is now integrated into your system. Find it in your desktop environment's menu or launch it from the terminal with femlinux-downloader.

🛠️ Universal Method (Portable Binary)
If you use another distribution (like Fedora, Void Linux, Puppy Linux, etc.) or simply don't want to install anything on your system, you can use the standalone binary file.

1. Download the executable:
Download the file simply named femlinux-downloader (it weighs around 29 MB).

2. Grant execution permissions:
Open the terminal where you downloaded the file and make it executable:
Bash

chmod +x femlinux-downloader

3. Prerequisites:
Make sure you have ffmpeg and tk (or python3-tk) installed using your distribution's package manager, as the download engine requires them to process audio and video.

4. Run:
Double-click the file or run it from the terminal with:
Bash

./femlinux-downloader
