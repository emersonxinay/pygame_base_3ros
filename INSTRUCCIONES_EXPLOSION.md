# 💥 Instrucciones para Imágenes de Explosión

El sistema de explosiones está implementado y funciona con **3 opciones**:

## Opción 1: Múltiples Frames (Animación Completa) ⭐ RECOMENDADO

Descarga o crea 4 imágenes de explosión y nómbralas:
- `explosion_0.png` - Frame inicial (más pequeño/brillante)
- `explosion_1.png` - Frame medio
- `explosion_2.png` - Frame avanzado
- `explosion_3.png` - Frame final (más grande/desvanecido)

**Colócalas en:** `imagenes/`

**Sitios para descargar sprites de explosión:**
- [OpenGameArt.org](https://opengameart.org/art-search?keys=explosion) - Búsqueda: "explosion sprite sheet"
- [Itch.io](https://itch.io/game-assets/free/tag-explosion) - Assets gratuitos
- [Kenney.nl](https://kenney.nl/assets?q=explosion) - Packs de sprites gratuitos

**Buscar términos:**
- "explosion sprite sheet"
- "2d explosion animation"
- "pixel art explosion"
- "cartoon explosion frames"

## Opción 2: GIF Animado

Si encuentras un GIF de explosión:
1. Descarga el archivo `.gif`
2. Renómbralo a `explosion.gif`
3. Colócalo en: `imagenes/`

**Nota:** Pygame convertirá el primer frame del GIF en una imagen estática.

## Opción 3: Una Sola Imagen

Si solo tienes una imagen de explosión:
1. Descarga cualquier imagen de explosión
2. Renómbrala a `explosion.png`
3. Colócala en: `imagenes/`

El sistema la usará y la repetirá en todos los frames.

## Opción 4: Placeholder Automático (Ya implementado)

Si no agregas ninguna imagen, el sistema creará automáticamente un **círculo naranja** como placeholder.

**Color:** RGB(255, 128, 0) - Naranja
**Tamaño:** 60x60 píxeles

---

## 🎨 Crear tus propias explosiones

### Usando un editor online gratuito:

1. **Piskel** (https://www.piskelapp.com/)
   - Editor de sprites online
   - Crea animaciones frame por frame
   - Exporta como PNG

2. **Photopea** (https://www.photopea.com/)
   - Similar a Photoshop, gratis
   - Edita capas
   - Exporta PNG

### Tutorial rápido con Piskel:

1. Ir a https://www.piskelapp.com/
2. Crear nuevo sprite de 60x60 píxeles
3. Crear 4 frames:
   - Frame 1: Círculo pequeño rojo brillante
   - Frame 2: Círculo mediano naranja
   - Frame 3: Círculo grande amarillo
   - Frame 4: Círculo muy grande gris translúcido
4. Exportar cada frame como PNG
5. Nombrar: `explosion_0.png`, `explosion_1.png`, etc.

---

## ⚙️ Configuración de Explosiones

Si quieres modificar el comportamiento de las explosiones, edita estas constantes en `variables.py`:

```python
# Línea 34-36
TAMANO_EXPLOSION = 60      # Tamaño en píxeles
DURACION_EXPLOSION = 500   # Duración en milisegundos (0.5 seg)
FRAMES_EXPLOSION = 4       # Número de frames
```

---

## 🧪 Prueba del Sistema

El sistema está listo y funcional **SIN NECESIDAD DE IMÁGENES**.

Para probar:
```bash
python principal.py
```

**Explosiones aparecen cuando:**
1. Un proyectil destruye un enemigo
2. Un enemigo colisiona con el jugador

---

## 📝 Notas Técnicas

- **Formato soportado:** PNG (con transparencia), GIF
- **Tamaño recomendado:** 60x60 píxeles por frame
- **Ubicación:** Carpeta `imagenes/`
- **Fallback:** Si no hay imágenes, usa círculo naranja automático

---

**El sistema ya funciona, solo mejorará visualmente si agregas sprites personalizados! 🎉**
