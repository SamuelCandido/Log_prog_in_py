diametro=int(input("Digite o valor do diametro: "))
def volume_esfera(diametro):
    raio=diametro/2
    volume=(raio ** 3) * (4/3) * 3.14159265
    print(volume)
volume_esfera(diametro)