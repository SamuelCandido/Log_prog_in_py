i=0
string=''
def sorteia_dado(i, string):
    import random
    for i in range(1000000):
        i+=1
        h=random.randrange(1, 7)
        string+=str(h)
    print("O numero 1 apareceu:", string.count('1'),"vezes.")
    print("O numero 2 apareceu:", string.count('2'),"vezes.")
    print("O numero 3 apareceu:", string.count('3'),"vezes.")
    print("O numero 4 apareceu:", string.count('4'),"vezes.")
    print("O numero 5 apareceu:", string.count('5'),"vezes.")
    print("O numero 6 apareceu:", string.count('6'),"vezes.")
    
sorteia_dado(i, string)


