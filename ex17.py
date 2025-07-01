from math import hypot
#solicitando valores ao usuário
co=float(input('Comprimento do cateto oposto:'))
ca=float(input('Comprimento do cateto adjacente'))

#calculo da hipotenusa
hip= hypot(co, ca)

#exibindo o resultado
print(' A hipotenusa vai medir {}{:.2f}'.format('\033[35m', hip))

