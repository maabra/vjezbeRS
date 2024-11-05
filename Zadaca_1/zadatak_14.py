
def isPrime(x):
    for i in range (2,x):
        if x%i == 0:
            return False
    return True
        
print(isPrime(10))

def primes_in_range(start, end):
    lista = []
    for i in range (start, end+1):
        prime= True
        for j in range (2,i):
            if i%j == 0:
                prime= False
                break
        if prime == True:
            lista.append(i)        
    return lista

print(primes_in_range(1,10))