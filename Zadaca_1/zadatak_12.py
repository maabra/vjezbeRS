rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

def obrni_rjecnik(rjecnik):
    novirjecnik = {}
    for kljuc in rjecnik.keys():
        pomocnakljuc = kljuc
        pomocnavrijednost = rjecnik.get(kljuc)
        
        novirjecnik[pomocnavrijednost] = pomocnakljuc

    return novirjecnik

print(obrni_rjecnik(rjecnik))