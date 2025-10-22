# 🎮 Proyecto Pygame - Clase: Sonidos y Retroalimentación Visual Básica

## 📚 Descripción del Proyecto

Juego de naves espaciales desarrollado en Python utilizando Pygame, que implementa sistema de audio con `pygame.mixer` y retroalimentación visual avanzada. El proyecto está completamente modularizado siguiendo buenas prácticas de programación.

---

## 🎯 Objetivos de la Clase

### **Tema:** Sonidos y Retroalimentación Visual Básica

Este proyecto implementa los conceptos fundamentales de la clase:

1. ✅ **Sistema de Audio con pygame.mixer**
2. ✅ **Retroalimentación Visual Dinámica**
3. ✅ **Sincronización Audio-Visual**
4. ✅ **Interfaz de Usuario Interactiva**

---

## 🔊 Implementación de Audio (pygame.mixer)

### **1. Inicialización del Sistema de Sonido**
```python
# audio.py - Línea 15
pg.mixer.init()
```

### **2. Carga de Archivos de Audio**
- **Formatos compatibles implementados:** MP3
- **Módulo responsable:** `audio.py`

```python
# Carga de efectos de sonido con pygame.mixer.Sound()
sonido = pg.mixer.Sound('ruta/archivo.mp3')

# Carga de música de fondo con pygame.mixer.music
pg.mixer.music.load('musica_fondo.mp3')
```

### **3. Efectos de Sonido Implementados**

| Evento | Archivo | Método | Ubicación en Código |
|--------|---------|--------|---------------------|
| **Disparo** | `disparo.mp3` | `Sound.play()` | `eventos.py:72-73` |
| **Explosión (enemigo destruido)** | `explosion.mp3` | `Sound.play()` | `actualizacion.py:65-66` |
| **Daño al jugador** | `danio.mp3` | `Sound.play()` | `actualizacion.py:114-115` |
| **Game Over** | `game_over.mp3` | `Sound.play()` | `actualizacion.py:105-106` |
| **Reinicio** | `reinicio.mp3` | `Sound.play()` | `eventos.py:34-35` |
| **Música de fondo** | `musica_fondo.mp3` | `music.play(-1)` | `principal.py:40` |

### **4. Control de Volumen**
```python
# Cada sonido tiene su volumen configurado con set_volume()
reproducir_efecto(sonido, volumen=0.5)  # Volumen de 0.0 a 1.0
```

### **5. Funciones de Audio Implementadas**
- ✅ `reproducir_musica_fondo()` - Música en loop infinito
- ✅ `reproducir_efecto()` - Efectos de sonido con volumen ajustable
- ✅ `detener_musica()` - Control de música
- ✅ `pausar_musica()` / `reanudar_musica()` - Control avanzado

---

## 🎨 Retroalimentación Visual Implementada

### **1. Cambios de Color en Respuesta a Eventos**

#### **Sistema de Vidas - Código de Colores**
```python
# renderizado.py:85-86
# Texto blanco para información estándar
texto_vidas = FUENTE_HUD.render(f"Vidas: {estado['vidas']}", True, (255, 255, 255))
```

#### **Game Over - Retroalimentación Visual Dramática**
```python
# renderizado.py:108
# Texto rojo para Game Over
texto_game_over = FUENTE_GAME_OVER.render("GAME OVER", True, (255, 0, 0))
```

### **2. Elementos Visuales Dinámicos con pygame.draw**

El juego utiliza `pygame.draw` implícitamente a través de:
- **Rectángulos colisionables** (`pygame.Rect`)
- **Superficies con transparencia** (overlay de Game Over)

```python
# renderizado.py:102-105
# Overlay semi-transparente oscuro al morir
overlay = pg.Surface(ventana.get_size())
overlay.set_alpha(128)  # Transparencia 50%
overlay.fill((0, 0, 0))
```

### **3. Texto en Pantalla con pygame.font**

