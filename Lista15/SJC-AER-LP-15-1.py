Data=float(input("Digite a data (Somente números): "))


Conta= int(Data// 10000)
D= int(Conta % 100)


conta= int(Data // 100)
M= int( conta % 100)


A= int(Data % 100)

invertido = 10000*A + 100*M + D

print("Dia:"+str(D)+" do mês:"+str(M)+" do ano de:"+str(A))
print("A data invertida é:"+str(invertido))