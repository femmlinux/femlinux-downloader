# Maintainer: FemLinux Developer
pkgname=femlinux-downloader
pkgver=3.1
pkgrel=2
pkgdesc="Gestor de descargas de YouTube de alto rendimiento (Audio MP3 y Video MP4)"
arch=('x86_64')
license=('GPL')
depends=('tk' 'ffmpeg')

package() {
    # 1. Instala el binario ejecutable que compiló PyInstaller
    install -Dm755 "${startdir}/dist/femlinux-downloader" "${pkgdir}/usr/bin/femlinux-downloader"
    
    # 2. Crea el directorio para el acceso directo en el sistema de archivos del paquete
    install -dm755 "${pkgdir}/usr/share/applications"
    
    # 3. Genera e instala el archivo .desktop automáticamente en caliente
    cat <<EOF > "${pkgdir}/usr/share/applications/femlinux-downloader.desktop"
[Desktop Entry]
Version=1.0
Name=FemLinux Downloader
Comment=Gestor de descargas de YouTube automático
Exec=femlinux-downloader
Icon=download
Terminal=false
Type=Application
Categories=AudioVideo;Network;Utility;
EOF

    # 4. Asigna los permisos correctos de lectura al acceso directo
    chmod 644 "${pkgdir}/usr/share/applications/femlinux-downloader.desktop"
}
