import pygame as pg

# Inicialización
pg.init()
pg.mixer.init()
ventana = pg.display.set_mode((400, 300))
pg.display.set_caption("Ejercicio Final")

# Recursos
sonido_clic = pg.mixer.Sound('audios/musica_fondo.mp3')
sonido_clic.set_volume(0.7)  # Ajustar volumen
fuente = pg.font.Font(None, 48)

# Variables
color_fondo = (0, 0, 0)
clics = 0
reloj = pg.time.Clock()

# Bucle principal
corriendo = True
while corriendo:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False

        if evento.type == pg.MOUSEBUTTONDOWN:
            # Audio
            sonido_clic.play()
            
            # Visual - cambiar entre negro y rojo
            if color_fondo == (0, 0, 0):
                color_fondo = (255, 0, 0)
            else:
                color_fondo = (0, 0, 0)
            
            # Contador
            clics += 1

    # Renderizado
    ventana.fill(color_fondo)
    texto = fuente.render(f"¡Haz clic! ({clics})", True, (255, 255, 255))
    ventana.blit(texto, (80, 125))
    
    pg.display.flip()
    reloj.tick(60)

pg.quit()