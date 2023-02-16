positivos= 0
negativos = 0

for i in range(3):
    v = int(input("Digite um número: "))
    if v >= 0:
        positivos = positivos + v
    else:
        negativos = negativos + 1

print("Soma dos positivos é igual a", positivos)
print("Total de números negativos é igual a", negativos)