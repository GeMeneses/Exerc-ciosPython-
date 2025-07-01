celsius= float(input('Informe a temperatura em Cº'))

#conversão em Fahrenheit
f= (celsius * 9/5) + 32

#exibição do resultado
print('A temperatura de \033[31m{:.1f}ºC\033[m corresponde a \033[31m{:.1f}ºF'.format(celsius, f))