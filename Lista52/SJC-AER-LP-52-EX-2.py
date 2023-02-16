n1=str(input("Digite o primeiro número: "))
n2=str(input("Digite o segundo número: "))
valor = True
aux = len(str1)
if len(n1) > len(n2):
    aux = len(n2)
for i in range(aux):
    if not (n1[i] < n2[i]):
        break
        valor = False
print(valor)