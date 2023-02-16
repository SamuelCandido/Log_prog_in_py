numero=int(input("Digite o numero da tabuada que quer: "))
print()
print("Tabuada de", numero)
for i in range(1,16):
    k= i * numero
    print(numero, "X", i,"=", k)