#### **HUD (Heads-Up Display)**
```python
# renderizado.py:11-13
# Inicialización de fuentes
pg.font.init()
FUENTE_HUD = pg.font.Font(None, 36)
FUENTE_GAME_OVER = pg.font.Font(None, 72)
```

#### **Mensajes Mostrados:**
- ✅ **Vidas restantes** (esquina superior izquierda)
- ✅ **Puntuación actual** (debajo de vidas)
- ✅ **"GAME OVER"** (pantalla completa)
- ✅ **Puntuación final** (al morir)
- ✅ **"Presiona R para reiniciar"** (instrucciones)

### **4. Animaciones Implementadas**

#### **A. Desaparición del Jugador (Transparencia)**
```python
# renderizado.py:24-26
# El jugador desaparece cuando está muerto o invulnerable
if estado['jugador_visible']:
    ventana.blit(recursos['jugador'], (jugador.x, jugador.y))
```

#### **B. Sistema de Invulnerabilidad (Parpadeo Visual)**
```python
# actualizacion.py:87-91
# Invulnerabilidad temporal de 2 segundos tras recibir daño
if estado['invulnerable']:
    tiempo_actual = pg.time.get_ticks()
    if tiempo_actual - estado['tiempo_invulnerabilidad'] > 2000:
        estado['jugador_visible'] = True
```

#### **C. Movimiento Fluido de Proyectiles**
```python
# actualizacion.py:17-18
# Animación de movimiento vertical
proyectil.y -= vel
```

#### **D. Movimiento de Enemigos**
```python
# enemigo.py:43
# Animación de caída de enemigos
enemigo.y += vel
```

---

## 🎪 Sincronización Audio-Visual

### **Eventos Sincronizados Implementados:**

| Acción del Usuario | Retroalimentación Visual | Retroalimentación Auditiva |
|-------------------|-------------------------|---------------------------|
| **Presionar ESPACIO** | Aparece proyectil | Sonido de disparo |
| **Proyectil destruye enemigo** | Enemigo desaparece, +10 puntos | Explosión |
| **Enemigo golpea jugador** | Jugador desaparece 2 seg, -1 vida | Sonido de daño |
| **Vidas = 0** | Overlay oscuro + "GAME OVER" | Música de Game Over |
| **Presionar R** | Pantalla se reinicia | Sonido de reinicio |
| **Juego iniciado** | Elementos aparecen | Música de fondo (loop) |

---

## 📁 Estructura del Proyecto (Modularizada)

```
pygame_base_3ros/
├── audios/                          # 🔊 Recursos de audio
│   ├── musica_fondo.mp3            # Música de fondo en loop
│   ├── disparo.mp3                 # Efecto al disparar
│   ├── explosion.mp3               # Enemigo destruido
│   ├── danio.mp3                   # Jugador recibe daño
│   ├── game_over.mp3               # Fin del juego
│   └── reinicio.mp3                # Reiniciar partida
│
├── imagenes/                        # 🎨 Recursos visuales
│   ├── fondo.png                   # Fondo del juego (800x600)
│   ├── jugador.png                 # Sprite del jugador (40x40)
│   ├── proyectil.png               # Sprite del proyectil (10x20)
│   ├── enemigo.png                 # Sprite del enemigo (50x50)
│   └── icono.png                   # Icono de la ventana
│
├── actualizacion.py                 # ⚙️ Lógica de colisiones y puntos
├── audio.py                         # 🔊 Sistema de audio (pygame.mixer)
├── enemigo.py                       # 👾 Generación y movimiento de enemigos
├── eventos.py                       # ⌨️ Procesamiento de entrada del usuario
├── init_pygame.py                   # 🎬 Inicialización de Pygame
├── movimientos.py                   # 🎮 Control del jugador
├── principal.py                     # 🚀 Bucle principal del juego
├── recursos.py                      # 📦 Carga de imágenes
├── renderizado.py                   # 🖼️ Renderizado y HUD
├── variables.py                     # 📊 Constantes y estado del juego
└── README.md                        # 📖 Este archivo
```

