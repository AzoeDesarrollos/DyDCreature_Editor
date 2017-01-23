from azoe.widgets import Value, NamedValue


class Caracteristica:
    _mod = 0

    def __init__(self, parent, nombre, valor):
        self.parent = parent
        self.nombre = nombre
        self.name = NamedValue(nombre)
        self.valor = Value(self, valor)
        self._mod = Value(self, self.obtener_mod(), show_sign=True)

        self.valor.rect.left = self.name.rect.right + 8
        self._mod.rect.left = self.valor.rect.right + 15

    def obtener_mod(self):
        n = self.valor.get_value()
        if n % 2 == 0:
            mod = (n-10)//2
        else:
            mod = (n-11)//2

        return mod

    @property
    def punt(self):
        return self.valor

    @property
    def mod(self):
        return self._mod

    @punt.setter
    def punt(self, value):
        self.valor.set_value(value)
        self.mod.set_value(self.obtener_mod())

    @punt.deleter
    def punt(self):
        self.valor.set_value(0)
        self.mod.set_value(self.obtener_mod())

    def update(self):
        self.mod.set_value(self.obtener_mod())
