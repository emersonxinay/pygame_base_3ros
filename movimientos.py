# ============================================================================
# ARCHIVO: movimientos.py
# ============================================================================
"""
Módulo de control de movimiento del jugador.
Gestiona el desplazamiento del jugador y los límites de la pantalla.
"""
import pygame
from variables import VELOCIDAD_JUGADOR, ANCHO_VENTANA, ALTO_VENTANA


def actualizar_movimiento_jugador(jugador):
    """
    Actualiza la posición del jugador basándose en las teclas presionadas.
    Mantiene al jugador dentro de los límites de la ventana.
    
    Args:
        jugador (pygame.Rect): Rectángulo que representa al jugador.
    """
    teclas = pygame.key.get_pressed()
    
    # Aplicar movimiento según teclas presionadas
    if teclas[pygame.K_LEFT]:
        jugador.x -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_RIGHT]:
        jugador.x += VELOCIDAD_JUGADOR
    if teclas[pygame.K_UP]:
        jugador.y -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_DOWN]:
        jugador.y += VELOCIDAD_JUGADOR
    
    # Aplicar límites de la ventana
    aplicar_limites_ventana(jugador)


def aplicar_limites_ventana(jugador):
    """
    Restringe la posición del jugador para que no salga de los límites de la ventana.
    
    Args:
        jugador (pygame.Rect): Rectángulo que representa al jugador.
    """
    jugador.x = max(0, min(jugador.x, ANCHO_VENTANA - jugador.width))
    jugador.y = max(0, min(jugador.y, ALTO_VENTANA - jugador.height))
