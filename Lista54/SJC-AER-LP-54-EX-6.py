x=int(input("Digite o valor de X: "))
y=int(input("Digite o valor de y: "))
def potencia(x, y):
    for i in range(y-1):
        x *= x 
        return x
result = potencia(x, y)
print(result)
potencia(x, y)
