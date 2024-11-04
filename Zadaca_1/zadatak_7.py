

a=input("Unesi lozinku: 8-15 znakova, barem jedno veliko slovo i jedan broj\n")
zabranjeno= {"password", "lozinka"}

if len(a)>=8 and len(a)<=15:
    if any(char.isupper() for char in a) and any(char.isdigit() for char in a):
        if any(zabrana in a.lower() for zabrana in zabranjeno):
            print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        else:
            print("dobro je")
            
    else:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")

else:
    print("Lozinka mora sadržavati između 8 i 15 znakova")

