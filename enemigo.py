# ============================================================================
# ARCHIVO: enemigo.py
# ============================================================================
"""
Módulo de gestión de enemigos.
Controla la generación, actualización y movimiento de enemigos.
"""
import pygame as pg
import random
from variables import (
    INTERVALO_GENERACION_ENEMIGO,
    TAMANO_ENEMIGO,
    VELOCIDAD_ENEMIGO,
    ANCHO_VENTANA,
    ALTO_VENTANA
)


def generar_enemigo(estado):
    """
    Genera un nuevo enemigo en una posición aleatoria superior si ha pasado el intervalo establecido.
    
    Args:
        estado (dict): Diccionario con el estado actual del juego.
    """
    tiempo_actual = pg.time.get_ticks()

    if tiempo_actual - estado['ultimo_enemigo'] > INTERVALO_GENERACION_ENEMIGO:
        x_enemigo = random.randint(0, ANCHO_VENTANA - TAMANO_ENEMIGO - 10)
        enemigo = pg.Rect(x_enemigo, -40, TAMANO_ENEMIGO, TAMANO_ENEMIGO)
        estado['enemigos'].append((enemigo, VELOCIDAD_ENEMIGO))
        estado['ultimo_enemigo'] = tiempo_actual


def actualizar_enemigos(enemigos):
    """
    Actualiza la posición de todos los enemigos y elimina los que salen de la pantalla.
    
    Args:
        enemigos (list): Lista de tuplas (enemigo, velocidad).
    """
    for enemigo, vel in enemigos[:]:
        enemigo.y += vel
        if enemigo.y > ALTO_VENTANA:
            enemigos.remove((enemigo, vel))
