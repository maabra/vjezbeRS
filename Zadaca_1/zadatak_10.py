tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje . Python je vrlo popularan ."

def brojanje_rijeci(tekst):
    rijeci = tekst.split()
    brojac = {}
    for rijec in rijeci:
        if rijec in brojac:
            brojac[rijec] += 1
        else:
            brojac[rijec] = 1
    return brojac
 

print(brojanje_rijeci(tekst))
