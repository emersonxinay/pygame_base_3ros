# ============================================================================
# ARCHIVO: actualizacion.py
# ============================================================================
"""
Módulo de actualización del estado del juego.
Gestiona proyectiles y detección de colisiones.
"""


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


def detectar_colisiones(proyectiles, enemigos):
    """
    Detecta colisiones entre proyectiles y enemigos, eliminando ambos en caso de impacto.
    
    Args:
        proyectiles (list): Lista de tuplas (proyectil, velocidad).
        enemigos (list): Lista de tuplas (enemigo, velocidad).
    """
    proyectiles_a_eliminar = []
    enemigos_a_eliminar = []
    
    # Detectar todas las colisiones
    for proyectil, p_vel in proyectiles:
        for enemigo, e_vel in enemigos:
            if proyectil.colliderect(enemigo):
                if (proyectil, p_vel) not in proyectiles_a_eliminar:
                    proyectiles_a_eliminar.append((proyectil, p_vel))
                if (enemigo, e_vel) not in enemigos_a_eliminar:
                    enemigos_a_eliminar.append((enemigo, e_vel))
    
    # Eliminar proyectiles impactados
    for proyectil in proyectiles_a_eliminar:
        if proyectil in proyectiles:
            proyectiles.remove(proyectil)
    
    # Eliminar enemigos destruidos
    for enemigo in enemigos_a_eliminar:
        if enemigo in enemigos:
            enemigos.remove(enemigo)
