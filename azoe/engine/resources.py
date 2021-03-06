from pygame import image, Rect
import json


class Resources:
    @staticmethod
    def abrir_json(archivo):
        ex = open(archivo, 'r')
        data = json.load(ex)
        ex.close()
        return data

    @staticmethod
    def guardar_json(archivo, datos, ordenar=True):
        ex = open(archivo, 'w')
        if ordenar:
            json.dump(datos, ex, sort_keys=True, indent=4, separators=(',', ': '))
        else:
            json.dump(datos, ex)
        ex.close()

    @staticmethod
    def cargar_imagen(ruta):
        return image.load(ruta).convert_alpha()

    @staticmethod
    def guardar_imagen(imagen, ruta):
        image.save(imagen, ruta)

    @classmethod
    def split_spritesheet(cls, ruta, w=32, h=32):
        spritesheet = cls.cargar_imagen(ruta)
        ancho = spritesheet.get_width()
        alto = spritesheet.get_height()
        tamanio = w, h
        sprites = []
        for y in range(int(alto / h)):
            for x in range(int(ancho / w)):
                rect = Rect((int(ancho / (ancho / w)) * x, int(alto / (alto / h)) * y), tamanio)
                sprites.append(spritesheet.subsurface(rect))
        return sprites

    @classmethod
    def cargar_iconos(cls, nombres, ruta, w, h):
        iconos = cls.split_spritesheet(ruta, w, h)
        d, i = {}, -1
        for y in range(4):
            for x in range(6):
                i += 1
                if i <= len(nombres) - 1:
                    d[nombres[i]] = iconos[i]

        return d
