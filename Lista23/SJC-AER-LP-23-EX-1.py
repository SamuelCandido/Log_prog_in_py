import math  

a = int(input("Digite o primeiro valor : "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor "))

delta = b ** 2 -4 * a * c
if delta >= 0:
    x1 = (-b + math.sqrt(delta))/ (2*a)
    x2 = (-b - math.sqrt(delta))/ (2*a)
    if delta >= 1:
        print("A equação possui duas raízes reais")
        print("S{"+str(x1)+","+str(x2)+"}")
    if delta == 0:
        print ("A equação possui uma raíz real")
        print ("S{"+str(x1)+"}")
else:
    print ("A equação não possui raízes reais pois o delta foi menor que 0")
    print(delta)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      