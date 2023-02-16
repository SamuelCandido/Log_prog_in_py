n=int(input("Digite um numero: "))
d=int(input("Digite um numero: "))
def conta_digitos(n, d):
    if d >0 and d <=9:
        n = str(n)
        d = str(d)
        digito=n.count(d)
        print("O numero", d,"aparece", digito,"vezes.")
    elif num <0:
        print("O digito não atende os requisitos.")
conta_digitos(n, d)