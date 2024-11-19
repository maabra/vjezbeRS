kvadriraj = lambda x: x**2
print (kvadriraj(5))

zbroji_pa_kvadriraj = lambda a,b : (a+b)**2
print (zbroji_pa_kvadriraj(2,2))

kvadriraj_duljinu = lambda niz: len(niz) **2
print (kvadriraj_duljinu("bokbok"))

pomnozi_i_potenciraj = lambda x,y: (y*5) **x
print (pomnozi_i_potenciraj(2,2))

paran_broj = lambda x: "paran" if x%2==0 else "neparan"
print (paran_broj(3))