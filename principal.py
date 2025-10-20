# ============================================================================
# ARCHIVO: principal.py
# ============================================================================
"""
Módulo principal del juego.
Coordina la inicialización y ejecución del bucle principal del juego.
"""
import pygame
from init_pygame import inicializar_pygame, crear_ventana, establecer_icono
from recursos import cargar_recursos
from variables import inicializar_variables, ANCHO_VENTANA, ALTO_VENTANA, FPS
from eventos import procesar_eventos
from movimientos import actualizar_movimiento_jugador
from enemigo import generar_enemigo, actualizar_enemigos
from actualizacion import actualizar_proyectiles, detectar_colisiones
from renderizado import renderizar_juego


def ejecutar_juego():
    """
    Función principal que ejecuta el bucle del juego.
    Inicializa todos los componentes y coordina la actualización y renderizado.
    """
    # Inicialización
    reloj = inicializar_pygame()
    ventana = crear_ventana(ANCHO_VENTANA, ALTO_VENTANA, "Mi primer juego")
    establecer_icono("icono.png")
    
    # Cargar recursos
    recursos = cargar_recursos()
    
    # Inicializar estado del juego
    estado = inicializar_variables()
    
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
        
        # Detectar colisiones
        detectar_colisiones(estado['proyectiles'], estado['enemigos'])
        
        # Renderizar todo
        renderizar_juego(ventana, recursos, estado)
        
        # Controlar velocidad de fotogramas
        reloj.tick(FPS)
    
    # Finalizar pygame
    pygame.quit()


if __name__ == "__main__":
    ejecutar_juego()
