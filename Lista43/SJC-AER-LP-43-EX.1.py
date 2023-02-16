n=None
i= 0
menor= n
maior= n
while n !="fim":
    n = input("Digite um valor(Digite [fim] para parar): ")
    if n == None:
        print("Não foi digitado nada.")
        
    if n == "fim":
        break
    
    if i == 0:
        maior = n
        menor = n
    i += 1
    
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print("Maior:", int(maior),"Menor:", int(menor))
