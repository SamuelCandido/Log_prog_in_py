i= 0
a= 1
n = int(input("Digite um valor: "))
if n !=0:
    while n >= a:
        i += (n - (a-1))/a
        a+= 1
    print(i)
if n == 0:
    print("Você digitou 0")
