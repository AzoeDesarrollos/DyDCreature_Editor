from pygame import init as py_init, quit as py_quit
from pygame import display as pantalla, event
from azoe.engine import EventHandler
from entidad import Entidad
from sys import exit

py_init()
fondo = pantalla.set_mode((400, 400))
event.set_blocked([12, 13])
entity = Entidad()

EventHandler.add_widget(entity.caracteristicas['FUE'].name)
EventHandler.add_widget(entity.caracteristicas['FUE'].punt)
EventHandler.add_widget(entity.caracteristicas['FUE'].mod)

EventHandler.currentFocus = entity.caracteristicas['FUE'].punt

hayCambios = True
while hayCambios:
    fondo.fill((255, 255, 255))
    entity.update()
    events = event.get()
    hayCambios = EventHandler.update(events, fondo)

    if hayCambios:
        pantalla.update(hayCambios)

py_quit()
exit()
