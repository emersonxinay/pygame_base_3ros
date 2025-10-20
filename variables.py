# ============================================================================
# ARCHIVO: variables.py
# ============================================================================
"""
Módulo de variables globales del juego.
Define constantes y estructuras de datos utilizadas en todo el programa.
"""
import pygame

# Dimensiones de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# Configuración del jugador
TAMANO_JUGADOR = 40
VELOCIDAD_JUGADOR = 10

# Configuración de proyectiles
TAMANO_PROYECTIL_ANCHO = 10
TAMANO_PROYECTIL_ALTO = 20
VELOCIDAD_PROYECTIL = 8

# Configuración de enemigos
TAMANO_ENEMIGO = 50
VELOCIDAD_ENEMIGO = 5
INTERVALO_GENERACION_ENEMIGO = 2000  # Milisegundos

# Configuración del juego
FPS = 60


def inicializar_variables():
    """
    Inicializa las variables dinámicas del juego que cambiarán durante la ejecución.
    
    Returns:
        dict: Diccionario con todas las variables del estado del juego.
    """
    jugador = pygame.Rect(0, 0, TAMANO_JUGADOR, TAMANO_JUGADOR)
    proyectiles = []
    enemigos = []
    ultimo_enemigo = pygame.time.get_ticks()
    
    estado = {
        'jugador': jugador,
        'proyectiles': proyectiles,
        'enemigos': enemigos,
        'ultimo_enemigo': ultimo_enemigo,
        'correr': True
    }
    
    return estado
