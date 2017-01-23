from azoe.engine import Resources

RAZAS = None
CLASES = None
IDIOMAS = None
ESCUELAS = None
CONJUROS = None
HABS = None
DOTES = None
ARMAS = None
ARMDS = None
APTS = None
DOMINIOS = None
OBJMAG = None
CHARS = None
ALINI = None
TAM = None


def load_language(lang):
    root = 'database/' + lang + '/'
    global CHARS, RAZAS, TAM, CLASES, ALINI, IDIOMAS, HABS, DOTES, ESCUELAS, DOMINIOS, CONJUROS, ARMAS, ARMDS, OBJMAG
    CHARS = Resources.abrir_json(root + 'basicos' + ".json")['caracteristicas']
    TAM = Resources.abrir_json(root + 'basicos' + ".json")['tamanios']
    ALINI = Resources.abrir_json(root + 'basicos' + ".json")['alineamientos']
    RAZAS = Resources.abrir_json(root + 'razas' + ".json")
    CLASES = Resources.abrir_json(root + 'clases' + ".json")
    IDIOMAS = Resources.abrir_json(root + 'idiomas' + ".json")
    HABS = Resources.abrir_json(root + 'habilidades' + ".json")
    DOTES = Resources.abrir_json(root + 'dotes' + ".json")
    ESCUELAS = Resources.abrir_json(root + 'escuelas' + ".json")
    DOMINIOS = Resources.abrir_json(root + 'dominios' + ".json")
    CONJUROS = Resources.abrir_json(root + 'conjuros' + ".json")
    ARMAS = Resources.abrir_json(root + 'armas' + ".json")
    ARMDS = Resources.abrir_json(root + 'armaduras' + ".json")
    OBJMAG = Resources.abrir_json(root + 'objetos_magicos' + ".json")

lengua = Resources.abrir_json('config.json')['lengua']
load_language(lengua)

__all__ = "CHARS,RAZAS,TAM,CLASES,ALINI,IDIOMAS,HABS,DOTES,ESCUELAS,DOMINIOS,CONJUROS,ARMAS,ARMDS,OBJMAG".split(',')
