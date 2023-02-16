n=int(input("Digite a quantidade de termos:"))

if n==0:
    print("Fibonacci: Ø")
    
elif n==1:
    print("Fibonacci: 0")

elif n==2:
    print("Fibonacci: 0, 1")

else:
    a1 = 0
    a2 = 1
    for i in range(3, n+1):
        print("Fibonacci: 0, 1,", end=" ")
        t = a1 + a2
        print(t, end=", ")
        a1 = a2
        a2 = t