---

## 🎓 Conceptos de la Clase Aplicados

### **1. pygame.mixer para Manejo de Audio**
- ✅ `pygame.mixer.init()` - Inicialización del sistema
- ✅ `pygame.mixer.Sound()` - Carga de efectos de sonido
- ✅ `pygame.mixer.music` - Gestión de música de fondo
- ✅ `.play()`, `.stop()`, `.set_volume()` - Control de reproducción

**Archivos involucrados:** `audio.py`, `principal.py`, `eventos.py`, `actualizacion.py`

### **2. Retroalimentación Visual Básica**
- ✅ **Cambios de color:** Texto blanco (normal), rojo (Game Over)
- ✅ **pygame.draw:** Superficies y overlays con transparencia
- ✅ **pygame.font:** HUD con vidas, puntos y mensajes
- ✅ **Animaciones:** Desaparición, invulnerabilidad, movimiento

**Archivos involucrados:** `renderizado.py`, `actualizacion.py`

### **3. Práctica Guiada Implementada**
- ✅ ~~Programa que reproduce sonido al presionar tecla~~ → **Disparo con ESPACIO**
- ✅ ~~Cambiar color de rectángulo en evento~~ → **Overlay oscuro en Game Over**
- ✅ ~~Mostrar texto de retroalimentación~~ → **HUD completo + mensajes**
- ✅ ~~Sincronización audio-visual~~ → **6 eventos sincronizados**

### **4. Ejercicio Práctico Ampliado**
- ✅ ~~Clic produce sonido y cambio visual~~ → **Sistema completo de eventos**
- ✅ **Extra:** Sistema de vidas, puntos, invulnerabilidad, Game Over

---

## 🚀 Instalación y Ejecución

### **Requisitos:**
```bash
Python 3.7+
pygame 2.0+
```

### **Instalación:**
```bash
# Clonar o descargar el proyecto
cd pygame_base_3ros

# Instalar dependencias
pip install pygame
```

### **Ejecutar:**
```bash
python principal.py
```

---

## 🎮 Controles del Juego

| Tecla | Acción |
|-------|--------|
| **←** | Mover izquierda |
| **→** | Mover derecha |
| **↑** | Mover arriba |
| **↓** | Mover abajo |
| **ESPACIO** | Disparar (🔊 sonido) |
| **R** | Reiniciar juego (🔊 sonido) |

---

## 🎯 Mecánicas del Juego

### **Sistema de Puntuación:**
- ✅ Cada enemigo destruido: **+10 puntos**
- ✅ Puntuación visible en HUD

### **Sistema de Vidas:**
- ✅ Vidas iniciales: **3**
- ✅ Colisión con enemigo: **-1 vida** (🔊 sonido de daño)
- ✅ Invulnerabilidad: **2 segundos** (jugador desaparece)
- ✅ Vidas = 0: **Game Over** (🔊 música especial)

### **Sistema de Audio:**
| Evento | Sonido | Volumen |
|--------|--------|---------|
| Música de fondo | Loop infinito | 30% |
| Disparo | Efecto corto | 40% |
| Explosión | Efecto medio | 50% |
| Daño | Efecto enfático | 60% |
| Reinicio | Efecto positivo | 60% |
| Game Over | Efecto dramático | 70% |

---

## 💡 Características Técnicas

### **Modularización:**
- ✅ **10 módulos** separados por responsabilidad
- ✅ Alias `pg` para pygame (código más limpio)
- ✅ Docstrings en todas las funciones
- ✅ Manejo de errores (archivos faltantes)

### **Optimizaciones:**
- ✅ FPS fijo: **60**
- ✅ Gestión eficiente de listas (proyectiles, enemigos)
- ✅ Recursos cargados una sola vez al inicio

