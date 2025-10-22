# 📚 Clase: Sonidos y Retroalimentación Visual Básica con Pygame
## Guía Completa de Aprendizaje

---

# 🎯 INICIO DE CLASE

## Activación de Conocimientos Previos

### Preguntas Orientadoras

**1. ¿Qué papel juegan los sonidos en la experiencia de un videojuego?**

Los sonidos son fundamentales porque:
- **Proporcionan retroalimentación inmediata** de las acciones del jugador
- **Crean inmersión** y atmósfera en el juego
- **Refuerzan eventos importantes** (explosiones, victorias, derrotas)
- **Mejoran la satisfacción** al realizar acciones
- **Comunican información** sin necesidad de texto

**Ejemplo en nuestro proyecto:**
- Cuando disparas → Escuchas un "pew" (retroalimentación inmediata)
- Cuando destruyes un enemigo → Escuchas una explosión (refuerzo del logro)
- Durante todo el juego → Música de fondo (inmersión)

**2. ¿Cómo mejora la retroalimentación visual la interacción con un programa?**

La retroalimentación visual mejora porque:
- **Comunica el estado actual** del sistema (vidas, puntos)
- **Indica consecuencias** de las acciones del usuario
- **Guía al usuario** sobre qué hacer a continuación
- **Previene errores** mostrando información clara
- **Aumenta la confianza** del usuario al ver respuestas a sus acciones

**Ejemplo en nuestro proyecto:**
- HUD muestra vidas y puntos → Sabes tu estado actual
- Enemigo desaparece al dispararle → Consecuencia visible de tu acción
- "Presiona R para reiniciar" → Guía clara sobre qué hacer
- Jugador desaparece al recibir daño → Indicación visual de invulnerabilidad

---

# 📖 DESARROLLO DE CLASE

## Módulo 1: Sistema de Audio con pygame.mixer

### 1.1 Introducción al Módulo pygame.mixer

**¿Qué es pygame.mixer?**

`pygame.mixer` es un módulo de Pygame que permite:
- Reproducir archivos de audio
- Controlar música de fondo
- Reproducir efectos de sonido
- Ajustar volumen y pausar/reanudar audio

**Arquitectura de pygame.mixer:**

```
pygame.mixer
    ├── mixer.init()          → Inicializa el sistema de audio
    ├── mixer.Sound()         → Maneja efectos de sonido cortos
    └── mixer.music           → Maneja música de fondo larga
```

---

### 1.2 Inicialización del Sistema de Sonido

**Pregunta Kahoot #1: ¿Qué función se debe llamar PRIMERO?**

**Respuesta: `pygame.mixer.init()`**

**¿Por qué?**

Antes de reproducir cualquier sonido, debes inicializar el subsistema de audio de pygame. Es como encender el equipo de sonido antes de insertar un CD.

**Código en el proyecto:**

```python
# archivo: audio.py - línea 15

def inicializar_mixer():
    """
    Inicializa el sistema de audio de pygame.
    Debe llamarse antes de cargar cualquier sonido.
    """
    pg.mixer.init()
```

**Uso en principal.py:**

```python
# archivo: principal.py - línea 30-31

# NUEVO: Inicializar sistema de audio
inicializar_mixer()
```

**⚠️ ¿Qué pasa si NO inicializas mixer?**

```python
# ❌ ERROR - No funcionará
sonido = pg.mixer.Sound('disparo.mp3')
sonido.play()
# pygame.error: mixer system not initialized

# ✅ CORRECTO
pg.mixer.init()  # Primero inicializar
sonido = pg.mixer.Sound('disparo.mp3')
sonido.play()  # Ahora sí funciona
```

---

### 1.3 Tipos de Audio: Sound vs Music

**Pregunta Kahoot #2: ¿Cuál es la diferencia?**

**Respuesta: Sound es para efectos cortos, music es para música de fondo**

#### Comparación Detallada:

| Característica | pygame.mixer.Sound | pygame.mixer.music |
|----------------|-------------------|-------------------|
| **Uso** | Efectos de sonido cortos | Música de fondo larga |
| **Duración** | < 5 segundos | Minutos/horas |
| **Carga** | En memoria RAM | Stream desde disco |
| **Simultáneos** | Múltiples a la vez | Solo 1 a la vez |
| **Ejemplo** | Disparo, explosión, salto | Música de nivel, menu |

**Código en el proyecto:**

```python
# archivo: audio.py - líneas 28-33

sonidos = {
    'musica_fondo': 'musica_fondo.mp3',  # → music
    'disparo': cargar_efecto('disparo.mp3'),  # → Sound
    'explosion': cargar_efecto('explosion.mp3'),  # → Sound
    'danio': cargar_efecto('danio.mp3'),  # → Sound
}
```

**¿Por qué esta distinción?**

**pygame.mixer.Sound:**
- Carga todo el archivo en memoria
- Rápido de reproducir (sin retraso)
- Ideal para efectos que se repiten mucho
- Permite reproducir varios a la vez

```python
# Puedes disparar muchas veces rápido
disparo1.play()  # 🔫
disparo2.play()  # 🔫
disparo3.play()  # 🔫
# ¡Los 3 suenan simultáneamente!
```

**pygame.mixer.music:**
- Lee el archivo poco a poco (streaming)
- Ahorra memoria RAM
- Solo puedes tener 1 música a la vez
- Perfecto para archivos largos

