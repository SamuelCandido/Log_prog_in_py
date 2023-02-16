from random import randint
def gera_lista(n):
    for i in range(n):
        random = randint(0,n-1)
        lista.append(random)
    lista.sort()
    print(lista)
lista=[]
n=int(input("Digite um numero: "))
gera_lista(n)