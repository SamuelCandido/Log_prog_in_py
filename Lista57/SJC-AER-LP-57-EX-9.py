a= input("Digite um valor: ")
b=input("Digite o seguimento do valor passado: ")
def segmento(a, b):
    menor = a
    maior = b
    if a > b:
        menor = b
        maior = a
    if menor in maior:
        return True
    return False
print(segmento(a,b))