```python
# Solo 1 música de fondo
pg.mixer.music.load('nivel1.mp3')
pg.mixer.music.play(-1)  # Loop infinito
```

---

### 1.4 Formatos de Audio Compatibles

**Pregunta Kahoot #3: ¿Qué formato usamos en el proyecto?**

**Respuesta: MP3**

**Formatos soportados por pygame.mixer:**

| Formato | Extensión | Ventajas | Desventajas |
|---------|-----------|----------|-------------|
| **WAV** | .wav | Sin compresión, máxima calidad | Archivos muy grandes |
| **MP3** | .mp3 | Comprimido, archivos pequeños | Requiere codecs extra |
| **OGG** | .ogg | Comprimido, código abierto | Menos común |

**¿Por qué elegimos MP3?**

1. **Tamaño pequeño** - Ahorra espacio en disco
2. **Fácil de encontrar** - Mayoría de sitios ofrecen MP3
3. **Compatible** - Funciona en todos los sistemas
4. **Balance** - Buena calidad con poco tamaño

**Código en el proyecto:**

```python
# archivo: audio.py - líneas 28-33

sonidos = {
    'disparo': cargar_efecto('disparo.mp3'),      # ← .mp3
    'explosion': cargar_efecto('explosion.mp3'),  # ← .mp3
    'danio': cargar_efecto('danio.mp3'),          # ← .mp3
}
```

**Estructura de archivos:**

```
audios/
    ├── musica_fondo.mp3  (3.2 MB)  ← Música larga
    ├── disparo.mp3       (15 KB)   ← Efecto corto
    ├── explosion.mp3     (42 KB)   ← Efecto medio
    ├── danio.mp3         (28 KB)   ← Efecto corto
    ├── game_over.mp3     (65 KB)   ← Efecto medio
    └── reinicio.mp3      (38 KB)   ← Efecto corto
```

---

### 1.5 Carga de Archivos de Audio

**Dos métodos diferentes:**

#### Método 1: Cargar Efectos de Sonido (Sound)

```python
# archivo: audio.py - líneas 42-60

def cargar_efecto(nombre_archivo):
    """
    Carga un efecto de sonido desde la carpeta de audios.

    Args:
        nombre_archivo (str): Nombre del archivo (ej: 'disparo.mp3')

    Returns:
        pg.mixer.Sound: Objeto de sonido cargado
    """
    ruta = os.path.join(CARPETA_AUDIOS, nombre_archivo)
    try:
        return pg.mixer.Sound(ruta)  # ← Carga en memoria RAM
    except:
        print(f"Advertencia: No se pudo cargar '{ruta}'")
        # Crear sonido vacío como fallback
        return pg.mixer.Sound(buffer=b'\x00' * 1000)
```

**¿Qué hace este código?**

1. **Construye la ruta completa** - `audios/disparo.mp3`
2. **Intenta cargar** - `pg.mixer.Sound(ruta)`
3. **Si falla** - Crea sonido silencioso (no rompe el juego)

#### Método 2: Cargar Música de Fondo (music)

```python
# archivo: audio.py - líneas 63-77

def reproducir_musica_fondo(ruta_musica, volumen=0.3, loop=True):
    """
    Reproduce música de fondo en loop.

    Args:
        ruta_musica (str): Ruta del archivo de música
        volumen (float): Volumen de 0.0 a 1.0
        loop (bool): Si True, loop infinito
    """
    try:
        pg.mixer.music.load(ruta_musica)  # ← Prepara para streaming
        pg.mixer.music.set_volume(volumen)
        if loop:
            pg.mixer.music.play(-1)  # -1 = loop infinito
        else:
            pg.mixer.music.play()
    except:
        print(f"Advertencia: No se pudo cargar '{ruta_musica}'")
```

---

### 1.6 Reproducción de Sonidos: play(), stop(), set_volume()

**Pregunta Kahoot #4: ¿Qué parámetro hace loop infinito?**

**Respuesta: `-1`**

#### Método .play()

**Para Sound:**

```python
# Sintaxis básica
sonido.play()

# Con parámetros
sonido.play(
    loops=0,      # 0 = 1 vez, 1 = 2 veces, -1 = infinito
    maxtime=0,    # Tiempo máximo en milisegundos
    fade_ms=0     # Fade in en milisegundos
)
```

**Ejemplos:**

```python
# Reproducir una vez
disparo.play()

# Repetir 3 veces
explosion.play(loops=2)  # loops=2 → reproduce 3 veces total

# Loop infinito con fade
musica.play(loops=-1, fade_ms=2000)  # Entra suavemente en 2 seg
```

**Para music:**

```python
# Pregunta Kahoot #4
pg.mixer.music.play(-1)  # ← Loop infinito
```

**¿Por qué -1?**

En pygame, `-1` es una convención que significa "infinito":
- `0` → Reproduce 1 vez
- `1` → Reproduce 2 veces
- `2` → Reproduce 3 veces
- `-1` → Reproduce infinitamente ♾️

**Código en el proyecto:**

```python
# archivo: principal.py - línea 40

reproducir_musica_fondo(sonidos['musica_fondo'], volumen=0.3)

# Internamente llama a:
pg.mixer.music.play(-1)  # Loop infinito
```

