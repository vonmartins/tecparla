#! /usr/bin/env python3

import numpy as np
from ramses.util import *
from ramses.prm import *
from ramses.mar import *

def entrena(dirPrm, dirMar, lisUni, ficMod,*ficGui):
    unidades = leeLis(lisUni)

    # inicializamos el modelo
    modelo = {}

    # inicializamos el entrenamiento
    total = {unidad : 0 for unidad in unidades}
    numUni = {unidad : 0 for unidad in unidades}

    # bucle para todas las señales del entrenamiento
    for señal in leeLis(*ficGui):
        # leemos la señal y el contenido del fichero de marcas
        pathPrm = pathName(dirPrm, señal, 'prm')
        prm = leePrm(pathPrm)
        pathMar = pathName(dirMar, señal, 'mar')
        unidad = cogeTrn(pathMar)

        # actualizamos la información del entrenamiento
        total[unidad] += prm
        numUni[unidad] += 1
    
    # recalculamos el modelo
    for unidad in unidades:
        modelo[unidad] = total[unidad]/numUni[unidad]
    
    # escribimos el modelo resultante
    chkPathName(ficMod)
    with open(ficMod, 'wb') as fpMod:
        np.save(fpMod, modelo)
        
