idade=int(input("Digite uma nota: "))
def conceito_idade(idade):
    if idade >= 5 and idade <= 7:
        print("A idade:", idade,"Recebe o conceito 'Infantil A'.")
    elif idade >= 8 and idade <= 10 :
        print("A idade:", idade,"Recebe o conceito 'Infantil B'.")
    elif idade >= 11 and idade <= 13:
        print("A idade:", idade,"Recebe o conceito 'Juvenil A'.")
    elif idade >= 14 and idade <= 17:
        print("A idade:", idade,"Recebe o conceito 'Juvenil b'.")
    elif idade >= 18 :
        print("A idade:", idade,"Recebe o conceito 'Adulto'.")
conceito_idade(idade)
