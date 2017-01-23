from azoe.widgets import Value


class LinkedValue:
    valor = 0

    def __init__(self, parent, nombre):
        self.parent = parent
        self.nombre = nombre
        self.valor = Value(self, self.parent.value, self.parent.show_sign)

    def update(self):
        self.valor.set_value(self.parent.value)
