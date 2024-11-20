import asyncio

#z1
#async def korutina():
#    lista_brojeva = [i for i in range (1,11)]
#    print(f'dohvacam listu brojeva ')
#    await asyncio.sleep(3)
#    print(f'Podaci dohvaceni: {lista_brojeva}')
#    return lista_brojeva

#asyncio.run(korutina())
    

async def korutina1():
    korisnici = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
    ]
    await asyncio.sleep(3)
    return korisnici

async def korutina2():
    proizvodi = [
    {"ime": "dorina", "proizvodac": "kras", "cijena": 19},
    {"ime": "domacica", "proizvodac": "kras", "cijena": 20},
    {"ime": "darko", "proizvodac": "kandit", "cijena": 5}
    ]
    await asyncio.sleep(5)
    return proizvodi


async def main():
    korisnici, proizvodi = await asyncio.gather(korutina1(),korutina2())
    print("Korisnici:", korisnici)
    print("Proizvodi:", proizvodi)
    
asyncio.run(main())

#4
#async def provjeri_parnost(broj):
    