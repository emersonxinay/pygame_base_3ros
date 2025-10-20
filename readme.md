# Código base videojuego 
## ARCHIVO: init_pygame.py

```py
# ============================================================================
# ARCHIVO: init_pygame.py
# ============================================================================
"""
Módulo de inicialización de Pygame.
Configura la ventana principal y los componentes básicos del sistema.
"""
import pygame


def inicializar_pygame():
    """
    Inicializa todos los módulos de pygame necesarios para el funcionamiento del juego.
    
    Returns:
        pygame.time.Clock: Objeto reloj para controlar la tasa de fotogramas.
    """
    pygame.init()
    reloj = pygame.time.Clock()
    return reloj


def crear_ventana(ancho, alto, titulo):
    """
    Crea y configura la ventana principal del juego.
    
    Args:
        ancho (int): Ancho de la ventana en píxeles.
        alto (int): Alto de la ventana en píxeles.
        titulo (str): Título que se mostrará en la barra de la ventana.
    
    Returns:
        pygame.Surface: Superficie de la ventana principal.
    """
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(titulo)
    return ventana


def establecer_icono(ruta_icono):
    """
    Establece el ícono de la ventana del juego.
    
    Args:
        ruta_icono (str): Ruta del archivo de imagen para el ícono.
    """
    icono = pygame.image.load(ruta_icono)
    pygame.display.set_icon(icono)

```
## ARCHIVO: recursos.py

```py
# ============================================================================
# ARCHIVO: recursos.py
# ============================================================================
"""
Módulo de gestión de recursos.
Carga y prepara todos los recursos gráficos del juego.
"""
import pygame


def cargar_imagen(ruta, ancho, alto):
    """
    Carga una imagen desde el disco y la escala al tamaño especificado.
    
    Args:
        ruta (str): Ruta del archivo de imagen.
        ancho (int): Ancho deseado en píxeles.
        alto (int): Alto deseado en píxeles.
    
    Returns:
        pygame.Surface: Imagen cargada y escalada.
    """
    imagen = pygame.image.load(ruta)
    imagen = pygame.transform.scale(imagen, (ancho, alto))
    return imagen


def cargar_recursos():
    """
    Carga todos los recursos gráficos necesarios para el juego.
    
    Returns:
        dict: Diccionario con todas las imágenes cargadas, indexadas por nombre.
    """
    recursos = {
        'fondo': cargar_imagen("fondo.png", 800, 600),
        'jugador': cargar_imagen("jugador.png", 40, 40),
        'proyectil': cargar_imagen("proyectil.png", 10, 20),
        'enemigo': cargar_imagen("enemigo.png", 50, 50)
    }
    return recursos

```
## ARCHIVO: variables.py

```py
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

```
## ARCHIVO: eventos.py

```py
# ============================================================================
# ARCHIVO: eventos.py
# ============================================================================
"""
Módulo de procesamiento de eventos.
Gestiona la entrada del usuario y eventos del sistema.
"""
import pygame


def procesar_eventos(estado):
    """
    Procesa los eventos del juego, incluyendo el cierre de ventana y la creación de proyectiles.
    
    Args:
        estado (dict): Diccionario con el estado actual del juego.
    
    Returns:
        bool: True si el juego debe continuar, False si debe cerrarse.
    """
    evento = pygame.event.poll()
    
    if evento.type == pygame.QUIT:
        return False
    
    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
        crear_proyectil(estado)
    
    return True


def crear_proyectil(estado):
    """
    Crea un nuevo proyectil en la posición del jugador.
    
    Args:
        estado (dict): Diccionario con el estado actual del juego.
    """
    from variables import VELOCIDAD_PROYECTIL, TAMANO_PROYECTIL_ANCHO, TAMANO_PROYECTIL_ALTO
    
    jugador = estado['jugador']
    proyectiles = estado['proyectiles']
    
    proyectil = pygame.Rect(
        jugador.centerx - TAMANO_PROYECTIL_ANCHO // 2,
        jugador.y,
        TAMANO_PROYECTIL_ANCHO,
        TAMANO_PROYECTIL_ALTO
    )
    proyectiles.append((proyectil, VELOCIDAD_PROYECTIL))

```
## ARCHIVO: movimientos.py

