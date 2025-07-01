from math import trunc
num=float(input('Digite um número:'))
inteiro=trunc(num)
print('A porção inteira do número {}{}{} é {}{}{}!!!'.format('\033[34m', num, '\033[m','\033[35m',inteiro, '\033[m'))