#### Método .stop()

```python
# Detener un efecto
sonido.stop()

# Detener la música
pg.mixer.music.stop()
```

**Código en el proyecto:**

```python
# archivo: audio.py - línea 80-84

def detener_musica():
    """Detiene la música de fondo."""
    pg.mixer.music.stop()
```

#### Método .set_volume()

**Pregunta Kahoot #5: ¿Qué rango de valores acepta?**

**Respuesta: 0.0 a 1.0**

```python
# Volumen al 50%
sonido.set_volume(0.5)

# Volumen al máximo
sonido.set_volume(1.0)

# Silencio
sonido.set_volume(0.0)

# ❌ ERROR - Fuera de rango
sonido.set_volume(150)  # No funciona, debe ser 0.0-1.0
```

**¿Por qué 0.0 a 1.0 y no 0 a 100?**

Es una convención en programación:
- **0.0** = 0% (matemáticamente es multiplicar por 0)
- **0.5** = 50% (multiplicar por 0.5)
- **1.0** = 100% (multiplicar por 1)

**Código en el proyecto:**

```python
# archivo: audio.py - líneas 87-95

def reproducir_efecto(sonido, volumen=0.5):
    """
    Reproduce un efecto de sonido.

    Args:
        sonido (pg.mixer.Sound): Objeto de sonido
        volumen (float): Volumen de 0.0 a 1.0
    """
    if sonido:
        sonido.set_volume(volumen)  # ← Ajusta volumen
        sonido.play()
```

**Volúmenes configurados en el proyecto:**

```python
# eventos.py - línea 73
reproducir_efecto(estado['sonidos']['disparo'], volumen=0.4)  # 40%

# actualizacion.py - línea 70
reproducir_efecto(estado['sonidos']['explosion'], volumen=0.5)  # 50%

# actualizacion.py - línea 115
reproducir_efecto(estado['sonidos']['danio'], volumen=0.6)  # 60%

# actualizacion.py - línea 106
reproducir_efecto(estado['sonidos']['game_over'], volumen=0.7)  # 70%
```

**¿Por qué volúmenes diferentes?**

- **Disparo (40%)** - Se repite mucho, volumen bajo previene saturación
- **Explosión (50%)** - Balance entre audible e importante
- **Daño (60%)** - Más alto para alertar al jugador
- **Game Over (70%)** - El más alto, evento muy importante

---

### 1.7 Práctica: Sistema de Audio Completo

**Flujo completo de carga y reproducción:**

```python
# 1. INICIALIZACIÓN (1 sola vez al inicio)
pg.mixer.init()

# 2. CARGAR SONIDOS (1 sola vez al inicio)
disparo = pg.mixer.Sound('audios/disparo.mp3')
musica = 'audios/musica_fondo.mp3'

# 3. CONFIGURAR MÚSICA (1 sola vez al inicio)
pg.mixer.music.load(musica)
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)  # Comienza loop infinito

# 4. REPRODUCIR EFECTOS (cada vez que se necesite)
# En el bucle del juego:
if evento.key == pg.K_SPACE:
    disparo.set_volume(0.4)
    disparo.play()  # ¡Pew! 🔫
```

**Código en el proyecto (archivo principal.py):**

```python
# Línea 30-31: Paso 1
inicializar_mixer()

# Línea 37: Paso 2
sonidos = cargar_sonidos()

# Línea 40: Paso 3
reproducir_musica_fondo(sonidos['musica_fondo'], volumen=0.3)

# Estado del juego:
estado['sonidos'] = sonidos

# Línea 48-49 (bucle del juego): Paso 4
# Los efectos se reproducen cuando ocurren eventos
```

---

## Módulo 2: Retroalimentación Visual

### 2.1 Sincronización Audio-Visual

**Pregunta Kahoot #6: ¿Cuántos eventos sincronizados hay?**

**Respuesta: 6 eventos**

**Tabla completa de sincronización:**

| # | Acción del Usuario | Retroalimentación Visual | Retroalimentación Auditiva | Ubicación en Código |
|---|-------------------|-------------------------|---------------------------|---------------------|
| 1 | Presiona ESPACIO | Aparece proyectil | `disparo.mp3` (40%) | eventos.py:72-73 |
| 2 | Proyectil destruye enemigo | Enemigo desaparece + explosión animada + +10 puntos | `explosion.mp3` (50%) | actualizacion.py:65-74 |
| 3 | Enemigo golpea jugador | Jugador desaparece 2 seg + explosión + -1 vida | `danio.mp3` (60%) | actualizacion.py:114-126 |
| 4 | Vidas = 0 | Overlay oscuro + "GAME OVER" rojo + puntuación final | `game_over.mp3` (70%) | actualizacion.py:105-106 |
| 5 | Presiona R (Game Over) | Pantalla se reinicia + todos los elementos vuelven | `reinicio.mp3` (60%) | eventos.py:34-35 |
| 6 | Juego inicia | Elementos aparecen + HUD visible | `musica_fondo.mp3` (30% loop) | principal.py:40 |

**¿Por qué es importante la sincronización?**

1. **Coherencia** - El jugador espera ver Y escuchar cuando hace algo
2. **Inmersión** - Los sentidos trabajan juntos
3. **Claridad** - Doble confirmación de que algo pasó
4. **Satisfacción** - Ver y escuchar el impacto refuerza la sensación de logro

