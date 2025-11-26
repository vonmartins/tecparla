import re

reLBO = re.compile(r"LBO:(\s*\d*\s*,){3}(?P<trn>\w+)")

def cogeTrn(ficMar):
    with open(ficMar, "rt") as fpMar:
        for linea in fpMar:
            if (match := reLBO.match(linea)):
                return match["trn"]