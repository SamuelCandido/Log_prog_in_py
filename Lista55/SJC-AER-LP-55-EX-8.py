num=int(input("Digite um numero: "))
def primo(num):
    aux=0
    for i in range(1, num+1):
        if num % i == 0:
            aux+=1
    if aux == 2:
        print(True)
    else:
        print(False)
primo(num)