```py
# ============================================================================
# ARCHIVO: movimientos.py
# ============================================================================
"""
Módulo de control de movimiento del jugador.
Gestiona el desplazamiento del jugador y los límites de la pantalla.
"""
import pygame
from variables import VELOCIDAD_JUGADOR, ANCHO_VENTANA, ALTO_VENTANA


def actualizar_movimiento_jugador(jugador):
    """
    Actualiza la posición del jugador basándose en las teclas presionadas.
    Mantiene al jugador dentro de los límites de la ventana.
    
    Args:
        jugador (pygame.Rect): Rectángulo que representa al jugador.
    """
    teclas = pygame.key.get_pressed()
    
    # Aplicar movimiento según teclas presionadas
    if teclas[pygame.K_LEFT]:
        jugador.x -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_RIGHT]:
        jugador.x += VELOCIDAD_JUGADOR
    if teclas[pygame.K_UP]:
        jugador.y -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_DOWN]:
        jugador.y += VELOCIDAD_JUGADOR
    
    # Aplicar límites de la ventana
    aplicar_limites_ventana(jugador)


def aplicar_limites_ventana(jugador):
    """
    Restringe la posición del jugador para que no salga de los límites de la ventana.
    
    Args:
        jugador (pygame.Rect): Rectángulo que representa al jugador.
    """
    jugador.x = max(0, min(jugador.x, ANCHO_VENTANA - jugador.width))
    jugador.y = max(0, min(jugador.y, ALTO_VENTANA - jugador.height))

```
## ARCHIVO: enemigo.py
```py
# ============================================================================
# ARCHIVO: enemigo.py
# ============================================================================
"""
Módulo de gestión de enemigos.
Controla la generación, actualización y movimiento de enemigos.
"""
import pygame
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
    tiempo_actual = pygame.time.get_ticks()
    
    if tiempo_actual - estado['ultimo_enemigo'] > INTERVALO_GENERACION_ENEMIGO:
        x_enemigo = random.randint(0, ANCHO_VENTANA - TAMANO_ENEMIGO - 10)
        enemigo = pygame.Rect(x_enemigo, -40, TAMANO_ENEMIGO, TAMANO_ENEMIGO)
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

```
## ARCHIVO: actualizacion.py

```py
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

```
## ARCHIVO: renderizado.py

```py
# ============================================================================
# ARCHIVO: renderizado.py
# ============================================================================
"""
Módulo de renderizado gráfico.
Gestiona el dibujado de todos los elementos visuales del juego.
"""
import pygame


def renderizar_juego(ventana, recursos, estado):
    """
    Dibuja todos los elementos del juego en la ventana.
    
    Args:
        ventana (pygame.Surface): Superficie de la ventana donde se dibujará.
        recursos (dict): Diccionario con todos los recursos gráficos.
        estado (dict): Diccionario con el estado actual del juego.
    """
    # Dibujar fondo
    ventana.blit(recursos['fondo'], (0, 0))
    
    # Dibujar jugador
    jugador = estado['jugador']
    ventana.blit(recursos['jugador'], (jugador.x, jugador.y))
    
    # Dibujar proyectiles
    dibujar_proyectiles(ventana, recursos['proyectil'], estado['proyectiles'])
    
    # Dibujar enemigos
    dibujar_enemigos(ventana, recursos['enemigo'], estado['enemigos'])
    
    # Actualizar pantalla
    pygame.display.flip()


def dibujar_proyectiles(ventana, imagen_proyectil, proyectiles):
    """
    Dibuja todos los proyectiles activos en la ventana.
    
    Args:
        ventana (pygame.Surface): Superficie donde se dibujará.
        imagen_proyectil (pygame.Surface): Imagen del proyectil.
        proyectiles (list): Lista de tuplas (proyectil, velocidad).
    """
    for proyectil, _ in proyectiles:
        ventana.blit(imagen_proyectil, (proyectil.x, proyectil.y))


def dibujar_enemigos(ventana, imagen_enemigo, enemigos):
    """
    Dibuja todos los enemigos activos en la ventana.
    
    Args:
        ventana (pygame.Surface): Superficie donde se dibujará.
        imagen_enemigo (pygame.Surface): Imagen del enemigo.
        enemigos (list): Lista de tuplas (enemigo, velocidad).
    """
    for enemigo, _ in enemigos:
        ventana.blit(imagen_enemigo, (enemigo.x, enemigo.y))

```
## ARCHIVO: principal.py

```py
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

```