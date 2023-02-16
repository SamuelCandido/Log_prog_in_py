contador=int(input('Digite quantos numeros haverá na lista: '))
lista=[]
def pares_impares(lista, contador):
    list_par = []
    list_impar = []
    for i in range(contador):
        num = int(input("Digite um valor da lista: "))
        if (num%2) == 0:
            list_par.append(num)
        else:
            list_impar.append(num)
    print("Este numero/numeros é par:", list_par)
    print("Este numero/numeros é impar:", list_impar)
pares_impares(lista, contador)