**Ejemplo de sincronización perfecta:**

```python
# archivo: actualizacion.py - líneas 60-74

# Enemigo destruido
enemigos.remove(enemigo)          # 1. Desaparece visualmente
enemigos_destruidos += 1
estado['puntos'] += 10            # 2. Puntos aumentan (HUD)

# Reproducir sonido
reproducir_efecto(
    estado['sonidos']['explosion'],
    volumen=0.5                   # 3. Sonido de explosión
)

# Crear explosión visual
crear_explosion(                   # 4. Animación de explosión
    estado,
    enemigo.centerx,
    enemigo.centery
)
```

**Resultado para el jugador:**
1. Ve que el enemigo desaparece ✅
2. Ve que ganó 10 puntos ✅
3. Escucha la explosión ✅
4. Ve la animación de explosión ✅

**¡4 tipos de retroalimentación simultáneas!**

---

### 2.2 Cambios de Color en Respuesta a Eventos

**Teoría del color en UI/UX:**

| Color | Significado | Uso en el Proyecto |
|-------|-------------|-------------------|
| **Blanco** | Neutral, información | Texto del HUD (vidas, puntos) |
| **Rojo** | Peligro, error, fin | "GAME OVER" |
| **Verde** | Éxito, correcto | (No usado) |
| **Amarillo** | Advertencia | (No usado) |

**Pregunta Kahoot #10: ¿Qué color se usa para "GAME OVER"?**

**Respuesta: Rojo**

**Código en el proyecto:**

```python
# archivo: renderizado.py - línea 85-86

# HUD normal - BLANCO
texto_vidas = FUENTE_HUD.render(
    f"Vidas: {estado['vidas']}",
    True,
    (255, 255, 255)  # ← RGB = Blanco
)
```

```python
# archivo: renderizado.py - línea 108

# Game Over - ROJO
texto_game_over = FUENTE_GAME_OVER.render(
    "GAME OVER",
    True,
    (255, 0, 0)  # ← RGB = Rojo brillante
)
```

**¿Por qué estos colores?**

**Blanco para HUD:**
- **Neutral** - No distrae del juego
- **Legible** - Contrasta con fondo oscuro
- **Estándar** - Convención en videojuegos

**Rojo para Game Over:**
- **Alarma** - Color de peligro universal
- **Atención** - Imposible de ignorar
- **Emoción** - Transmite urgencia/fin

**Psicología del color en acción:**

```python
# Imagina estos dos escenarios:

# Escenario A: Game Over en blanco
texto = FUENTE.render("GAME OVER", True, (255, 255, 255))
# Reacción: "Oh, supongo que perdí" 😐

# Escenario B: Game Over en rojo
texto = FUENTE.render("GAME OVER", True, (255, 0, 0))
# Reacción: "¡NOOO! ¡PERDÍ!" 😱

# El color ROJO genera más emoción
```

---

### 2.3 Texto en Pantalla con pygame.font

**Pregunta Kahoot #7: ¿Qué función renderiza texto?**

**Respuesta: `font.render()`**

**Proceso completo de mostrar texto:**

```python
# PASO 1: Inicializar el sistema de fuentes
pg.font.init()

# PASO 2: Crear un objeto fuente
fuente = pg.font.Font(None, 36)  # None = fuente por defecto, 36 = tamaño

# PASO 3: Renderizar texto a superficie
superficie_texto = fuente.render(
    "Hola Mundo",       # Texto a mostrar
    True,               # Antialiasing (True = suave, False = pixelado)
    (255, 255, 255)     # Color RGB
)

# PASO 4: Dibujar en ventana
ventana.blit(superficie_texto, (x, y))  # Posición
```

**Código en el proyecto:**

```python
# archivo: renderizado.py - líneas 11-13

# PASO 1: Inicializar (1 vez al inicio del módulo)
pg.font.init()

# PASO 2: Crear fuentes (1 vez al inicio)
FUENTE_HUD = pg.font.Font(None, 36)        # Tamaño 36 para HUD
FUENTE_GAME_OVER = pg.font.Font(None, 72) # Tamaño 72 para Game Over
```

```python
# archivo: renderizado.py - líneas 85-90

# PASO 3 y 4: Renderizar y dibujar (cada frame)
def dibujar_hud(ventana, estado):
    # Texto de vidas
    texto_vidas = FUENTE_HUD.render(
        f"Vidas: {estado['vidas']}",  # ← Texto dinámico
        True,                          # ← Antialiasing
        (255, 255, 255)                # ← Color blanco
    )
    ventana.blit(texto_vidas, (10, 10))  # ← Posición (10, 10)

    # Texto de puntos
    texto_puntos = FUENTE_HUD.render(
        f"Puntos: {estado['puntos']}",
        True,
        (255, 255, 255)
    )
    ventana.blit(texto_puntos, (10, 50))  # ← Posición (10, 50)
```

**¿Qué es antialiasing?**

Antialiasing suaviza los bordes del texto:

```
SIN antialiasing (False):          CON antialiasing (True):
█████                              ░███▓
█   █                              ▓█ ░█░
█████                              ░███▓
█                                  ▓█
█                                  ░█

Bordes duros, pixelados           Bordes suaves, profesionales
```

