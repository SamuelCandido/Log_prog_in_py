a=input("Digite um valor:")
b=input("Digite outro valor que devera encaixar:")
def encaixa(a, b):
    b = str(b)
    a = str(a)
    contador = len(a) - len(b)
    aux = len(a)+1
    ult_dig = a[contador:aux]
    if ult_dig == b:
        return True
    return False
print(encaixa(a,b))