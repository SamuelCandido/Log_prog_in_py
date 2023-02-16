s2 = "local"
s1 = "misterio"

soma_palavras = ""

if len(s2)<len(s1):
    aux = s1
    s1 = s2
    s2 = aux
    

for i in range(len(s1)):
    soma_palavras = soma_palavras + s1[i] +s2[i]

if len(s2)>len(s1):
    soma_palavras = soma_palavras + s2[len(s1):]

print(soma_palavras)