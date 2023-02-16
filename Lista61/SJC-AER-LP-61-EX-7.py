def ordenar_lista(lista):
    for contador in range(len(lista)-1,0,-1):
        for i in range(contador):
            if lista[i]>lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

lista = [99, 55, 77, 84, 15, 45, 29, 23, 20]
ordenar_lista(lista)
print(lista)