**Siempre usa `True` para texto legible.**

**Pregunta Kahoot Bonus 2: ¿Qué muestra el HUD?**

**Respuesta: Vidas y puntos**

**Mensajes en el proyecto:**

| Mensaje | Fuente | Tamaño | Color | Ubicación |
|---------|--------|--------|-------|-----------|
| "Vidas: 3" | HUD | 36px | Blanco | (10, 10) |
| "Puntos: 50" | HUD | 36px | Blanco | (10, 50) |
| "GAME OVER" | Game Over | 72px | Rojo | Centro |
| "Puntuacion Final: 50" | HUD | 36px | Blanco | Centro+20 |
| "Presiona R para reiniciar" | HUD | 36px | Blanco | Centro+70 |

---

### 2.4 Elementos Visuales Dinámicos: pygame.draw y Superficies

**Uso de Superficies con Transparencia:**

```python
# Crear superficie
superficie = pg.Surface((ancho, alto))

# Establecer transparencia
superficie.set_alpha(valor)  # 0-255

# Rellenar con color
superficie.fill((R, G, B))

# Dibujar en ventana
ventana.blit(superficie, (x, y))
```

**Pregunta Kahoot #8: ¿Qué método establece transparencia?**

**Respuesta: `surface.set_alpha()`**

**Valores de transparencia:**

```python
superficie.set_alpha(0)     # Invisible (0%)
superficie.set_alpha(64)    # Muy transparente (25%)
superficie.set_alpha(128)   # Semi-transparente (50%)
superficie.set_alpha(192)   # Poco transparente (75%)
superficie.set_alpha(255)   # Opaco (100%)
```

**Código en el proyecto:**

```python
# archivo: renderizado.py - líneas 102-105

# Crear overlay oscuro de Game Over
overlay = pg.Surface(ventana.get_size())  # Mismo tamaño que ventana
overlay.set_alpha(128)                     # 50% transparente
overlay.fill((0, 0, 0))                    # Negro
ventana.blit(overlay, (0, 0))              # Cubrir toda la pantalla
```

**Efecto visual:**

```
ANTES del overlay:              DESPUÉS del overlay:
┌─────────────────┐            ┌─────────────────┐
│   🚀            │            │░░░🚀░░░░░░░░░░░│  ← Todo más oscuro
│        👾  👾   │     →      │░░░░░░░👾░░👾░░░│
│     ▪▪▪         │            │░░░░░▪▪▪░░░░░░░░│
│                 │            │░░░░░░░░░░░░░░░░│
│ Vidas: 0        │            │░Vidas: 0░░░░░░░│
│ GAME OVER       │            │░GAME OVER░░░░░░│  ← Texto destaca más
└─────────────────┘            └─────────────────┘
```

**¿Por qué usar overlay?**

1. **Enfoque** - Oscurece elementos no importantes
2. **Legibilidad** - Texto "GAME OVER" destaca más
3. **Drama** - Sensación de "fin"
4. **Usabilidad** - Jugador sabe que el juego pausó

**Rectángulos colisionables (pygame.Rect):**

Aunque no dibujamos rectángulos visibles, los usamos para:

```python
# Crear rectángulo (área de colisión)
rect = pg.Rect(x, y, ancho, alto)

# Detectar colisión
if rect1.colliderect(rect2):
    print("¡Colisión!")
```

**En el proyecto:**

```python
# variables.py - línea 41
jugador = pg.Rect(0, 0, TAMANO_JUGADOR, TAMANO_JUGADOR)

# eventos.py - línea 63
proyectil = pg.Rect(
    jugador.centerx - TAMANO_PROYECTIL_ANCHO // 2,
    jugador.y,
    TAMANO_PROYECTIL_ANCHO,
    TAMANO_PROYECTIL_ALTO
)

# actualizacion.py - línea 47
if proyectil.colliderect(enemigo):  # ← Detección de colisión
    # ¡Explosión!
```

---

### 2.5 Animaciones Simples

**Tipos de animación implementados:**

#### 1. Movimiento (Cambio de Posición)

```python
# Proyectil moviéndose hacia arriba
proyectil.y -= velocidad  # Cada frame, Y disminuye

# Enemigo moviéndose hacia abajo
enemigo.y += velocidad    # Cada frame, Y aumenta
```

**Código:**

```python
# actualizacion.py - línea 18
proyectil.y -= vel

# enemigo.py - línea 43
enemigo.y += vel
```

**Efecto visual:**

```
Frame 1:  Frame 2:  Frame 3:
  ▪         ▪         ▪       ← Proyectil sube

 👾                            ← Enemigo baja
           👾
                    👾
```

#### 2. Aparición/Desaparición (Cambio de Transparencia)

```python
# Jugador visible
if estado['jugador_visible']:
    ventana.blit(imagen_jugador, (x, y))
else:
    # No se dibuja = invisible
    pass
```

**Código:**

```python
# renderizado.py - líneas 24-26
if estado['jugador_visible']:
    jugador = estado['jugador']
    ventana.blit(recursos['jugador'], (jugador.x, jugador.y))
```

**Efecto visual (invulnerabilidad):**

```
Colisión → Jugador desaparece → 2 segundos → Jugador reaparece

t=0s:     t=0.5s:   t=1.0s:   t=1.5s:   t=2.0s:
 🚀        (vacío)   (vacío)   (vacío)    🚀
👾                                        👾
```

