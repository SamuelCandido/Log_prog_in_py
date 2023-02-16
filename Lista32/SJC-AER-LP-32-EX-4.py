n = int(input("Digite um valor: "))
h=0
for i in range(1,n+1):
    if i % 2 ==0:
        h = h - 1/i

    else:
        h = h + 1/i

print(h)
