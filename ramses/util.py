def leeLis(fitlis):
    with open(fitlis,"rt") as fpLis:
        lista = []
        for linea in fpLis:
            lista.append(linea.strip())
    return lista