#### 3. Animación por Frames (Sprite Sheet)

**Pregunta Kahoot #9: ¿Cuántos frames tiene la explosión?**

**Respuesta: 8 frames**

```python
# Cambiar frame según tiempo transcurrido
progreso = tiempo_transcurrido / DURACION_TOTAL
frame_actual = int(progreso * FRAMES_EXPLOSION)

# Dibujar frame correspondiente
ventana.blit(animacion[frame_actual], (x, y))
```

**Código:**

```python
# actualizacion.py - líneas 170-171
progreso = tiempo_transcurrido / DURACION_EXPLOSION
explosion['frame_actual'] = min(int(progreso * FRAMES_EXPLOSION), FRAMES_EXPLOSION - 1)
```

**Efecto visual (explosión de 8 frames en 600ms):**

```
Frame: 0     1     2     3     4     5     6     7
Tiempo: 0ms  75ms  150ms 225ms 300ms 375ms 450ms 525ms
Visual: 💥    💥    💥    💥    💥    💥    💥    💥
       amarillo→naranja→marrón→disperso
       pequeño → grande → partículas
```

**Cálculo del frame:**

```python
# Ejemplo: Han pasado 300ms de 600ms totales
tiempo_transcurrido = 300
DURACION_EXPLOSION = 600
FRAMES_EXPLOSION = 8

progreso = 300 / 600 = 0.5        # 50% completado
frame = 0.5 * 8 = 4.0              # Frame 4
frame = min(4, 7) = 4              # Asegurar que no pase de 7

# Resultado: Mostrar frame 4 (mitad de la explosión)
```

---

## Módulo 3: Implementación Práctica

### 3.1 Estructura Modular del Proyecto

**Pregunta Kahoot Bonus 1: ¿En qué archivo está `reproducir_musica_fondo()`?**

**Respuesta: audio.py**

**Arquitectura del proyecto:**

```
Módulos del Proyecto:
├── principal.py        → Orquestador (llama a todos)
├── audio.py           → Sistema de audio ✅ AQUÍ
├── variables.py       → Configuración y estado
├── eventos.py         → Input del usuario
├── movimientos.py     → Física del jugador
├── enemigo.py         → IA de enemigos
├── actualizacion.py   → Lógica del juego
├── renderizado.py     → Gráficos y HUD
├── recursos.py        → Carga de assets
└── init_pygame.py     → Inicialización base
```

**Separación de responsabilidades:**

```python
# ❌ MAL - Todo mezclado en principal.py
def bucle_juego():
    sonido = pg.mixer.Sound('disparo.mp3')
    sonido.play()
    fuente = pg.font.Font(None, 36)
    texto = fuente.render("Vidas: 3", True, (255,255,255))
    # ... 500 líneas más ...

# ✅ BIEN - Modular
# En principal.py:
reproducir_efecto(sonidos['disparo'])  # ← Delega a audio.py
dibujar_hud(ventana, estado)           # ← Delega a renderizado.py
```

**Ventajas de la modularización:**

1. **Mantenibilidad** - Cambios en audio solo afectan audio.py
2. **Legibilidad** - Cada archivo tiene un propósito claro
3. **Reutilización** - Puedes usar audio.py en otro proyecto
4. **Testing** - Puedes probar cada módulo independientemente
5. **Colaboración** - Varios programadores trabajan sin conflictos

---

### 3.2 Sistema Completo de Explosiones

**Flujo completo desde colisión hasta animación:**

```
PASO 1: Colisión detectada
    ↓
PASO 2: Crear objeto explosión
    ↓
PASO 3: Agregar a lista de explosiones
    ↓
PASO 4: Cada frame actualizar explosiones
    ↓
PASO 5: Calcular frame actual según tiempo
    ↓
PASO 6: Renderizar frame correspondiente
    ↓
PASO 7: Eliminar cuando termine (600ms)
```

**PASO 1: Detectar colisión**

```python
# actualizacion.py - líneas 47-53
if proyectil.colliderect(enemigo):
    # ... marcar para eliminar ...
    # Guardar posición para explosión
    posiciones_explosiones.append((enemigo.centerx, enemigo.centery))
```

**PASO 2: Crear explosión**

```python
# actualizacion.py - líneas 133-151
def crear_explosion(estado, x, y):
    tiempo_actual = pg.time.get_ticks()

    explosion = {
        'x': x,                      # Posición X
        'y': y,                      # Posición Y
        'tiempo_inicio': tiempo_actual,  # Cuándo empezó
        'frame_actual': 0            # Frame inicial
    }

    estado['explosiones'].append(explosion)  # Agregar a lista
```

**PASO 3: Ya incluido en PASO 2** (línea append)

**PASO 4: Actualizar cada frame**

```python
# principal.py - línea 68
actualizar_explosiones(estado['explosiones'])
```

**PASO 5: Calcular frame actual**

```python
# actualizacion.py - líneas 166-171
for explosion in explosiones:
    tiempo_transcurrido = tiempo_actual - explosion['tiempo_inicio']

    # Calcular progreso (0.0 a 1.0)
    progreso = tiempo_transcurrido / DURACION_EXPLOSION

    # Convertir a número de frame (0 a 7)
    explosion['frame_actual'] = min(
        int(progreso * FRAMES_EXPLOSION),  # Calcular frame
        FRAMES_EXPLOSION - 1               # Máximo frame 7
    )
```

