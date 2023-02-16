total = 0

for i in range(85, 908):
    total = total + i
    if i %2==0:
        print("Um dos números pares é", i,end=" / ")
print()
print("A soma de todos os nomeros é", total)
