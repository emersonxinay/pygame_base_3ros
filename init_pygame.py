# ============================================================================
# ARCHIVO: init_pygame.py
# ============================================================================
"""
Módulo de inicialización de Pygame.
Configura la ventana principal y los componentes básicos del sistema.
"""
import pygame


def inicializar_pygame():
    """
    Inicializa todos los módulos de pygame necesarios para el funcionamiento del juego.
    
    Returns:
        pygame.time.Clock: Objeto reloj para controlar la tasa de fotogramas.
    """
    pygame.init()
    reloj = pygame.time.Clock()
    return reloj


def crear_ventana(ancho, alto, titulo):
    """
    Crea y configura la ventana principal del juego.
    
    Args:
        ancho (int): Ancho de la ventana en píxeles.
        alto (int): Alto de la ventana en píxeles.
        titulo (str): Título que se mostrará en la barra de la ventana.
    
    Returns:
        pygame.Surface: Superficie de la ventana principal.
    """
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(titulo)
    return ventana


def establecer_icono(ruta_icono):
    """
    Establece el ícono de la ventana del juego.
    
    Args:
        ruta_icono (str): Ruta del archivo de imagen para el ícono.
    """
    icono = pygame.image.load(ruta_icono)
    pygame.display.set_icon(icono)