**PASO 6: Renderizar**

```python
# renderizado.py - líneas 90-99
for explosion in explosiones:
    # Obtener frame correcto de la animación
    frame = animacion_explosion[explosion['frame_actual']]

    # Calcular posición (centrado)
    x = explosion['x'] - TAMANO_EXPLOSION // 2
    y = explosion['y'] - TAMANO_EXPLOSION // 2

    # Dibujar
    ventana.blit(frame, (x, y))
```

**PASO 7: Eliminar completadas**

```python
# actualizacion.py - líneas 173-179
if tiempo_transcurrido >= DURACION_EXPLOSION:
    explosiones_a_eliminar.append(explosion)

for explosion in explosiones_a_eliminar:
    if explosion in explosiones:
        explosiones.remove(explosion)
```

**Ejemplo completo de una explosión:**

```
t=0ms:    Colisión detectada
          crear_explosion(estado, 400, 300)
          explosiones = [{'x': 400, 'y': 300, 'tiempo_inicio': 5000, 'frame_actual': 0}]

t=75ms:   Actualizar: progreso = 75/600 = 0.125
          frame_actual = 0.125 * 8 = 1
          Renderizar: frame 1 en (400, 300)

t=150ms:  frame_actual = 2, renderizar frame 2

t=225ms:  frame_actual = 3, renderizar frame 3

t=300ms:  frame_actual = 4, renderizar frame 4

t=375ms:  frame_actual = 5, renderizar frame 5

t=450ms:  frame_actual = 6, renderizar frame 6

t=525ms:  frame_actual = 7, renderizar frame 7

t=600ms:  tiempo_transcurrido >= 600
          Eliminar explosión
          explosiones = []
```

---

### 3.3 Configuración y Personalización

**Variables configurables:**

```python
# variables.py - líneas 34-36

# Explosiones
TAMANO_EXPLOSION = 64      # Tamaño en píxeles
DURACION_EXPLOSION = 600   # Duración en milisegundos
FRAMES_EXPLOSION = 8       # Número de frames

# Audio (volúmenes)
# eventos.py:73
VOLUMEN_DISPARO = 0.4

# actualizacion.py:70
VOLUMEN_EXPLOSION = 0.5

# actualizacion.py:115
VOLUMEN_DANIO = 0.6

# actualizacion.py:106
VOLUMEN_GAME_OVER = 0.7
```

**Ejercicio de personalización:**

```python
# Hacer explosiones más lentas y grandes:
TAMANO_EXPLOSION = 100      # Era 64
DURACION_EXPLOSION = 1000   # Era 600

# Hacer música más silenciosa:
reproducir_musica_fondo(sonidos['musica_fondo'], volumen=0.1)  # Era 0.3

# Hacer disparo más ruidoso:
reproducir_efecto(sonido, volumen=0.8)  # Era 0.4
```

---

# 🎓 CIERRE DE CLASE

## Resumen de Conceptos Aprendidos

### Checklist de Conocimientos Adquiridos

**pygame.mixer (Sistema de Audio):**
- ✅ Entiendo qué es pygame.mixer y para qué sirve
- ✅ Sé inicializar el sistema con `pg.mixer.init()`
- ✅ Conozco la diferencia entre Sound y music
- ✅ Puedo cargar archivos MP3
- ✅ Sé reproducir sonidos con `.play()`
- ✅ Puedo controlar volumen con `.set_volume(0.0 a 1.0)`
- ✅ Entiendo cómo hacer loop infinito con `-1`

**Retroalimentación Visual:**
- ✅ Sé usar pygame.font para mostrar texto
- ✅ Entiendo el método `.render()` y sus parámetros
- ✅ Puedo crear superficies con transparencia usando `.set_alpha()`
- ✅ Conozco la importancia del color en la UI (blanco/rojo)
- ✅ Sé crear animaciones simples (movimiento, aparición, frames)

**Sincronización Audio-Visual:**
- ✅ Entiendo cómo sincronizar sonidos con eventos visuales
- ✅ Puedo implementar 6 tipos de eventos sincronizados
- ✅ Sé cuándo usar qué volumen según la importancia del evento

**Arquitectura de Código:**
- ✅ Comprendo la importancia de la modularización
- ✅ Sé separar responsabilidades en diferentes archivos
- ✅ Puedo organizar assets en carpetas (audios/, imagenes/)

---

## Ejercicio Práctico Final

**Desarrolla una interacción simple donde un clic produzca sonido y cambio visual:**

```python
import pygame as pg

# Inicialización
pg.init()
pg.mixer.init()
ventana = pg.display.set_mode((400, 300))
pg.display.set_caption("Ejercicio Final")

# Recursos
sonido_clic = pg.mixer.Sound('clic.mp3')
fuente = pg.font.Font(None, 48)
color_fondo = (0, 0, 0)  # Negro inicial

# Bucle principal
corriendo = True
while corriendo:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False

        if evento.type == pg.MOUSEBUTTONDOWN:
            # ¡SINCRONIZACIÓN AUDIO-VISUAL!

            # Audio
            sonido_clic.play()

            # Visual
            color_fondo = (255, 0, 0)  # Cambiar a rojo

    # Renderizado
    ventana.fill(color_fondo)

    texto = fuente.render("¡Haz clic!", True, (255, 255, 255))
    ventana.blit(texto, (100, 125))

    pg.display.flip()
    pg.time.Clock().tick(60)

pg.quit()
```

