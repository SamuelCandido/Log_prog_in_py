n = int(input("Digite um valor: "))
h=0
for i in range(0,n):
    h = h + (n-i)/(i+1)

print(h)