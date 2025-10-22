# ============================================================================
# ARCHIVO: audio.py
# ============================================================================
"""
Módulo de gestión de audio.
Carga y reproduce efectos de sonido y música de fondo del juego.
"""
import pygame as pg
import os

# NUEVO: Ruta de la carpeta de audios
CARPETA_AUDIOS = "audios"


def inicializar_mixer():
    """
    Inicializa el sistema de audio de pygame.
    Debe llamarse antes de cargar cualquier sonido.
    """
    pg.mixer.init()


def cargar_sonidos():
    """
    Carga todos los efectos de sonido y música del juego.
    MODIFICADO: Carga archivos desde la carpeta 'audios'.

    Returns:
        dict: Diccionario con todos los sonidos cargados, indexados por nombre.
    """
    sonidos = {
        'musica_fondo': os.path.join(CARPETA_AUDIOS, 'musica_fondo.mp3'),
        'disparo': cargar_efecto('disparo.mp3'),
        'explosion': cargar_efecto('explosion.mp3'),
        'danio': cargar_efecto('danio.mp3'),
        'game_over': cargar_efecto('game_over.mp3'),
        'reinicio': cargar_efecto('reinicio.mp3')
    }
    return sonidos


def cargar_efecto(nombre_archivo):
    """
    Carga un efecto de sonido desde la carpeta de audios.
    MODIFICADO: Ahora busca en la carpeta 'audios'.

    Args:
        nombre_archivo (str): Nombre del archivo de audio (ej: 'disparo.mp3').

    Returns:
        pg.mixer.Sound: Objeto de sonido cargado.
    """
    ruta = os.path.join(CARPETA_AUDIOS, nombre_archivo)
    try:
        return pg.mixer.Sound(ruta)
    except:
        # Si no se encuentra el archivo, crear un sonido vacío
        print(f"Advertencia: No se pudo cargar el sonido '{ruta}'")
        # Crear un buffer de audio vacío
        return pg.mixer.Sound(buffer=b'\x00' * 1000)


def reproducir_musica_fondo(ruta_musica, volumen=0.3, loop=True):
    """
    Reproduce música de fondo en loop.

    Args:
        ruta_musica (str): Ruta del archivo de música.
        volumen (float): Volumen de la música (0.0 a 1.0).
        loop (bool): Si True, la música se reproduce en loop infinito.
    """
    try:
        pg.mixer.music.load(ruta_musica)
        pg.mixer.music.set_volume(volumen)
        if loop:
            pg.mixer.music.play(-1)  # -1 significa loop infinito
        else:
            pg.mixer.music.play()
    except:
        print(f"Advertencia: No se pudo cargar la música '{ruta_musica}'")


def detener_musica():
    """
    Detiene la música de fondo.
    """
    pg.mixer.music.stop()


def reproducir_efecto(sonido, volumen=0.5):
    """
    Reproduce un efecto de sonido.

    Args:
        sonido (pg.mixer.Sound): Objeto de sonido a reproducir.
        volumen (float): Volumen del efecto (0.0 a 1.0).
    """
    if sonido:
        sonido.set_volume(volumen)
        sonido.play()


def pausar_musica():
    """
    Pausa la música de fondo.
    """
    pg.mixer.music.pause()


def reanudar_musica():
    """
    Reanuda la música de fondo.
    """
    pg.mixer.music.unpause()
