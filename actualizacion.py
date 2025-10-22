# ============================================================================
# ARCHIVO: actualizacion.py
# ============================================================================
"""
Módulo de actualización del estado del juego.
Gestiona proyectiles, detección de colisiones y explosiones.
"""
import pygame as pg


def actualizar_proyectiles(proyectiles):
    """
    Actualiza la posición de todos los proyectiles y elimina los que salen de la pantalla.
    
    Args:
        proyectiles (list): Lista de tuplas (proyectil, velocidad).
    """
    for proyectil, vel in proyectiles[:]:
        proyectil.y -= vel
        if proyectil.y < -20:
            proyectiles.remove((proyectil, vel))


def detectar_colisiones(proyectiles, enemigos, estado):
    """
    Detecta colisiones entre proyectiles y enemigos, eliminando ambos en caso de impacto.
    MODIFICADO: Ahora suma puntos, reproduce sonido y crea explosión visual.

    Args:
        proyectiles (list): Lista de tuplas (proyectil, velocidad).
        enemigos (list): Lista de tuplas (enemigo, velocidad).
        estado (dict): Estado del juego para actualizar puntos.

    Returns:
        int: Número de enemigos destruidos.
    """
    from variables import PUNTOS_POR_ENEMIGO
    from audio import reproducir_efecto

    proyectiles_a_eliminar = []
    enemigos_a_eliminar = []
    posiciones_explosiones = []  # NUEVO: guardar posiciones para explosiones

    # Detectar todas las colisiones
    for proyectil, p_vel in proyectiles:
        for enemigo, e_vel in enemigos:
            if proyectil.colliderect(enemigo):
                if (proyectil, p_vel) not in proyectiles_a_eliminar:
                    proyectiles_a_eliminar.append((proyectil, p_vel))
                if (enemigo, e_vel) not in enemigos_a_eliminar:
                    enemigos_a_eliminar.append((enemigo, e_vel))
                    # NUEVO: Guardar posición del centro del enemigo
                    posiciones_explosiones.append((enemigo.centerx, enemigo.centery))

    # Eliminar proyectiles impactados
    for proyectil in proyectiles_a_eliminar:
        if proyectil in proyectiles:
            proyectiles.remove(proyectil)

    # Eliminar enemigos destruidos y sumar puntos
    enemigos_destruidos = 0
    for enemigo in enemigos_a_eliminar:
        if enemigo in enemigos:
            enemigos.remove(enemigo)
            enemigos_destruidos += 1
            estado['puntos'] += PUNTOS_POR_ENEMIGO  # Sumar puntos

            # Reproducir sonido de explosión
            if 'sonidos' in estado and estado['sonidos']['explosion']:
                reproducir_efecto(estado['sonidos']['explosion'], volumen=0.5)

    # NUEVO: Crear explosiones en las posiciones de colisión
    for pos_x, pos_y in posiciones_explosiones:
        crear_explosion(estado, pos_x, pos_y)

    return enemigos_destruidos


def detectar_colision_jugador_enemigo(estado):
    """
    Detecta colisiones entre el jugador y los enemigos.
    MODIFICADO: Ahora maneja vidas, invulnerabilidad, fin del juego y sonidos.

    Args:
        estado (dict): Estado del juego.
    """
    import pygame as pg
    from audio import reproducir_efecto

    # No verificar colisiones si el jugador es invulnerable o el juego terminó
    if estado['invulnerable'] or estado['juego_terminado']:
        return

    # Verificar si pasó el tiempo de invulnerabilidad
    if estado['invulnerable']:
        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - estado['tiempo_invulnerabilidad'] > 2000:  # 2 segundos
            estado['invulnerable'] = False
            estado['jugador_visible'] = True

    # Detectar colisión
    for enemigo, _ in estado['enemigos']:
        if estado['jugador'].colliderect(enemigo):
            # Perder una vida
            estado['vidas'] -= 1

            if estado['vidas'] <= 0:
                # Game Over
                estado['juego_terminado'] = True
                estado['jugador_visible'] = False

                # NUEVO: Reproducir sonido de Game Over
                if 'sonidos' in estado and estado['sonidos']['game_over']:
                    reproducir_efecto(estado['sonidos']['game_over'], volumen=0.7)
            else:
                # Activar invulnerabilidad temporal
                estado['invulnerable'] = True
                estado['tiempo_invulnerabilidad'] = pg.time.get_ticks()
                estado['jugador_visible'] = False

                # NUEVO: Reproducir sonido de daño
                if 'sonidos' in estado and estado['sonidos']['danio']:
                    reproducir_efecto(estado['sonidos']['danio'], volumen=0.6)

            # NUEVO: Crear explosión en la posición del jugador
            crear_explosion(estado, estado['jugador'].centerx, estado['jugador'].centery)

            # Eliminar el enemigo que colisionó
            estado['enemigos'].remove((enemigo, _))
            break


def crear_explosion(estado, x, y):
    """
    NUEVO: Crea una explosión en la posición especificada.

    Args:
        estado (dict): Estado del juego.
        x (int): Posición X del centro de la explosión.
        y (int): Posición Y del centro de la explosión.
    """
    tiempo_actual = pg.time.get_ticks()

    explosion = {
        'x': x,
        'y': y,
        'tiempo_inicio': tiempo_actual,
        'frame_actual': 0
    }

    estado['explosiones'].append(explosion)


def actualizar_explosiones(explosiones):
    """
    NUEVO: Actualiza las explosiones y elimina las que terminaron.

    Args:
        explosiones (list): Lista de explosiones activas.
    """
    from variables import DURACION_EXPLOSION, FRAMES_EXPLOSION

    tiempo_actual = pg.time.get_ticks()
    explosiones_a_eliminar = []

    for explosion in explosiones:
        tiempo_transcurrido = tiempo_actual - explosion['tiempo_inicio']

        # Calcular frame actual basado en el tiempo
        progreso = tiempo_transcurrido / DURACION_EXPLOSION
        explosion['frame_actual'] = min(int(progreso * FRAMES_EXPLOSION), FRAMES_EXPLOSION - 1)

        # Eliminar si terminó la animación
        if tiempo_transcurrido >= DURACION_EXPLOSION:
            explosiones_a_eliminar.append(explosion)

    # Eliminar explosiones completadas
    for explosion in explosiones_a_eliminar:
        if explosion in explosiones:
            explosiones.remove(explosion)
