contador= int(input("Quantos itens deverão ser perguntados?: "))
lista=[]
def inverte(contador, lista):
    for i in range(contador):
        num = input("Digite um item: ")
        lista.append(num)
    lista.reverse()
    print("A lista invertida é", lista)
inverte(contador, lista)