num=int(input("Digite um valor inteiro maior que 0: "))
primeiro_digito=""
def primeiro(num, primeiro_digito):
    if num >0:
        primeiro_digito=str(num)
        print("O primeiro digito de", num,"é:", primeiro_digito[0])
    elif num<0:
        print("O digito não atende os requisitos.")
primeiro(num, primeiro_digito)