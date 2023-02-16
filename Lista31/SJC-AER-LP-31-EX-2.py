
valor = 1

print("Estes números são impares:")
for i in range(1,16,2):
    valor*=i
    print(i, end=" / ")

valor = 1
for i in range(1,16,2):
     valor*=i
print()    
print("O resutado dos produtos dos números impares é", valor)
