import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
from tkinterdnd2 import TkinterDnD, DND_TEXT
import yt_dlp
import threading
import os

# --- Configuración de Carpetas ---
def obtener_carpeta_musica():
    musica_es = os.path.expanduser('~/Música')
    musica_en = os.path.expanduser('~/Music')
    if os.path.exists(musica_es): return list(os.path.split(musica_es))
    elif os.path.exists(musica_en): return list(os.path.split(musica_en))
    return [os.path.expanduser('~'), 'Descargas']

ruta_base, carpeta_actual = obtener_carpeta_musica()
carpeta_descarga = os.path.join(ruta_base, carpeta_actual)
titulo_actual = "Ninguno"

def seleccionar_carpeta():
    global carpeta_descarga
    seleccionada = filedialog.askdirectory(initialdir=carpeta_descarga, title="Seleccionar Destino")
    if seleccionada:
        carpeta_descarga = seleccionada
        lbl_carpeta.config(text=f"📂 Guardar en: {carpeta_descarga}")

# --- Manejo de Drag & Drop ---
def al_soltar_enlace_audio(event): procesar_drop(event, caja_enlaces_audio)
def al_soltar_enlace_video(event): procesar_drop(event, caja_enlaces_video)

def procesar_drop(event, caja_texto):
    url = event.data.strip()
    if url.startswith('{') and url.endswith('}'): url = url[1:-1].strip()
    if url:
        contenido = caja_texto.get("1.0", tk.END).strip()
        if contenido == "": caja_texto.insert(tk.END, url + '\n')
        else: caja_texto.insert(tk.END, '\n' + url + '\n')
        caja_texto.see(tk.END)

# --- Hooks y UI Dinámica ---
def hook_progreso(d):
    global titulo_actual
    if d['status'] == 'downloading':
        titulo_actual = d.get('info_dict', {}).get('title', 'Archivo de YouTube')
        porcentaje = d.get('_percent_str', '0%').strip()
        descargado = d.get('_downloaded_bytes_str', '0MiB').strip()
        total = d.get('_total_bytes_str', d.get('_total_bytes_estimate_str', '?\nMiB')).strip()
        
        info = f"▶️ {titulo_actual}\n📊 {descargado} de {total} ({porcentaje})"
        ventana.after(0, actualizar_lbl_progreso, info)

def actualizar_lbl_progreso(texto): lbl_progreso.config(text=texto, fg="#007ACC")

def agregar_al_historial(linea):
    txt_historial.config(state=tk.NORMAL)
    txt_historial.insert(tk.END, linea + "\n")
    txt_historial.see(tk.END)
    txt_historial.config(state=tk.DISABLED)

# --- Lógica de Descarga Centralizada ---
def iniciar_descarga():
    tab_activa = notebook.index(notebook.select())
    
    if tab_activa == 0:
        texto = caja_enlaces_audio.get("1.0", tk.END).strip()
        ignorar_listas = True if opcion_playlist_audio.get() == 1 else False
        modo = "audio"
        calidad = None
    else:
        texto = caja_enlaces_video.get("1.0", tk.END).strip()
        ignorar_listas = True if opcion_playlist_video.get() == 1 else False
        modo = "video"
        
        # Mapeo inteligente de resoluciones para yt-dlp
        calidad_sel = combo_calidad.get()
        if calidad_sel == "4K":
            calidad = "2160"
        elif calidad_sel == "2K":
            calidad = "1440"
        else:
            calidad = calidad_sel.replace("p", "")

    enlaces = [linea.strip() for linea in texto.split('\n') if linea.strip()]

    if not enlaces:
        messagebox.showwarning("Atención", "Por favor, ingresá al menos un enlace en la pestaña actual.")
        return

    # Bloquear interfaz durante el proceso
    btn_descargar.config(state=tk.DISABLED)
    btn_carpeta.config(state=tk.DISABLED)
    txt_historial.config(state=tk.NORMAL)
    txt_historial.delete("1.0", tk.END)
    txt_historial.config(state=tk.DISABLED)

    hilo = threading.Thread(target=proceso_por_lotes, args=(enlaces, ignorar_listas, modo, calidad))
    hilo.start()

