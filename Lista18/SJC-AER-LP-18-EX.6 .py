a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))


if a > b: 
    x = a 
    x = x % b
elif a < b :
    x = b
    x = x % a
else: 
    x = 0

if x >= 1:
    print (a, "e",b, "não são múltiplos")
else:
    print (a, "e",b, "são múltiplos")