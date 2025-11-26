#! /usr/bin/env python3

import soundfile as sf
import numpy as np
from tqdm import tqdm

from ramses.util import * 
from ramses.prm import *

def parametriza(dirPrm, dirSen, *guiSen):
    for nomSen in tqdm(leeLis(*guiSen)):
        pathSen = pathName(dirSen, nomSen, "wav")
        sen, fm = sf.read(pathSen)

        prm = np.array(sen)

        pathPrm = pathName(dirPrm, nomSen, "prm")
        chkPathName(pathPrm)
        escrPrm(pathPrm, prm)


if __name__=="__main__":
    from docopt import docopt

    usage= ''' 
        Parametriza una base de datos de señales de voz

        usage:
            parametriza.py [options] <guia>...
            parametriza.py -h | --help
            parametriza.py --version

        options:
            -s, --dirSen DIRECTORI directori de la senyal d'entrada [default: .]
            -p, --dirPrm DIRECTORI directori de la senyal parametrizada [default: .]
        '''
    args=docopt(usage, version= "tecparla2025")
    dirSen = args["--dirSen"]
    dirPrm = args["--dirPrm"]
    guiSen = args["<guia>"]
    parametriza("prm", "Sen", "Gui/train.gui", "Gui/devel.gui")