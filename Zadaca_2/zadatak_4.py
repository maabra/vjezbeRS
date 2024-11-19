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
print(kalkulator.korijen())


#3