a = int(input("Digite a primeira nota: "))
b = int(input("Digite a segunda nota: "))


if n1 + n2  >= 10 : 
  x = (n1 + n2)/2 
  if n1 > 3 and n2 > 3:
       print ("Parabéns")
       print ("Aprovado, sua média é: ",x)
  else :
      nf = (x - 5)
      print ("Reprovado com a média de: ",x)
      print ("A nota necessária para a aprovação é:",nf)

else :
 y = (n1 + n2)/2
 print ("Reprovado,sua média é:",y)