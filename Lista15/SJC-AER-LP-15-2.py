Data=float(input("Digite a data (Somente números): "))


Conta= int(Data// 100000)
A= int(Conta % 100)


conta= int(Data // 1000)
S= int( conta % 10)


D= int(Data % 1000)


print("Ano da matrícula:"+str(A)+" semestre da matrículad@:"+str(S)+" ordem de matrícula:"+str(D))
