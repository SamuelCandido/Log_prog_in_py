dia=int(input("Digite um dia: "))
mes=int(input("Digite um mes: "))
ano=int(input("Digite um ano: "))
def valido(dia, mes, ano):
    soma=0
    if dia <0 or dia >31:
        soma += -1
    if mes <0 or mes>12:
        soma += -2
    if ano <0:
        soma += -4
    return soma
valido(dia, mes, ano)