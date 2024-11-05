vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def counter_vowels_consonants(tekst):
    tekstuslovima= [*tekst]
    rjecnik = {'suglasnici':0 ,'samoglasnici':0}
    for slovo in tekstuslovima:
        if slovo in vowels:
            rjecnik['samoglasnici'] += 1
        elif slovo in consonants:
            rjecnik['suglasnici'] += 1
    
    return rjecnik

print(counter_vowels_consonants(tekst))
            
            




