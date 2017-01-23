from pygame import init as py_init, quit as py_quit
from pygame import display as pantalla, event
from azoe.engine import EventHandler
from azoe.widgets import NamedValue
from entidad import Entidad
from sys import exit

py_init()
fondo = pantalla.set_mode((400, 400))
event.set_blocked([12, 13])
entity = Entidad()

initiative = NamedValue('Iniciativa')
initiative.rect.top = entity.caracteristicas['DES'].name.rect.bottom + 2
entity.iniciativa.valor.rect.topleft = initiative.rect.right + 2, initiative.rect.top

EventHandler.add_widget(initiative)
EventHandler.add_widget(entity.iniciativa.valor)
EventHandler.add_widget(entity.caracteristicas['DES'].name)
EventHandler.add_widget(entity.caracteristicas['DES'].punt)
EventHandler.add_widget(entity.caracteristicas['DES'].mod)

EventHandler.currentFocus = entity.caracteristicas['DES'].punt


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
