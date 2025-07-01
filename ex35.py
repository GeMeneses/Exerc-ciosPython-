# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('\033[34mAnalisador de triângulos...\033[m')
a=float(input('Primeiro segmento:'))
b=float(input('Segundo segmento:'))
c=float(input('terceiro segmento:'))

if a + b > c and b + c > a and c + a > b:
    print ('Os segmentos \033[31m{}\033[m, \033[32m{}\033[m, \033[33m{}\033[m formam um triângulo'.format(a, b, c))
else:
    print('Os segmentos \033[34m{}\033[m, \033[35m{}\033[m, \033[36m{}\033[mnão podem formar um triângulo')