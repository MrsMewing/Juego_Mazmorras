import pygame

pygame.init()

class Bloque(pygame.sprite.Sprite):
    def __init__(self, imagen, coordenadas):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()

        self.rect.x = coordenadas[0]
        self.rect.y = coordenadas[1]

    def draw(self, ventana_juego):
        ventana_juego.blit(self.image, self.rect)

ruta_bloque = "assets_villa/bloques_escenario/tile18.png"

def crear_escenario(imagen, tamaño_escenario, coordenadas_escenario, tamaño_bloques):

    cuadrados_escenario = pygame.sprite.Group()

    coordenada_y_bloque = coordenadas_escenario[1]

    for filas in range(tamaño_escenario[1]):
        coordenada_x_bloque = coordenadas_escenario[0]
        
        for columnas in range(tamaño_escenario[0]):
            cuadrados_escenario.add(Bloque(imagen, [coordenada_x_bloque, coordenada_y_bloque]))

            coordenada_x_bloque += tamaño_bloques[0]

        coordenada_y_bloque += tamaño_bloques[1]

    return cuadrados_escenario

bloques_escenario = crear_escenario(ruta_bloque, [10, 10], [100, 200], [16, 16])

bloque = Bloque(ruta_bloque, [100, 100])

class Habitacion(pygame.sprite.Sprite):
    def __init__(self, tamaño, enemigos, trampas, tesoros = None):
        super().__init__()
        self.tamaño = tamaño
        self.enemigos = enemigos
        self.trampas = trampas
        self.tesoros = tesoros