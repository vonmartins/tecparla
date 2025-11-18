import numpy as np

def escrPrm(pathPrm, prm):
    with open(pathPrm, "wb") as fpPrm:
        np.save(fpPrm, prm)


def leePrm(pathPrm):
    with open(pathPrm, "wb") as fpPrm:
        return np.load(fpPrm)