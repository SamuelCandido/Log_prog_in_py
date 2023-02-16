a = int(input("Digite o primeiro digito: "))
b = int(input("Digite o segundo digito: "))
c = int(input("Digite o terceiro digito: "))


if a > b and b > c: 
   print (c)
elif a < b and b < c:
    print (a)
elif a > b and b < c:
    print (b)
elif a == b:
    print (a)
else:
    print(c)