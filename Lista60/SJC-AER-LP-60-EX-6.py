def media_turma(lista):
    contador=0
    maior=lista[0]
    menor=lista[0]
    for i in range (len(lista)):
        contador+=lista[i]
        if lista[i]>maior:
            maior=lista[i]
        if lista[i]<menor:
            menor=lista[i]
    
    print("A média é:", contador/len(lista), "A maior nota é:", maior, "A menor nota é:", menor)
lista=[]
while True:
    nota=int(input("Digite uma das notas (digite 000 para parar): "))
    if nota==000:
        break
    else:
        lista.append(nota)
media_turma(lista)