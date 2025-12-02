#! /usr/bin/env python3

import numpy as np

from ramses.util import * 
from ramses.prm import * 
from tqdm import tqdm

def reconoce(dirRec, dirPrm, ficMod, *guiSen):
    """
    Reconoce la unidad cuyo modelo se ajusta mejor
    """
    modelos = np.load(ficMod, allow_pickle=True).item()

    for señal in tqdm(leeLis(*guiSen), ascii="·|/-\\#"):
        pathPrm = pathName(dirPrm, señal, 'prm')
        prm = leePrm(pathPrm)

        minDist = np.inf 
        for modelo in modelos:
            distancia = sum(abs(prm -modelos[modelo])**2)
            if distancia < minDist:
                minDist = distancia
                reconocida = modelo 

        pathRec = pathName(dirRec, señal, '.rec')
        chkPathName(pathRec)
        with open(pathRec, 'wt') as fpRec: 
            fpRec.write(f'LBO:,,,{reconocida}\n')      

if __name__ == "__main__":
    from docopt import docopt
    import sys

    usage=f"""
        Reconoce una bases de datos de señales de voz

        usage:
            {sys.argv[0]} [options] <guia> ...
            {sys.argv[0]} -h | --help
            {sys.argv[0]} --version

        options:
            -r, --dirRec DIRECTORI  directori de la señal reconeguda [default: .]
            -p, --dirPrm PATH  Directorio con las señales parametrizadas [default: .]
            -m, --ficMod FILE  directori amb els continguts acústics [default: .]
        """
    args= docopt(usage, version="tecparla2025")
    dirRec = args["--dirRec"]
    dirPrm = args["--dirPrm"]
    ficMod = args["--ficMod"]
    guiSen = args["<guia>"]

    reconoce(dirRec, dirPrm, ficMod, *guiSen)
