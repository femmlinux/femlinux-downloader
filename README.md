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

---

## 📥 Instalación / How to use (Linux)

La aplicación se ejecuta a través de su código fuente de forma universal para cualquier distribución de Linux. Sigue estos pasos para prepararla en tu sistema:

The application runs directly from its source code and is universal for any Linux distribution. Follow these steps to set it up on your system:

### 1. Cloná este repositorio / Clone this repository

git clone [https://github.com/femmlinux/femlinux-downloader.git](https://github.com/femmlinux/femlinux-downloader.git)
cd femlinux-downloader

### 2. Instalá las dependencias del sistema / Install system dependencies

Requiere ffmpeg para procesar multimedia y python3-tk (o tk) para la interfaz gráfica. / Requires ffmpeg for multimedia processing and python3-tk (or tk) for the GUI.

En Debian / Ubuntu:
sudo apt update
sudo apt install ffmpeg python3-tk python3-venv

En Arch Linux:
sudo pacman -S ffmpeg tk python

### 3. Instalá las librerías necesarias de Python / Install the required Python libraries

Para evitar conflictos con el sistema en distribuciones modernas (como Debian 12 o Arch), se recomienda instalar las dependencias de Python dentro de un entorno virtual (venv). / To avoid system conflicts on modern distributions, it is recommended to install Python dependencies inside a virtual environment (venv).

# Crear el entorno virtual / Create virtual environment
python3 -m venv entorno

# Activar el entorno / Activate the environment
source entorno/bin/activate

# Instalar los paquetes / Install packages
pip install yt-dlp tkinterdnd2

### 4. Iniciá la aplicación / Launch the application

Asegúrate de tener el entorno virtual activado antes de ejecutar el programa. / Make sure the virtual environment is activated before running the program.

python femlinux-downloader.py
