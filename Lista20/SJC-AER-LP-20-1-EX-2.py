n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))


if n1 + n2  >= 10 : 
  x = (n1 + n2)/2 
  if n1 > 3 and n2 > 3:
       print ("Parabéns")
       print ("Aprovado, sua média é: ",x)
  else :
      print ("Reprovado com a média de: ",x)
      print ("A uma ou mais das notas inferior à 3")

else :
 y = (n1 + n2)/2
 print ("Reprovado, sua média é:",y)