### **Retroalimentación Visual Avanzada:**
- ✅ HUD siempre visible
- ✅ Overlay de Game Over con transparencia
- ✅ Fuentes de diferentes tamaños (36px y 72px)
- ✅ Sistema de visibilidad del jugador

---

## 📝 Preguntas Orientadoras Respondidas

### **¿Qué papel juegan los sonidos en la experiencia de un videojuego?**

**Respuesta implementada en el proyecto:**
- Los sonidos proporcionan **retroalimentación inmediata** de las acciones del jugador
- Crean **inmersión** y atmósfera (música de fondo)
- **Refuerzan eventos** importantes (explosiones, daño, Game Over)
- Mejoran la **satisfacción** al realizar acciones (disparar, destruir enemigos)

**Evidencia en código:**
- 6 efectos de sonido diferentes sincronizados con eventos visuales
- Música de fondo que crea ambiente constante
- Volúmenes ajustados según importancia del evento

### **¿Cómo mejora la retroalimentación visual la interacción con un programa?**

**Respuesta implementada en el proyecto:**
- Proporciona **información clara** del estado del juego (vidas, puntos)
- Indica **consecuencias** de las acciones (enemigo desaparece al ser destruido)
- Comunica **estados temporales** (invulnerabilidad con desaparición)
- Guía al usuario con **instrucciones visuales** ("Presiona R para reiniciar")

**Evidencia en código:**
- HUD con información en tiempo real
- Cambios de color según contexto (blanco/rojo)
- Animaciones de desaparición y movimiento
- Overlay oscuro para enfocar atención en Game Over

---

## 🎨 Recursos Necesarios

### **Archivos de Audio (audios/):**
Descarga desde: [Freesound.org](https://freesound.org), [Pixabay](https://pixabay.com/sound-effects), [Mixkit](https://mixkit.co)

Buscar:
- `laser shoot`, `8-bit shoot` → disparo.mp3
- `small explosion`, `arcade boom` → explosion.mp3
- `hurt`, `damage` → danio.mp3
- `game over`, `defeat` → game_over.mp3
- `power up`, `success` → reinicio.mp3
- `chiptune loop`, `8-bit music` → musica_fondo.mp3

### **Archivos de Imagen (imagenes/):**
- Crear sprites simples o descargar de [OpenGameArt.org](https://opengameart.org)
- Tamaños requeridos especificados en `recursos.py:42-46`

---

## 👨‍💻 Autor

**Proyecto Educativo** - Clase de Videojuegos 3ros
**Tema:** Sonidos y Retroalimentación Visual Básica con Pygame

---

## 📄 Licencia

Este proyecto es de uso educativo libre.

---

## 🔗 Referencias

- [Documentación Pygame](https://www.pygame.org/docs/)
- [pygame.mixer](https://www.pygame.org/docs/ref/mixer.html)
- [pygame.font](https://www.pygame.org/docs/ref/font.html)
- [pygame.Surface](https://www.pygame.org/docs/ref/surface.html)

---

## ✨ Conceptos Clave Demostrados

```python
# 1. Inicialización de audio
pg.mixer.init()

# 2. Carga y reproducción de sonidos
sonido = pg.mixer.Sound('archivo.mp3')
sonido.play()
sonido.set_volume(0.5)

# 3. Música de fondo
pg.mixer.music.load('musica.mp3')
pg.mixer.music.play(-1)  # Loop infinito

# 4. Texto en pantalla
fuente = pg.font.Font(None, 36)
texto = fuente.render("Mensaje", True, (255, 255, 255))
ventana.blit(texto, (x, y))

# 5. Transparencia
superficie = pg.Surface((ancho, alto))
superficie.set_alpha(128)  # 0-255

# 6. Retroalimentación visual condicional
if condicion:
    cambiar_color()
    mostrar_mensaje()
```

---

**¡Proyecto completo y funcional! 🎉**
