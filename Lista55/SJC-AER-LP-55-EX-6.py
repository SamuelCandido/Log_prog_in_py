altura=float(input("Digite a sua altura: "))
sexo=str(input("Digite o seu sexo: "))
def peso_ideal(altura, sexo):
    if sexo == "Mulher" or sexo == "mulher":
        pesoM=62.1*altura- 44.7
        print("Seu peso ideal é:", pesoM)
    
    elif sexo == "Homem" or sexo == "homem":
        pesoH=72.7 * altura -58
        print("Seu peso ideal é:", pesoH)
peso_ideal(altura, sexo)


