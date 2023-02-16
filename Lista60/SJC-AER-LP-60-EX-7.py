def vogais_consoantes(texto):
    vogais=''
    consoantes=''
    for i in texto:
        for letra in i:
            if letra.upper() in "AEIOU":
                vogais+=letra
            elif letra.upper() in "BCDFGHJKLMNPQRSTVWYZ":
                consoantes+=letra
    lista=[vogais, consoantes]
    return lista
    
    
print(vogais_consoantes(['Samuel Jose Candido']))