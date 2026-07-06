# FemLinux Downloader

*(Scroll down for the English version)*

Un gestor automático de descargas de YouTube diseñado para recuperar tus propios archivos de forma rápida y sencilla. Permite extraer audio en formato MP3 o descargar el video completo en formato MP4, mapeando todas las resoluciones disponibles mediante una interfaz gráfica intuitiva.

---

## 🛠️ Compilar e Instalar desde el Código Fuente (Linux)

Si querés compilar la aplicación desde cero en tu propia máquina para generar el ejecutable nativo e instalarlo en tu sistema, sigue estos pasos:

**1. Clonar el repositorio:**
```bash
git clone [https://github.com/femmlinux/femlinux-downloader.git](https://github.com/femmlinux/femlinux-downloader.git)
cd femlinux-downloader

2. Instalar dependencias del sistema:
Dependiendo de tu distribución, instalá las herramientas necesarias:

    En Debian / Ubuntu / antiX: sudo apt install ffmpeg python3-tk python3-pip

    En Arch Linux: sudo pacman -S ffmpeg tk python-pip

3. Instalar las librerías de Python y el compilador (PyInstaller):
Bash

pip install yt-dlp tkinterdnd2 pyinstaller

4. Compilar el ejecutable:
Este comando transformará el código de Python en un binario independiente:
Bash

pyinstaller --onefile --windowed --name femlinux-downloader femlinux-downloader.py

5. Instalar en el sistema:
Una vez finalizada la compilación, mové el archivo generado a la carpeta de binarios de tu sistema para poder ejecutarlo desde cualquier lado:
Bash

sudo cp dist/femlinux-downloader /usr/local/bin/
sudo chmod +x /usr/local/bin/femlinux-downloader

¡Listo! Ahora podés abrir la terminal, escribir femlinux-downloader y presionar Enter para usar la aplicación.
⚠️ Descargo de Responsabilidad (Disclaimer)

Esta aplicación fue creada como una herramienta de utilidad personal, orientada principalmente a que los creadores puedan descargar y recuperar sus propios videos en caso de haber perdido los archivos originales.

No me hago responsable por el uso que se le dé a esta aplicación. La descarga de contenido de terceros sin autorización y su posterior distribución constituye una violación a los derechos de autor (copyright), una práctica con la cual no estoy de acuerdo ni fomento bajo ninguna circunstancia. El uso de este software para descargar material protegido corre bajo la exclusiva y total responsabilidad del usuario final.
FemLinux Downloader (English)

An automatic YouTube download manager designed to recover your own files quickly and easily. It allows you to extract audio in MP3 format or download the full video in MP4 format, mapping all available resolutions through an intuitive graphical interface.
🛠️ Build and Install from Source (Linux)

If you want to build the application from scratch on your own machine to generate a native executable and install it on your system, follow these steps:

1. Clone the repository:
Bash

git clone [https://github.com/femmlinux/femlinux-downloader.git](https://github.com/femmlinux/femlinux-downloader.git)
cd femlinux-downloader

2. Install system dependencies:
Depending on your distribution, install the required tools:

    On Debian / Ubuntu / antiX: sudo apt install ffmpeg python3-tk python3-pip

    On Arch Linux: sudo pacman -S ffmpeg tk python-pip

3. Install Python libraries and the compiler (PyInstaller):
Bash

pip install yt-dlp tkinterdnd2 pyinstaller

4. Build the executable:
This command will pack the Python code into a standalone binary:
Bash

pyinstaller --onefile --windowed --name femlinux-downloader femlinux-downloader.py

5. Install on the system:
Once the build is complete, move the generated file to your system's binaries folder so you can run it from anywhere:
Bash

sudo cp dist/femlinux-downloader /usr/local/bin/
sudo chmod +x /usr/local/bin/femlinux-downloader

Done! You can now open a terminal, type femlinux-downloader, and press Enter to launch the application.
⚠️ Disclaimer

This application was created as a personal utility tool, primarily intended to allow creators to download and recover their own videos in the event of losing the original files.

I am not responsible for how this application is used. Downloading unauthorized third-party content and its subsequent distribution constitutes a copyright violation, a practice I do not agree with nor encourage under any circumstances. The use of this software to download copyrighted material is the sole and strict responsibility of the end user.
