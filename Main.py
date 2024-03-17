from Sprites import *
from Castle_Objects import *
import pygame

pygame.init()

ANCHO_VENTANA, ALTO_VENTANA = 680, 480

VENTANA_PRINCIPAL = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Las aventuras de Juan")

cartero = Personaje(nombre="Juan", objeto_spritesheets=sprites, coordenadas=(100, 250), velocidad=2)

reloj = pygame.time.Clock()

juego_terminado = False
while juego_terminado != True:

    reloj.tick(50)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True

    VENTANA_PRINCIPAL.fill((255, 255, 255))

    #bloque.draw(VENTANA_PRINCIPAL)
    bloques_escenario.draw(VENTANA_PRINCIPAL)

    #cartero.draw(VENTANA_PRINCIPAL)
    cartero.update(VENTANA_PRINCIPAL)

    pygame.display.flip()