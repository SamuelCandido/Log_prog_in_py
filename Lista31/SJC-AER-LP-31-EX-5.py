
maior=0
menor=0
soma=0

for i in range(10):
    a = int(input("Digite a uma nota"))
    if i == 0:
        maior = a
        menor = a
    if a >= maior:
        maior = a
    if a <= menor:
        menor = a
    soma = soma+a 
    media = soma/3

print("O maior número é:", maior)
print("O menor número é:", menor)
print("A média é:", media)