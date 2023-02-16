nome=str(input("Digite seu nome: "))
frase=str(input("Digite uma palavra/frase: "))
def asteristicos(nome, frase):
    i=0
    c=0
    num=len(frase)
    for i in range(num):
        i+=1
        print('*', end="")
    print()
    print(nome)
    print(frase)
    for c in range(num):
        c+=1
        print('*', end="")
asteristicos(nome, frase)