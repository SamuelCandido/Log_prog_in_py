def temperatura():
    contador=0
    calc=0
    media=0
    for contador in range(12):
        temperatura=int(input("Digite um numero: "))
        lista.append(temperatura)
        calc+=temperatura
    media= calc/12
    print("media: ", media)
    if lista[0] > media:
        print("Janeiro teve a temperatura de:", temperatura)
    if lista[1] > media:
        print("Fevereiro teve a temperatura de:", temperatura)
    if lista[2] > media:
        print("Março teve a temperatura de:", temperatura)
    if lista[3] > media:
        print("Abril teve a temperatura de:", temperatura)
    if lista[4] > media:
        print("Maio teve a temperatura de:", temperatura)
    if lista[5] > media:
        print("Junho teve a temperatura de:", temperatura)
    if lista[6] > media:
        print("Julho teve a temperatura de:", temperatura)
    if lista[7] > media:
        print("Agosto teve a temperatura de:", temperatura)
    if lista[8] > media:
        print("Setembro teve a temperatura de:", temperatura)
    if lista[9] > media:
        print("Outubro teve a temperatura de:", temperatura)
    if lista[10] > media:
        print("Novembro teve a temperatura de:", temperatura)
    if lista[11] > media:
        print("Dezembro teve a temperatura de:", temperatura)
lista=[]
temperatura()