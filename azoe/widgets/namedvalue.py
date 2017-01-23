from .basewidget import BaseWidget
from pygame import font


class NamedValue(BaseWidget):
    def __init__(self, name):
        super().__init__()
        self.nombre = name

        fuente = font.SysFont('verdana', 16, bold=1)
        self.image = fuente.render(name, 1, (0, 0, 0))
        self.rect = self.image.get_rect()

    def update(self):
        self.dirty = 1