def proceso_por_lotes(enlaces, ignorar_listas, modo, calidad):
    global titulo_actual
    
    opciones = {
        'outtmpl': os.path.join(carpeta_descarga, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [hook_progreso],
        'noplaylist': ignorar_listas
    }

    if modo == "audio":
        opciones['format'] = 'bestaudio/best'
        opciones['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        # Busca el formato contenedor mp4 que cumpla con el límite de altura de resolución seleccionado
        opciones['format'] = f'bestvideo[height<={calidad}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        opciones['merge_output_format'] = 'mp4'

    for i, url in enumerate(enlaces, start=1):
        titulo_actual = f"Enlace #{i} (Conectando...)"
        ventana.after(0, actualizar_lbl_progreso, f"⏳ Analizando: {titulo_actual}")
        
        with yt_dlp.YoutubeDL(opciones) as ydl:
            resultado = ydl.download([url])
            if resultado == 0:
                ventana.after(0, agregar_al_historial, f"✅ Completado: Enlace #{i}")
            else:
                ventana.after(0, agregar_al_historial, f"❌ Falló: Enlace #{i}")

    ventana.after(0, finalizar_interfaz)

def finalizar_interfaz():
    lbl_progreso.config(text="✨ ¡Todas las descargas completadas!", fg="#2E7D32")
    btn_descargar.config(state=tk.NORMAL)
    btn_carpeta.config(state=tk.NORMAL)
    caja_enlaces_audio.delete("1.0", tk.END)
    caja_enlaces_video.delete("1.0", tk.END)

# --- Interfaz Gráfica (TkinterDnD) ---
ventana = TkinterDnD.Tk()
ventana.title("Descargador Universal - Versión 3.1")
ventana.geometry("600x650")
ventana.config(padx=15, pady=15)

# Selector de Carpeta Global
frame_ruta = tk.Frame(ventana)
frame_ruta.pack(fill=tk.X, pady=(0, 10))
lbl_carpeta = tk.Label(frame_ruta, text=f"📂 Guardar en: {carpeta_descarga}", font=("Arial", 10, "italic"), anchor="w")
lbl_carpeta.pack(side=tk.LEFT, fill=tk.X, expand=True)
btn_carpeta = tk.Button(frame_ruta, text="⚙️ Cambiar", font=("Arial", 9), command=seleccionar_carpeta)
btn_carpeta.pack(side=tk.RIGHT)

# --- PESTAÑAS ---
notebook = ttk.Notebook(ventana)
notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

tab_audio = ttk.Frame(notebook)
tab_video = ttk.Frame(notebook)
notebook.add(tab_audio, text="🎵 Audio (MP3)")
notebook.add(tab_video, text="🎬 Video (MP4)")

# -- Contenido Pestaña AUDIO --
lbl_inst_audio = tk.Label(tab_audio, text="Pegá o arrastrá enlaces para extraer AUDIO:", font=("Arial", 10, "bold"))
lbl_inst_audio.pack(anchor="w", pady=(10, 5), padx=10)

caja_enlaces_audio = tk.Text(tab_audio, height=6, font=("Arial", 10))
caja_enlaces_audio.pack(fill=tk.X, padx=10, pady=5)
caja_enlaces_audio.drop_target_register(DND_TEXT)
caja_enlaces_audio.dnd_bind('<<Drop>>', al_soltar_enlace_audio)

opcion_playlist_audio = tk.IntVar(value=1)
tk.Radiobutton(tab_audio, text="Descargar el primer resultado nada más", variable=opcion_playlist_audio, value=1).pack(anchor="w", padx=10)
tk.Radiobutton(tab_audio, text="Descargar la lista entera", variable=opcion_playlist_audio, value=2).pack(anchor="w", padx=10)

# -- Contenido Pestaña VIDEO --
lbl_inst_video = tk.Label(tab_video, text="Pegá o arrastrá enlaces para descargar VIDEO:", font=("Arial", 10, "bold"))
lbl_inst_video.pack(anchor="w", pady=(10, 5), padx=10)

caja_enlaces_video = tk.Text(tab_video, height=6, font=("Arial", 10))
caja_enlaces_video.pack(fill=tk.X, padx=10, pady=5)
caja_enlaces_video.drop_target_register(DND_TEXT)
caja_enlaces_video.dnd_bind('<<Drop>>', al_soltar_enlace_video)

frame_calidad = tk.Frame(tab_video)
frame_calidad.pack(fill=tk.X, padx=10, pady=5)
tk.Label(frame_calidad, text="Resolución máxima deseada:").pack(side=tk.LEFT)

# Lista completa de resoluciones soportadas por YouTube (de mayor a menor)
resoluciones = ["4K", "2K", "1080p", "720p", "480p", "360p", "240p", "144p"]
combo_calidad = ttk.Combobox(frame_calidad, values=resoluciones, state="readonly", width=10)
combo_calidad.current(2) # 1080p por defecto como estándar base
combo_calidad.pack(side=tk.LEFT, padx=10)

opcion_playlist_video = tk.IntVar(value=1)
tk.Radiobutton(tab_video, text="Descargar el primer resultado nada más", variable=opcion_playlist_video, value=1).pack(anchor="w", padx=10)
tk.Radiobutton(tab_video, text="Descargar la lista entera", variable=opcion_playlist_video, value=2).pack(anchor="w", padx=10)

# --- BOTÓN UNIVERSAL Y MONITORES ---
btn_descargar = tk.Button(ventana, text="Descargar Todo", bg="#2E7D32", fg="white", font=("Arial", 12, "bold"), command=iniciar_descarga)
btn_descargar.pack(fill=tk.X, pady=(5, 10))

lbl_progreso = tk.Label(ventana, text="Esperando enlaces...", font=("Arial", 10), fg="#666", justify=tk.LEFT, anchor="w")
lbl_progreso.pack(fill=tk.X, pady=(0, 5))

txt_historial = scrolledtext.ScrolledText(ventana, height=6, font=("Arial", 9), bg="#F5F5F5")
txt_historial.pack(fill=tk.BOTH, expand=True)
txt_historial.config(state=tk.DISABLED)

ventana.mainloop()
