cpf = str(input('Digite seu cpf (somente numeros: '))
digito1 = 0
digito2 = 0
cont = 10
for i in range(len(cpf)-2):
    digito1 += int(cpf[i]) * cont
    cont -= 1
digito1 = (digito1 * 10 ) % 11
cont = 11
for i in range(len(cpf)-1):
    digito2 += int(cpf[i]) * cont
    cont -= 1
digito2 = (digito2 * 10 ) % 11
if digito1 == int(cpf[-2]) and digito2 == int(cpf[-1]):
    print('O cpf', cpf,'é válido')
else:
    print('O cpf', cpf,'é inválido')