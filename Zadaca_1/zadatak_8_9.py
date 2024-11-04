lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtriraj_parne(lista): 
    nova_lista=[]
    for broj in lista:
        if broj%2==0:
            nova_lista.append(broj)
    return nova_lista

print(filtriraj_parne(lista))


lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def ukloni_duplikate(lista):
    novaL = []
    for broj in lista:
        if broj not in novaL:
            novaL.append(broj)
    return novaL


print(ukloni_duplikate(lista))


