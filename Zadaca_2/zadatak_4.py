#1
import datetime
import math

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        return f"Marka automobila je {self.marka}, modela {self.model} napravljen {self.godina} sa {self.kilometraza} kilometara"
    
    def starost(self):
        return datetime.date.today().year - self.godina


automobil = Automobil("Opel", "Astra K", 2017, 160000)

print(automobil.ispis())
print(automobil.starost())

#2
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        return self.a / self.b
    
    def potenciranje(self):
        a = math.pow(self.a,2)
        b = math.pow(self.b,2)
        return a, b
    
    def korijen(self):
        a = math.sqrt(self.a)
        b = math.sqrt(self.b)
        return a, b


kalkulator = Kalkulator(4,9)
print(kalkulator.zbroj())
print(kalkulator.oduzimanje())
print(kalkulator.mnozenje())
print(kalkulator.dijeljenje())
print(kalkulator.potenciranje())
print(kalkulator.korijen(), "\n")


#3

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]


class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)


studenti_objekti = [Student(x["ime"], x["prezime"], x["godine"], x["ocjene"]) for x in studenti]

for s in studenti_objekti:
    print(f"{s.ime} {s.prezime}, godine: {s.godine}, ocjene: {s.ocjene}")


#4

class Krug:
    def __init__(self, r):
        self.r = r
    
    def opseg(self):
        return 2*self.r*3.14
    
    def povrsina(self):
        return (self.r**2) * 3.14
        
krug = Krug(float(input("Upisi radijus: ")))
print(krug.opseg())
print(krug.povrsina())

#5
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        return f"Radim na poziciji {self.pozicija} sa placom {self.placa} "
    
radnik = Radnik("Marko", "varioc", 5000)    
print(radnik.work())

class Manager(Radnik):
    def __init__(self,ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}"

    def give_raise(self, radnik, povecanje):
        radnik.placa = radnik.placa + povecanje


manager = Manager("Franko", "menager", 8000, "strojarstvo")
manager.give_raise(radnik, 2000)

print(manager.work())
print(radnik.work())


