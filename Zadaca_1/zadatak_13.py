lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def prvi_i_zadnji(lista):
    prvi = lista[0]
    zadnji = lista [-1]

    prvizadnji = (prvi, zadnji)

    return prvizadnji

print(prvi_i_zadnji(lista))

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def maks_i_min(lista):
    max = lista[0]
    min = lista[0]
    for broj in lista:
        if broj > max:
            max = broj
        if min > broj:
            min = broj

    return max,min

print(maks_i_min(lista))

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

def presjek(skup_1, skup_2):
    zajedno = skup_1 & skup_2
    return zajedno

print(presjek(skup_1, skup_2))