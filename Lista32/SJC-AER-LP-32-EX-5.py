precisao = int(input('Digite a precisão de π: '))
π = 3
contador = 0

print("Pi =", π)
for i in range(2, (precisao*2), 2):
    if contador % 2 == 0:
        π += 4 / (i * (i+1) * (i+2))
    elif contador % 2 != 0:
        π -= 4 / (i * (i+1) * (i+2))
    print("Pi =", π)
    contador += 1

