ano=int(input("Digite um ano: "))
def eh_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(True)
    else:
        (False)
eh_bissexto(ano)