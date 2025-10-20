# ============================================================================
# FUNCIONES COMPLETAS CORREGIDAS - LISTAS PARA COPIAR Y PEGAR
# ============================================================================
# Copia cada función completa y reemplaza la versión anterior en tu código
# ============================================================================

```py
# ============================================================================
# ARCHIVO: eventos.py
# ============================================================================

# FUNCIÓN 1: procesar_eventos (REEMPLAZAR LA EXISTENTE)
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
    
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_SPACE and estado['vivo']:
            crear_proyectil(estado)
        elif evento.key == pygame.K_r and not estado['vivo']:
            reiniciar_juego(estado)
    
    return True


# FUNCIÓN 2: reiniciar_juego (AGREGAR AL FINAL DEL ARCHIVO)
def reiniciar_juego(estado):
    """
    Reinicia el estado del juego a sus valores iniciales.
    
    Args:
        estado (dict): Diccionario con el estado actual del juego.
    """
    from variables import TAMANO_JUGADOR
    
    estado['jugador'] = pygame.Rect(0, 0, TAMANO_JUGADOR, TAMANO_JUGADOR)
    estado['proyectiles'] = []
    estado['enemigos'] = []
    estado['ultimo_enemigo'] = pygame.time.get_ticks()
    estado['vivo'] = True

```
```py
# ============================================================================
# ARCHIVO: variables.py
# ============================================================================

# FUNCIÓN: inicializar_variables (REEMPLAZAR LA EXISTENTE)
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
        'correr': True,
        'vivo': True
    }
    
    return estado

```
```py
# ============================================================================
# ARCHIVO: enemigo.py
# ============================================================================

# FUNCIÓN: generar_enemigo (REEMPLAZAR LA EXISTENTE)
def generar_enemigo(estado):
    """
    Genera un nuevo enemigo en una posición aleatoria superior si ha pasado el intervalo establecido.
    
    Args:
        estado (dict): Diccionario con el estado actual del juego.
    """
    if not estado['vivo']:
        return
    
    tiempo_actual = pygame.time.get_ticks()
    
    if tiempo_actual - estado['ultimo_enemigo'] > INTERVALO_GENERACION_ENEMIGO:
        x_enemigo = random.randint(0, ANCHO_VENTANA - TAMANO_ENEMIGO - 10)
        enemigo = pygame.Rect(x_enemigo, -40, TAMANO_ENEMIGO, TAMANO_ENEMIGO)
        estado['enemigos'].append((enemigo, VELOCIDAD_ENEMIGO))
        estado['ultimo_enemigo'] = tiempo_actual


```
```py

# ============================================================================
# ARCHIVO: movimientos.py (OPCIONAL)
# ============================================================================

# FUNCIÓN: actualizar_movimiento_jugador (REEMPLAZAR LA EXISTENTE)
def actualizar_movimiento_jugador(jugador, vivo):
    """
    Actualiza la posición del jugador basándose en las teclas presionadas.
    Mantiene al jugador dentro de los límites de la ventana.
    
    Args:
        jugador (pygame.Rect): Rectángulo que representa al jugador.
        vivo (bool): Indica si el jugador está vivo.
    """
    if not vivo:
        return
    
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

```
```py

# ============================================================================
# ARCHIVO: actualizacion.py
# ============================================================================

# FUNCIÓN: detectar_colision_jugador_enemigo (AGREGAR AL FINAL DEL ARCHIVO)
def detectar_colision_jugador_enemigo(jugador, enemigos, estado):
    """
    Detecta colisiones entre el jugador y los enemigos.
    Si hay colisión, el jugador muere.
    
    Args:
        jugador (pygame.Rect): Rectángulo que representa al jugador.
        enemigos (list): Lista de tuplas (enemigo, velocidad).
        estado (dict): Diccionario con el estado actual del juego.
    """
    if not estado['vivo']:
        return
    
    for enemigo, _ in enemigos:
        if jugador.colliderect(enemigo):
            estado['vivo'] = False
            return

```
```py

# ============================================================================
# ARCHIVO: renderizado.py
# ============================================================================

# FUNCIÓN: renderizar_juego (REEMPLAZAR LA EXISTENTE)
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
    
    # Dibujar jugador solo si está vivo
    if estado['vivo']:
        jugador = estado['jugador']
        ventana.blit(recursos['jugador'], (jugador.x, jugador.y))
    
    # Dibujar proyectiles
    dibujar_proyectiles(ventana, recursos['proyectil'], estado['proyectiles'])
    
    # Dibujar enemigos
    dibujar_enemigos(ventana, recursos['enemigo'], estado['enemigos'])
    
    # Actualizar pantalla
    pygame.display.flip()

```
```py
# ============================================================================
# ARCHIVO: principal.py
# ============================================================================

# CAMBIO 1: IMPORTS (BUSCAR LA LÍNEA Y REEMPLAZARLA)
# ANTES:
# from actualizacion import actualizar_proyectiles, detectar_colisiones

# DESPUÉS:
from actualizacion import actualizar_proyectiles, detectar_colisiones, detectar_colision_jugador_enemigo


# CAMBIO 2: FUNCIÓN ejecutar_juego - BUCLE PRINCIPAL (REEMPLAZAR EL BUCLE COMPLETO)
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
        actualizar_movimiento_jugador(estado['jugador'], estado['vivo'])
        
        # Generar y actualizar enemigos
        generar_enemigo(estado)
        actualizar_enemigos(estado['enemigos'])
        
        # Actualizar proyectiles
        actualizar_proyectiles(estado['proyectiles'])
        
        # Detectar colisiones
        detectar_colisiones(estado['proyectiles'], estado['enemigos'])
        detectar_colision_jugador_enemigo(estado['jugador'], estado['enemigos'], estado)
        
        # Renderizar todo
        renderizar_juego(ventana, recursos, estado)
        
        # Controlar velocidad de fotogramas
        reloj.tick(FPS)
    
    # Finalizar pygame
    pygame.quit()

```
