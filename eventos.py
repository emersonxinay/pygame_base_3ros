# ============================================================================
# ARCHIVO: eventos.py
# ============================================================================
"""
Módulo de procesamiento de eventos.
Gestiona la entrada del usuario y eventos del sistema.
"""
import pygame as pg


def procesar_eventos(estado):
    """
    Procesa los eventos del juego, incluyendo el cierre de ventana y la creación de proyectiles.
    MODIFICADO: Ahora maneja tecla R para reiniciar y bloquea disparo si el juego terminó.

    Args:
        estado (dict): Diccionario con el estado actual del juego.

    Returns:
        bool: True si el juego debe continuar, False si debe cerrarse.
    """
    from variables import inicializar_variables
    from audio import reproducir_efecto

    evento = pg.event.poll()

    if evento.type == pg.QUIT:
        return False

    if evento.type == pg.KEYDOWN:
        # NUEVO: Reiniciar juego con tecla R
        if evento.key == pg.K_r and estado['juego_terminado']:
            # NUEVO: Reproducir sonido de reinicio
            if 'sonidos' in estado and estado['sonidos']['reinicio']:
                reproducir_efecto(estado['sonidos']['reinicio'], volumen=0.6)

            nuevo_estado = inicializar_variables()
            # Preservar los sonidos en el nuevo estado
            sonidos = estado['sonidos']
            estado.update(nuevo_estado)
            estado['sonidos'] = sonidos
        # MODIFICADO: Solo disparar si el juego no ha terminado
        elif evento.key == pg.K_SPACE and not estado['juego_terminado']:
            crear_proyectil(estado)

    return True


def crear_proyectil(estado):
    """
    Crea un nuevo proyectil en la posición del jugador.
    MODIFICADO: Ahora reproduce sonido de disparo.

    Args:
        estado (dict): Diccionario con el estado actual del juego.
    """
    from variables import VELOCIDAD_PROYECTIL, TAMANO_PROYECTIL_ANCHO, TAMANO_PROYECTIL_ALTO
    from audio import reproducir_efecto

    jugador = estado['jugador']
    proyectiles = estado['proyectiles']

    proyectil = pg.Rect(
        jugador.centerx - TAMANO_PROYECTIL_ANCHO // 2,
        jugador.y,
        TAMANO_PROYECTIL_ANCHO,
        TAMANO_PROYECTIL_ALTO
    )
    proyectiles.append((proyectil, VELOCIDAD_PROYECTIL))

    # NUEVO: Reproducir sonido de disparo
    if 'sonidos' in estado and estado['sonidos']['disparo']:
        reproducir_efecto(estado['sonidos']['disparo'], volumen=0.4)
