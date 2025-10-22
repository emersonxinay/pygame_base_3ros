# ============================================================================
# ARCHIVO: principal.py
# ============================================================================
"""
Módulo principal del juego.
Coordina la inicialización y ejecución del bucle principal del juego.
"""
import pygame as pg
from init_pygame import inicializar_pygame, crear_ventana, establecer_icono
from recursos import cargar_recursos
from variables import inicializar_variables, ANCHO_VENTANA, ALTO_VENTANA, FPS
from eventos import procesar_eventos
from movimientos import actualizar_movimiento_jugador
from enemigo import generar_enemigo, actualizar_enemigos
from actualizacion import actualizar_proyectiles, detectar_colisiones, detectar_colision_jugador_enemigo, actualizar_explosiones
from renderizado import renderizar_juego
from audio import inicializar_mixer, cargar_sonidos, reproducir_musica_fondo  # NUEVO


def ejecutar_juego():
    """
    Función principal que ejecuta el bucle del juego.
    Inicializa todos los componentes y coordina la actualización y renderizado.
    """
    # Inicialización
    reloj = inicializar_pygame()
    ventana = crear_ventana(ANCHO_VENTANA, ALTO_VENTANA, "Mi primer juego")
    establecer_icono("icono.png")

    # NUEVO: Inicializar sistema de audio
    inicializar_mixer()

    # Cargar recursos
    recursos = cargar_recursos()

    # NUEVO: Cargar sonidos
    sonidos = cargar_sonidos()

    # NUEVO: Reproducir música de fondo
    reproducir_musica_fondo(sonidos['musica_fondo'], volumen=0.3)

    # Inicializar estado del juego
    estado = inicializar_variables()
    estado['sonidos'] = sonidos  # NUEVO: Agregar sonidos al estado
    
    # Bucle principal del juego
    while estado['correr']:
        # Procesar eventos
        estado['correr'] = procesar_eventos(estado)
        
        # Actualizar movimiento del jugador
        actualizar_movimiento_jugador(estado['jugador'])
        
        # Generar y actualizar enemigos
        generar_enemigo(estado)
        actualizar_enemigos(estado['enemigos'])
        
        # Actualizar proyectiles
        actualizar_proyectiles(estado['proyectiles'])

        # Detectar colisiones (MODIFICADO: ahora recibe estado para sumar puntos)
        detectar_colisiones(estado['proyectiles'], estado['enemigos'], estado)

        # Detectar colisión jugador-enemigo (MODIFICADO: ahora recibe todo el estado)
        detectar_colision_jugador_enemigo(estado)

        # NUEVO: Actualizar explosiones
        actualizar_explosiones(estado['explosiones'])

        # NUEVO: Manejar invulnerabilidad temporal
        if estado['invulnerable']:
            tiempo_actual = pg.time.get_ticks()
            if tiempo_actual - estado['tiempo_invulnerabilidad'] > 2000:  # 2 segundos
                estado['invulnerable'] = False
                estado['jugador_visible'] = True

        # Renderizar todo
        renderizar_juego(ventana, recursos, estado)

        # Controlar velocidad de fotogramas
        reloj.tick(FPS)

    # Finalizar pygame
    pg.quit()


if __name__ == "__main__":
    ejecutar_juego()
