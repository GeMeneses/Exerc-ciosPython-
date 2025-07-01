#: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#Solicitando valor ao usuário
a=int(input('Primeiro valor:'))
b=int(input('Segundo valor:'))
c=int(input('Terceiro valor:'))
#encontrando número maior

maior = a

if b > a and b > c:
    maior = b
if  c > a and c > b:
    maior= c


#encontrando menor númer
menor = a

if b < a and b < c:
    menor = b
if  c < a and c < b:
    menor = c
print('O maior valor foi \033[34m{}\033[m'.format(maior))
print('O menor valor foi \033[35m{}\033[m'.format(menor))

