from pygame import init as py_init, quit as py_quit
from pygame import display as pantalla, event, mouse
from pygame import QUIT, KEYDOWN, MOUSEBUTTONDOWN, MOUSEMOTION
from pygame import K_ESCAPE
from sys import exit

from value import Value


py_init()
fondo = pantalla.set_mode((400, 400))


def salir():
    py_quit()
    exit()

valor = Value(12, (200, 200))

while True:
    fondo.fill((255, 255, 255))
    events = event.get()
    for e in events:
        if e.type == QUIT:
            salir()
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                salir()
        elif e.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            if valor.rect.collidepoint(pos):
                valor.on_mouse_down(e.button)

        elif e.type == MOUSEMOTION:
            pos = mouse.get_pos()
            if valor.rect.collidepoint(pos):
                valor.on_mouse_in()
            else:
                valor.on_mouse_out()

    valor.update()
    fondo.blit(valor.image, valor.rect)
    pantalla.flip()
