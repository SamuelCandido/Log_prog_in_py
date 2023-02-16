f1= input("Digite uma frase:")
f2= input("Digite outra frase:")

contado= len(f1)
contador=len(f2)
print("A frase '"+str(f1)+"' tem:", contado,"caracteres")
print("A frase '"+str(f2)+"' tem:", contador,"caracteres")
if contador==contado:
    print("A frase '"+str(f1)+"' tem o mesmo tamanho que '"+str(f2)+"'")
else:
    print("A frase '"+str(f1)+"' tem o tamanho diferente de '"+str(f2)+"'")
if f1==f2:
    print("As duas frases contem o mesmo conteúdo")
else:
    print("As duas frases contem conteúdos diferentes")