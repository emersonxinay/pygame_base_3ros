# ============================================================================
# ARCHIVO: variables.py
# ============================================================================
"""
Módulo de variables globales del juego.
Define constantes y estructuras de datos utilizadas en todo el programa.
"""
import pygame as pg

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
VIDAS_INICIALES = 3  # NUEVO: vidas iniciales del jugador
PUNTOS_POR_ENEMIGO = 10  # NUEVO: puntos ganados por cada enemigo destruido

# NUEVO: Configuración de explosiones
TAMANO_EXPLOSION = 64  # Tamaño de cada frame de la explosión
DURACION_EXPLOSION = 600  # Duración en milisegundos (0.6 segundos)
FRAMES_EXPLOSION = 8  # Número de frames de la animación (tu sprite sheet tiene 8)


def inicializar_variables():
    """
    Inicializa las variables dinámicas del juego que cambiarán durante la ejecución.

    Returns:
        dict: Diccionario con todas las variables del estado del juego.
    """
    jugador = pg.Rect(0, 0, TAMANO_JUGADOR, TAMANO_JUGADOR)
    proyectiles = []
    enemigos = []
    ultimo_enemigo = pg.time.get_ticks()

    estado = {
        'jugador': jugador,
        'proyectiles': proyectiles,
        'enemigos': enemigos,
        'ultimo_enemigo': ultimo_enemigo,
        'correr': True,
        'jugador_visible': True,
        'vidas': VIDAS_INICIALES,  # NUEVO: vidas del jugador
        'puntos': 0,  # NUEVO: puntuación del jugador
        'juego_terminado': False,  # NUEVO: indica si el juego terminó
        'invulnerable': False,  # NUEVO: invulnerabilidad temporal tras perder vida
        'tiempo_invulnerabilidad': 0,  # NUEVO: tiempo de invulnerabilidad
        'explosiones': []  # NUEVO: lista de explosiones activas
    }

    return estado
