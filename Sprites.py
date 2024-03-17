import pygame

pygame.init()

def recortar_imagen(imagen_principal, coordenada_X, coordenada_Y, ancho, alto):
    return imagen_principal.subsurface(pygame.Rect(coordenada_X, coordenada_Y, ancho, alto))

class Personaje(pygame.sprite.Sprite):
    def __init__(self, nombre, objeto_spritesheets, coordenadas, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad
        self.velocidad_fotograma = 0.3

        self.sprite_sheets = objeto_spritesheets
        self.imagenes_animacion = self.sprite_sheets["correr_abajo"]

        self.indice_imagen = 0

        self.ejecutar_animacion = False

        self.imagen = self.imagenes_animacion[self.indice_imagen]

        self.rect = self.imagen.get_rect()
        self.rect.x = coordenadas[0]
        self.rect.y = coordenadas[1]

    def update(self, ventana_juego):
        eventos = pygame.key.get_pressed()

        #mover el personaje hacia la izquierda
        if eventos[pygame.K_LEFT]:
            self.ejecutar_animacion = True
            self.rect.move_ip(-self.velocidad, 0)
            self.imagenes_animacion = self.sprite_sheets["correr_izquierda"]
            self.draw(ventana_juego)

        #mover el personaje hacia la derecha
        elif eventos[pygame.K_RIGHT]:
            self.ejecutar_animacion = True
            self.rect.move_ip(self.velocidad, 0)
            self.imagenes_animacion = self.sprite_sheets["correr_derecha"]
            self.draw(ventana_juego)
        #mover el personaje hacia arriba
        elif eventos[pygame.K_UP]:
            self.ejecutar_animacion = True
            self.rect.move_ip(0, -self.velocidad)
            self.imagenes_animacion = self.sprite_sheets["correr_arriba"]
            self.draw(ventana_juego)

        #mover el personaje hacia abajo
        elif eventos[pygame.K_DOWN]:
            self.ejecutar_animacion = True
            self.rect.move_ip(0, self.velocidad)
            self.imagenes_animacion = self.sprite_sheets["correr_abajo"]
            self.draw(ventana_juego)
        else:
            self.ejecutar_animacion = False

        if self.ejecutar_animacion == False:
            ventana_juego.blit(self.sprite_sheets["correr_abajo"][0], self.rect)

    def draw(self,ventana_juego):

        if self.indice_imagen >= 3:
            self.indice_imagen = 0

        self.imagen = self.imagenes_animacion[int(self.indice_imagen)]

        ventana_juego.blit(self.imagen, self.rect)

        self.indice_imagen += self.velocidad_fotograma


hoja_sprites = pygame.transform.scale(pygame.image.load("assets_villa/personaje.png"), (100, 200))

cordenada_y_de_corte = 0

sprites = {
    "correr_arriba": [],
    "correr_abajo": [],
    "correr_izquierda": [],
    "correr_derecha": []
}

nombres_de_animaciones = ["correr_abajo", "correr_arriba", "correr_izquierda", "correr_derecha"]

indice_animacion = 0
#recorta la hoja de sprites original en partes que contengan los sprites de cada animacion del personaje
for hojas_sprites in range(0, 4):
    sprite = recortar_imagen(hoja_sprites, 0, cordenada_y_de_corte, 100, 50)

    #cad vez que se ejecuta el bucle se actualiza la posicion para recortar en horizontal
    cordenada_x_de_recorte= 0

    #recorta cada imagen individualmente que esta en esa hoja de sprites 
    for _ in range(0, 4):
        sprites2 = recortar_imagen(sprite, cordenada_x_de_recorte, 0, 25, 50)

        cordenada_x_de_recorte += 25

        #agrega cada imagen independiente a una lista la cual se guarda a su vez en un objeto sprites
        sprites[nombres_de_animaciones[indice_animacion]].append(sprites2)

    indice_animacion += 1

    cordenada_y_de_corte += 50

