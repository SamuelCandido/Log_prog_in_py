nome=str(input("Digite um nome: "))
n=int(input("Digite a quantidade de vezes que o nome se repete: "))
def imprime_nome(nome, n):
    for i in range(n):
        print(nome, end=",")
imprime_nome(nome,n)