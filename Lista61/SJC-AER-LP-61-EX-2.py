def notas():
    contador_notas=0
    calc=0
    media=0
    menores_7=0
    maiores_7=0
    while True:
        notas=int(input("Digite um numero: "))
        if notas == -1:
            break
        if notas >0:
            contador_notas+=1
            lista.append(notas)
            calc+=notas
            media= calc/contador_notas
        if notas <=7:
            menores_7+=1
        if notas >7:
            maiores_7+=1
    print(lista)
    lista.reverse()
    for i in range(contador_notas):
        print(lista[i])
    print("Quantidade de notas digitadas foi:", contador_notas)
    print("O valor da soma dos numeros digitados é:", calc)
    print("A media dos valores digitados é:", media)
    print("A quantidade de numeros digitados maiores de 7 é:", maiores_7)
    print("A quantidade de numeros digitados abaixo de 7 é:", menores_7)
    print("Mas que programa detalhado em!!! kkk")
lista=[]
notas()