def calcula_media(nota1, nota2, nota3, classe):
    if classe=="Aritmeticamente" or classe=="aritmeticamente":
        return (nota1+nota2+nota3)/3
    elif classe=="Ponderada" or classe=="ponderada":
        return (nota1*5+nota2*3+nota3*2)/10
    elif classe=="Harmônica" or classe=="harmônica":
        return(3/((1/nota1)+(1/nota2)+(1/nota3)))
    else:
        print("Esta letra não pertence as opções")

nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))
nota3=int(input("Digite a terceira nota: "))
classe= str(input("Como deve ser calculado? Aritmeticamente,Ponderada ou Harmônica?: "))

media=calcula_media(nota1, nota2, nota3, classe)

print(media)


