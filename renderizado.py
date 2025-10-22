# ============================================================================
# ARCHIVO: renderizado.py
# ============================================================================
"""
Módulo de renderizado gráfico.
Gestiona el dibujado de todos los elementos visuales del juego.
"""
import pygame as pg

# NUEVO: Configuración de fuente para el HUD
pg.font.init()
FUENTE_HUD = pg.font.Font(None, 36)
FUENTE_GAME_OVER = pg.font.Font(None, 72)


def renderizar_juego(ventana, recursos, estado):
    """
    Dibuja todos los elementos del juego en la ventana.
    
    Args:
        ventana (pg.Surface): Superficie de la ventana donde se dibujará.
        recursos (dict): Diccionario con todos los recursos gráficos.
        estado (dict): Diccionario con el estado actual del juego.
    """
    # Dibujar fondo
    ventana.blit(recursos['fondo'], (0, 0))

    # Dibujar jugador (MODIFICADO: solo si está visible)
    if estado['jugador_visible']:
        jugador = estado['jugador']
        ventana.blit(recursos['jugador'], (jugador.x, jugador.y))
    
    # Dibujar proyectiles
    dibujar_proyectiles(ventana, recursos['proyectil'], estado['proyectiles'])
    
    # Dibujar enemigos
    dibujar_enemigos(ventana, recursos['enemigo'], estado['enemigos'])

    # NUEVO: Dibujar explosiones
    dibujar_explosiones(ventana, recursos['explosion'], estado['explosiones'])

    # NUEVO: Dibujar HUD (vidas y puntos)
    dibujar_hud(ventana, estado)

    # NUEVO: Dibujar pantalla de Game Over si el juego terminó
    if estado['juego_terminado']:
        dibujar_game_over(ventana, estado)

    # Actualizar pantalla
    pg.display.flip()


def dibujar_proyectiles(ventana, imagen_proyectil, proyectiles):
    """
    Dibuja todos los proyectiles activos en la ventana.
    
    Args:
        ventana (pg.Surface): Superficie donde se dibujará.
        imagen_proyectil (pg.Surface): Imagen del proyectil.
        proyectiles (list): Lista de tuplas (proyectil, velocidad).
    """
    for proyectil, _ in proyectiles:
        ventana.blit(imagen_proyectil, (proyectil.x, proyectil.y))


def dibujar_enemigos(ventana, imagen_enemigo, enemigos):
    """
    Dibuja todos los enemigos activos en la ventana.

    Args:
        ventana (pg.Surface): Superficie donde se dibujará.
        imagen_enemigo (pg.Surface): Imagen del enemigo.
        enemigos (list): Lista de tuplas (enemigo, velocidad).
    """
    for enemigo, _ in enemigos:
        ventana.blit(imagen_enemigo, (enemigo.x, enemigo.y))


def dibujar_explosiones(ventana, animacion_explosion, explosiones):
    """
    NUEVO: Dibuja todas las explosiones activas en la ventana.

    Args:
        ventana (pg.Surface): Superficie donde se dibujará.
        animacion_explosion (list): Lista de frames de la animación de explosión.
        explosiones (list): Lista de explosiones activas.
    """
    from variables import TAMANO_EXPLOSION

    for explosion in explosiones:
        # Obtener el frame actual de la animación
        frame = animacion_explosion[explosion['frame_actual']]

        # Calcular posición para centrar la explosión
        x = explosion['x'] - TAMANO_EXPLOSION // 2
        y = explosion['y'] - TAMANO_EXPLOSION // 2

        # Dibujar el frame
        ventana.blit(frame, (x, y))


def dibujar_hud(ventana, estado):
    """
    NUEVO: Dibuja el HUD con información de vidas y puntos.

    Args:
        ventana (pg.Surface): Superficie donde se dibujará.
        estado (dict): Estado del juego.
    """
    # Texto de vidas
    texto_vidas = FUENTE_HUD.render(f"Vidas: {estado['vidas']}", True, (255, 255, 255))
    ventana.blit(texto_vidas, (10, 10))

    # Texto de puntos
    texto_puntos = FUENTE_HUD.render(f"Puntos: {estado['puntos']}", True, (255, 255, 255))
    ventana.blit(texto_puntos, (10, 50))


def dibujar_game_over(ventana, estado):
    """
    NUEVO: Dibuja la pantalla de Game Over con instrucciones para reiniciar.

    Args:
        ventana (pg.Surface): Superficie donde se dibujará.
        estado (dict): Estado del juego.
    """
    # Superficie semi-transparente
    overlay = pg.Surface(ventana.get_size())
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
    ventana.blit(overlay, (0, 0))

    # Texto GAME OVER
    texto_game_over = FUENTE_GAME_OVER.render("GAME OVER", True, (255, 0, 0))
    rect_game_over = texto_game_over.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 2 - 50))
    ventana.blit(texto_game_over, rect_game_over)

    # Puntuación final
    texto_puntuacion = FUENTE_HUD.render(f"Puntuacion Final: {estado['puntos']}", True, (255, 255, 255))
    rect_puntuacion = texto_puntuacion.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 2 + 20))
    ventana.blit(texto_puntuacion, rect_puntuacion)

    # Instrucciones para reiniciar
    texto_reiniciar = FUENTE_HUD.render("Presiona R para reiniciar", True, (255, 255, 255))
    rect_reiniciar = texto_reiniciar.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 2 + 70))
    ventana.blit(texto_reiniciar, rect_reiniciar)
