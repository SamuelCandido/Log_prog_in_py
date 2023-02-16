num=int(input("Digite um valor inteiro maior que 0: "))
def numero_digitos(num):
    if num >0:   
        print(len(str(num)))
    elif num <0:
        print("O digito não atende os requisitos.")
numero_digitos(num)