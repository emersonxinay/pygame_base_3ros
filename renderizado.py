# ============================================================================
# ARCHIVO: renderizado.py
# ============================================================================
"""
Módulo de renderizado gráfico.
Gestiona el dibujado de todos los elementos visuales del juego.
"""
import pygame


def renderizar_juego(ventana, recursos, estado):
    """
    Dibuja todos los elementos del juego en la ventana.
    
    Args:
        ventana (pygame.Surface): Superficie de la ventana donde se dibujará.
        recursos (dict): Diccionario con todos los recursos gráficos.
        estado (dict): Diccionario con el estado actual del juego.
    """
    # Dibujar fondo
    ventana.blit(recursos['fondo'], (0, 0))
    
    # Dibujar jugador
    jugador = estado['jugador']
    ventana.blit(recursos['jugador'], (jugador.x, jugador.y))
    
    # Dibujar proyectiles
    dibujar_proyectiles(ventana, recursos['proyectil'], estado['proyectiles'])
    
    # Dibujar enemigos
    dibujar_enemigos(ventana, recursos['enemigo'], estado['enemigos'])
    
    # Actualizar pantalla
    pygame.display.flip()


def dibujar_proyectiles(ventana, imagen_proyectil, proyectiles):
    """
    Dibuja todos los proyectiles activos en la ventana.
    
    Args:
        ventana (pygame.Surface): Superficie donde se dibujará.
        imagen_proyectil (pygame.Surface): Imagen del proyectil.
        proyectiles (list): Lista de tuplas (proyectil, velocidad).
    """
    for proyectil, _ in proyectiles:
        ventana.blit(imagen_proyectil, (proyectil.x, proyectil.y))


def dibujar_enemigos(ventana, imagen_enemigo, enemigos):
    """
    Dibuja todos los enemigos activos en la ventana.
    
    Args:
        ventana (pygame.Surface): Superficie donde se dibujará.
        imagen_enemigo (pygame.Surface): Imagen del enemigo.
        enemigos (list): Lista de tuplas (enemigo, velocidad).
    """
    for enemigo, _ in enemigos:
        ventana.blit(imagen_enemigo, (enemigo.x, enemigo.y))
