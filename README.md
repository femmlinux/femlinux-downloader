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

## 📥 Instalación / Cómo usar (Linux)  Installation / How to use (Linux)

The application runs directly from its source code and is universal for any Linux distribution. Follow these steps to set it up on your system:

La aplicación se ejecuta a través de su código fuente de forma universal para cualquier distribución de Linux. Sigue estos pasos para prepararla en tu sistema:

1. **Cloná este repositorio / Clone this repository:**

git clone [https://github.com/femmlinux/femlinux-downloader.git](https://github.com/femmlinux/femlinux-downloader.git)
cd femlinux-downloader

2. **Instalá las dependencias del sistema (requiere ffmpeg y herramientas gráficas)/Install system dependencies (ffmpeg and GUI toolkit are required)**
   
  En Debian / Ubuntu / antiX:
  sudo apt install ffmpeg python3-tk

  En Arch Linux: 
  sudo pacman -S ffmpeg tk
  
3. **Instalá las librerías necesarias de Python / Install the required Python libraries**

  pip install yt-dlp tkinterdnd2

4. **Iniciá la aplicación / Launch the application**

  python femlinux-downloader.py

  








