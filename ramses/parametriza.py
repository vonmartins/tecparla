#! /usr/bin/env python3

import soundfile as sf
import numpy as np 
from tqdm import tqdm
from ramses.util import * 
from ramses.prm import *

def parametriza(dirPrm, dirSen, *guiSen):
    """
    Lee las señales indicadas por 'dirSen', 'guiSen' y 'extSen', y escribe la señal
    parametrizada en el directorio 'dirPrm'.
    En la versión trivial, la señal parametrizada es igual a la señal temporal.
    """
    for nomSen in tqdm(leeLis(*guiSen), ascii="·|/-\\#"):
        pathSen = pathName(dirSen, nomSen, "wav")
        sen, fm = sf.read(pathSen)

        prm = np.array(sen)
        
        pathPrm = pathName(dirPrm, nomSen, ".prm")
        chkPathName(pathPrm)
        escrPrm(pathPrm, prm)

if __name__ == "__main__": 
    from docopt import docopt

    usage= """
        Parametriza una base de datos de señales de voz.

        usage: 
            parametriza.py [options] <guia> ...
            parametriza.py -h | --help 
            parametriza.py --version

        options: 
            -s DIRECTORI, --dirSen DIRECTORI  directori de la señal d'entrada [default: .]
            -p DIRECTORI, --dirPrm DIRECTORI  directori de la señal parametritzada [default: .]
        """ 
    args= docopt(usage, version= "tecparla2025") # diccionario
    dirSen = args["--dirSen"]
    dirPrm = args["--dirPrm"]
    guiSen = args["<guia>"] # lista de cadenas
    parametriza(dirPrm, dirSen, *guiSen) 
