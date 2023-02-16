n=int(input("Digite um valor inteiro positivo: "))
def fatorial(n):
    if n >0:
        fat = 1
        i = 2
        while i <= n:
            fat = fat*i
            i = i + 1
        print("O fatorail de", n,"é:", fat)
    else:
        print("Este valor não é positivo.")
fatorial(n)
