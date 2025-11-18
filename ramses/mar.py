import re

# reLBO = r"LBO:(\s*\d*\s*,){3}(?P<trn>\w+)"
reLBO = re.compile(r'LBO:(\s*\d*[.]?\d*,){3}(?P<trn>\w+)') # LBO -> Contenido ortográfico

def cogeTrn(ficMar):
    """
        Devuelve el contenido del cuarto campo de la primera etiqueta LBO presente en el
        fichero de Marcas 'ficMar'.
    """
    # hay que leer el fichero ficMar
    with open(ficMar, "rt") as fpMar: 
        for linea in fpMar:
            # match = re.match(reLBO, linea)

            if (match := reLBO.match(linea)):
                return match['trn']
            # if (lbo := reLBO.match(linea)): return lbo['trn']
