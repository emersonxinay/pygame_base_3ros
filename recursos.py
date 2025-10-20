# ============================================================================
# ARCHIVO: recursos.py
# ============================================================================
"""
Módulo de gestión de recursos.
Carga y prepara todos los recursos gráficos del juego.
"""
import pygame


def cargar_imagen(ruta, ancho, alto):
    """
    Carga una imagen desde el disco y la escala al tamaño especificado.
    
    Args:
        ruta (str): Ruta del archivo de imagen.
        ancho (int): Ancho deseado en píxeles.
        alto (int): Alto deseado en píxeles.
    
    Returns:
        pygame.Surface: Imagen cargada y escalada.
    """
    imagen = pygame.image.load(ruta)
    imagen = pygame.transform.scale(imagen, (ancho, alto))
    return imagen


def cargar_recursos():
    """
    Carga todos los recursos gráficos necesarios para el juego.
    
    Returns:
        dict: Diccionario con todas las imágenes cargadas, indexadas por nombre.
    """
    recursos = {
        'fondo': cargar_imagen("fondo.png", 800, 600),
        'jugador': cargar_imagen("jugador.png", 40, 40),
        'proyectil': cargar_imagen("proyectil.png", 10, 20),
        'enemigo': cargar_imagen("enemigo.png", 50, 50)
    }
    return recursos
