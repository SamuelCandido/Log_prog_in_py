contador= int(input("Quantos numeros deverão ser perguntados?: "))
lista=[]
def min_max(contador, lista):
    for i in range(contador):
        num = int(input("Digite um número:"))
        lista.append(num)
    lista.sort()   
    print("O menor numero é:", lista[0])
    print("O maior numero é:", lista[-1])    
        
min_max(contador, lista)