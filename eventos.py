# ============================================================================
# ARCHIVO: eventos.py
# ============================================================================
"""
Módulo de procesamiento de eventos.
Gestiona la entrada del usuario y eventos del sistema.
"""
import pygame


def procesar_eventos(estado):
    """
    Procesa los eventos del juego, incluyendo el cierre de ventana y la creación de proyectiles.
    
    Args:
        estado (dict): Diccionario con el estado actual del juego.
    
    Returns:
        bool: True si el juego debe continuar, False si debe cerrarse.
    """
    evento = pygame.event.poll()
    
    if evento.type == pygame.QUIT:
        return False
    
    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
        crear_proyectil(estado)
    
    return True


def crear_proyectil(estado):
    """
    Crea un nuevo proyectil en la posición del jugador.
    
    Args:
        estado (dict): Diccionario con el estado actual del juego.
    """
    from variables import VELOCIDAD_PROYECTIL, TAMANO_PROYECTIL_ANCHO, TAMANO_PROYECTIL_ALTO
    
    jugador = estado['jugador']
    proyectiles = estado['proyectiles']
    
    proyectil = pygame.Rect(
        jugador.centerx - TAMANO_PROYECTIL_ANCHO // 2,
        jugador.y,
        TAMANO_PROYECTIL_ANCHO,
        TAMANO_PROYECTIL_ALTO
    )
    proyectiles.append((proyectil, VELOCIDAD_PROYECTIL))
