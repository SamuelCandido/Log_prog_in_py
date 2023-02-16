strI=input("Digite um número:")
strF= ""
for i in range(len(strI)):
    if strI[i]== "9":
        aux= 0
    else:
        aux= int(strI[i])+ 1
    strF+= str(aux)
print(strF)