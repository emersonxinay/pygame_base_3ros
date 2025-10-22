# ============================================================================
# ARCHIVO: recursos.py
# ============================================================================
"""
Módulo de gestión de recursos.
Carga y prepara todos los recursos gráficos del juego.
"""
import pygame as pg
import os

# NUEVO: Ruta de la carpeta de imágenes
CARPETA_IMAGENES = "imagenes"


def cargar_imagen(nombre_archivo, ancho, alto):
    """
    Carga una imagen desde la carpeta de imágenes y la escala al tamaño especificado.
    MODIFICADO: Ahora busca en la carpeta 'imagenes'.

    Args:
        nombre_archivo (str): Nombre del archivo de imagen (ej: 'jugador.png').
        ancho (int): Ancho deseado en píxeles.
        alto (int): Alto deseado en píxeles.

    Returns:
        pg.Surface: Imagen cargada y escalada.
    """
    ruta = os.path.join(CARPETA_IMAGENES, nombre_archivo)
    imagen = pg.image.load(ruta)
    imagen = pg.transform.scale(imagen, (ancho, alto))
    return imagen


def cargar_recursos():
    """
    Carga todos los recursos gráficos necesarios para el juego.
    MODIFICADO: Carga imágenes desde la carpeta 'imagenes' + animación de explosión.

    Returns:
        dict: Diccionario con todas las imágenes cargadas, indexadas por nombre.
    """
    from variables import TAMANO_EXPLOSION, FRAMES_EXPLOSION

    recursos = {
        'fondo': cargar_imagen('fondo.png', 800, 600),
        'jugador': cargar_imagen('jugador.png', 40, 40),
        'proyectil': cargar_imagen('proyectil.png', 10, 20),
        'enemigo': cargar_imagen('enemigo.png', 50, 50),
        'explosion': cargar_animacion_explosion(TAMANO_EXPLOSION, FRAMES_EXPLOSION)  # NUEVO
    }
    return recursos


def cargar_animacion_explosion(tamano, frames):
    """
    NUEVO: Carga la animación de explosión desde un sprite sheet o frames individuales.

    Args:
        tamano (int): Tamaño de cada frame de explosión.
        frames (int): Número de frames esperados.

    Returns:
        list: Lista de superficies con los frames de la animación.
    """
    animacion = []

    # PRIORIDAD 1: Intentar cargar sprite sheet horizontal (explosion.png)
    try:
        ruta_sprite_sheet = os.path.join(CARPETA_IMAGENES, 'explosion.png')
        sprite_sheet = pg.image.load(ruta_sprite_sheet)

        # Obtener dimensiones del sprite sheet
        ancho_total = sprite_sheet.get_width()
        alto = sprite_sheet.get_height()
        ancho_frame = ancho_total // frames  # Dividir en frames

        print(f"Sprite sheet de explosión cargado: {ancho_total}x{alto} px, {frames} frames de {ancho_frame}x{alto} px")

        # Extraer cada frame del sprite sheet
        for i in range(frames):
            # Crear superficie para el frame
            frame_surface = pg.Surface((ancho_frame, alto), pg.SRCALPHA)

            # Copiar la porción del sprite sheet
            area = pg.Rect(i * ancho_frame, 0, ancho_frame, alto)
            frame_surface.blit(sprite_sheet, (0, 0), area)

            # Escalar al tamaño deseado
            frame_escalado = pg.transform.scale(frame_surface, (tamano, tamano))
            animacion.append(frame_escalado)

        return animacion

    except Exception as e:
        print(f"No se pudo cargar sprite sheet explosion.png: {e}")

    # PRIORIDAD 2: Intentar cargar frames individuales (explosion_0.png, explosion_1.png, etc.)
    for i in range(frames):
        try:
            frame = cargar_imagen(f'explosion_{i}.png', tamano, tamano)
            animacion.append(frame)
        except:
            if i == 0:
                # PRIORIDAD 3: Intentar cargar explosion.gif
                try:
                    imagen = cargar_imagen('explosion.gif', tamano, tamano)
                    animacion.append(imagen)
                except:
                    # ÚLTIMO RECURSO: Crear placeholder naranja
                    print("Advertencia: No se encontró imagen de explosión, usando placeholder")
                    superficie = pg.Surface((tamano, tamano), pg.SRCALPHA)
                    pg.draw.circle(superficie, (255, 128, 0), (tamano//2, tamano//2), tamano//2)
                    animacion.append(superficie)
            break

    # Si solo hay una imagen, duplicarla para todos los frames
    if len(animacion) == 1:
        animacion = animacion * frames

    return animacion
