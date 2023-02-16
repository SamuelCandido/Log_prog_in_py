data=input("Digite uma data(ddmmaaaa)obs:sem '/': ")
if data[2:4] == '01':
    mes = 'janeiro'
if data[2:4] == '02':
    mes = 'fevereiro'
if data[2:4] == '03':
    mes = 'março'
if data[2:4] == '04':
    mes = 'abril'
if data[2:4] == '05':
    mes = 'maio'
if data[2:4] == '06':
    mes = 'junho'
if data[2:4] == '07':
    mes = 'julho'
if data[2:4] == '08':
    mes = 'agosto'
if data[2:4] == '09':
    mes = 'setembro'
if data[2:4] == '10':
    mes = 'outubro'
if data[2:4] == '11':
    mes = 'novembro'
if data[2:4] == '12':
    mes = 'dezembro'
print(f'Você nasceu em {data[0:2]} de {mes} de {data[4:]}')
