dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês (De 1 a 12): "))
ano = int(input("Digite o ano: "))

x= dia*mes
calculo= ano % 100 


if x==calculo:
    
    print("A data é magica!! O dia X o mês é:",x)

else:
    print("Mas que pena está data não é mágica.",x)
   














