n= 0
i = 0
media = 0
while n != "fim":
    n= 0
    n = input("Digite um número ou a palava (fim) para parar:")
    if n == "fim":
        n = None
        break
    media += int(n)
    i +=1
media = media / i
if n == 0:
    print('Não foi digitado nenhum número.')
print("A media é:", media)
print("A quantidade de números digitados foi:", i)

