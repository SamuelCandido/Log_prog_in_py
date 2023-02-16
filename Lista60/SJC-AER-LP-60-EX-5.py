def media_turma():
    lista=[]
    for i in range(4):
        num = int(input("Digite uma nota: "))
        lista.append(num)
    media = (lista[0]+lista[1]+lista[2]+lista[3])/4
    print("Sua media é", media)
media_turma()