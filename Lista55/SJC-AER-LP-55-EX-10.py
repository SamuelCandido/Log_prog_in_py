ano=int(input("Digite seus anos de vida: "))
mes=int(input("Digite seus meses de vida: "))
dia=int(input("Digite seus dias de vida: "))
    
def idade_dias(ano,mes,dia):
    return (ano*365)+(mes*30)+dia
idade=idade_dias(ano,mes,dia)
print("A sua idade é ", idade,"em dias.") 