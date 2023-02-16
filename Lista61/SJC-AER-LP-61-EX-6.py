import random

def gera_lista_embaralhada(n):
    for i in range(n):
        aux=random.randrange(0,n-1)
        lista.append(aux)
    print(lista)

n=int(input("Digite um numero: "))
lista=[]
gera_lista_embaralhada(n)