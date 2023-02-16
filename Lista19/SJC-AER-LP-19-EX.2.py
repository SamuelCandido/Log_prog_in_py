n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if(n3 > n2):
    x = n3
    n3 = n2
    n2 = x

if(n2 > n1):
    x = n2
    n2 = n1
    n1 = x

if(n3 > n2):
    x = n3
    n3 = n2
    n2 = x    


print(n1,"/",n2,"/",n3)



