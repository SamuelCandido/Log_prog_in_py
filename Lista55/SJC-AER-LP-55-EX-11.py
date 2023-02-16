num=int(input("Digite um número: "))
contador=1
calc=0
def perfect_num(num, contador, calc):
    while contador<num:
        if num%contador == 0:
            calc+=contador
        contador+=1

    if calc==num:
        print("O número", num,"é perfeito")
    else:
        print("O número", num,"não é perfeito")    

perfect_num(num, contador, calc)