x = int(input("Digite o valor de 'x': "))
y = int(input("Digite o valor de 'y': "))
z = int(input("Digite o valor de 'z': "))


if x + y > z and x + z > y and y + z > x:
    if x == y and z == y:
      print ("É um triângulo equilátero")
    elif x == y or z == y:
      print("É um triângulo isóceles")  
    elif x != y and z != y:
      print ("É um triângulo escaleno")
    else :   
     print ("Eles não formam um triângulo") 
else : 
  print ("Eles não formam um triângulo")