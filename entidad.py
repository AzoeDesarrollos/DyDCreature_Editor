from data import *
from caracteristica import Caracteristica as Caract

class Entidad:
    nombre = ''
    dg = 0
    alineamiento = ''
    tipo = ''
    tamanio = ''
    iniciativa = 0
    velocidad = 0
    ataque_base = 0
    espacio = 0
    alcance = 0
    aptitudes = []
    cualidades = []
    ts_base = [0, 0, 0]
    caracteristicas = {}
    habilidades = {}
    dotes = []
    equipo = {}
    armas = []
    armadura = []
    escudo = []
    ca = 0
    toque = 0
    desprevenido = 0
    dinero = {'ppt': 0, 'po': 0, 'pp': 0, 'pc': 0}

    def __init__(self):
        for i in range(6):
            nombre = CHARS[str(i)]['abr']
            self.caracteristicas[nombre.upper()] = Caract(self, nombre, 0)
        for h in range(len(HABS)):
            self.habilidades[str(h)] = {'rng': 0, 'dts': 0, 'rcl': 0, 'sng': 0, 'obj': 0}

    def update(self):
        for caract in self.caracteristicas:
            self.caracteristicas[caract].update()