**Desafío extendido:**

Modifica el ejercicio para:
1. Que el color vuelva a negro después de 500ms
2. Que muestre cuántos clics has hecho
3. Que reproduzca un sonido diferente cada 10 clics
4. Que agregue una animación de círculo expandiéndose

---

## Evaluación de Aprendizaje

### Quiz de Autoevaluación (Respuestas al final)

1. ¿Cuál es el primer paso para usar audio en pygame?
2. ¿Qué diferencia hay entre Sound y music?
3. ¿Qué significa el parámetro `-1` en `play(-1)`?
4. ¿Qué rango de valores acepta `set_volume()`?
5. ¿Qué función renderiza texto a superficie?
6. ¿Para qué sirve `set_alpha()`?
7. ¿Cuántos eventos sincronizados implementamos?
8. ¿Por qué usamos color rojo para "GAME OVER"?
9. ¿Cuántos frames tiene nuestra animación de explosión?
10. ¿En qué archivo está la función `reproducir_musica_fondo()`?

**Respuestas:**
1. `pg.mixer.init()`
2. Sound = efectos cortos, music = música larga
3. Loop infinito
4. 0.0 a 1.0
5. `font.render()`
6. Establecer transparencia (0-255)
7. 6 eventos
8. Color de alarma/peligro universalmente reconocido
9. 8 frames
10. audio.py

---

## Recursos Adicionales

### Para Practicar Más:

**Sitios de Audio Gratuito:**
- [Freesound.org](https://freesound.org) - Miles de efectos de sonido
- [Pixabay](https://pixabay.com/sound-effects) - Audio libre de derechos
- [Mixkit](https://mixkit.co/free-sound-effects) - Efectos de gaming

**Sitios de Sprites:**
- [OpenGameArt.org](https://opengameart.org) - Arte para juegos
- [Kenney.nl](https://kenney.nl) - Packs completos gratuitos
- [Itch.io](https://itch.io/game-assets/free) - Assets de la comunidad

**Documentación Oficial:**
- [pygame.mixer](https://www.pygame.org/docs/ref/mixer.html)
- [pygame.font](https://www.pygame.org/docs/ref/font.html)
- [pygame.Surface](https://www.pygame.org/docs/ref/surface.html)

### Próximos Pasos:

**Nivel 1 (Principiante):**
- ✅ Has completado: Audio básico y retroalimentación visual
- ➡️ Siguiente: Menús interactivos
- ➡️ Después: Sistema de partículas

**Nivel 2 (Intermedio):**
- Música adaptativa (cambia según eventos)
- Animaciones con tweening (interpolación suave)
- Sistema de diálogos con texto

**Nivel 3 (Avanzado):**
- Audio posicional 3D
- Shaders para efectos visuales
- Sistema de cinemáticas

---

## Reflexión Final

**Preguntas para reflexionar:**

1. **¿Cómo mejoró la experiencia del juego al agregar sonidos?**
   - Antes: Silencio, difícil saber si disparaste
   - Después: Cada acción tiene confirmación audible

2. **¿Por qué es importante la sincronización audio-visual?**
   - Los humanos procesamos vista y oído juntos
   - Inconsistencias crean confusión
   - Sincronización = sensación de "solidez"

3. **¿Qué aprendiste sobre diseño de UI con colores?**
   - Colores no son decorativos, comunican información
   - Rojo = peligro es universal
   - Consistencia de colores ayuda al aprendizaje

4. **¿Cómo te ayudó la modularización del código?**
   - Fácil encontrar dónde está cada funcionalidad
   - Cambios no rompen otras partes
   - Código reutilizable

---

## Proyecto Final Sugerido

**Crea tu propio "Space Shooter" con:**

**Requisitos mínimos:**
- ✅ 3+ efectos de sonido sincronizados
- ✅ Música de fondo en loop
- ✅ HUD con al menos 2 datos (ej: vidas, puntos)
- ✅ 1 animación (sprite sheet o frame-by-frame)
- ✅ Uso de colores para comunicar estados
- ✅ Código modularizado (mínimo 3 archivos)

**Ideas para destacar:**
- Sistema de power-ups con sonido único
- Enemigos de diferentes tipos con animaciones
- Pantalla de victoria con música celebratoria
- Efectos de partículas para explosiones mejoradas
- Sistema de niveles con música diferente

---

## ¡Felicidades! 🎉

Has completado exitosamente la clase de **Sonidos y Retroalimentación Visual Básica**.

Ahora puedes:
- ✅ Implementar sistemas de audio profesionales
- ✅ Crear interfaces con retroalimentación clara
- ✅ Sincronizar audio y visual perfectamente
- ✅ Escribir código modular y mantenible

**¡Sigue practicando y creando juegos increíbles!** 🎮🚀

---

**Última actualización:** Clase 2025 - Videojuegos 3ros
**Instructor:** [Tu nombre]
**Contacto:** [Tu email/Discord]

**Repositorio del proyecto:** [Link a GitHub si aplica]

---

