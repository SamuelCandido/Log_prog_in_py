str1= str(input("Digitge alguma palavra: "))
str2= str(input("Digitge alguma outra palavra: "))

reverso= str1[::-1]

if str2 == reverso:
    print("A palavra "+str(str2)+" é o iverso da palavra "+str(str1))
    
else:
    print("A palavra "+str(str2)+" não é o iverso da palavra "+str(str1))