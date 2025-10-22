# ============================================================================
# ARCHIVO: init_pygame.py
# ============================================================================
"""
Módulo de inicialización de Pygame.
Configura la ventana principal y los componentes básicos del sistema.
"""
import pygame as pg
import os


def inicializar_pygame():
    """
    Inicializa todos los módulos de pygame necesarios para el funcionamiento del juego.

    Returns:
        pg.time.Clock: Objeto reloj para controlar la tasa de fotogramas.
    """
    pg.init()
    reloj = pg.time.Clock()
    return reloj


def crear_ventana(ancho, alto, titulo):
    """
    Crea y configura la ventana principal del juego.

    Args:
        ancho (int): Ancho de la ventana en píxeles.
        alto (int): Alto de la ventana en píxeles.
        titulo (str): Título que se mostrará en la barra de la ventana.

    Returns:
        pg.Surface: Superficie de la ventana principal.
    """
    ventana = pg.display.set_mode((ancho, alto))
    pg.display.set_caption(titulo)
    return ventana


def establecer_icono(nombre_icono):
    """
    Establece el ícono de la ventana del juego.
    MODIFICADO: Ahora busca el icono en la carpeta 'imagenes'.

    Args:
        nombre_icono (str): Nombre del archivo de icono (ej: 'icono.png').
    """
    ruta_icono = os.path.join("imagenes", nombre_icono)
    try:
        icono = pg.image.load(ruta_icono)
        pg.display.set_icon(icono)
    except:
        print(f"Advertencia: No se pudo cargar el icono '{ruta_icono}'")
