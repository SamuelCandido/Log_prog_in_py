num=int(input("Digite a quantidade de asteristicos que devera sair: "))

def asteristicos_num(num):
    i=0
    for i in range(num):
        i+=1
        print('*', end="")
asteristicos_num(num)