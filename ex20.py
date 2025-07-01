import random
n1=str(input('Primeiro aluno:'))
n2=str(input('Segundo aluno:'))
n3=str(input('Terceiro aluno:'))
n4=str(input('Quarto aluno:'))

#Sorteando a ordem
lista = [n1, n2, n3, n4]
random.shuffle(lista)

#exibindo o resultado
print('A ordem de apresentação séra:')
print('\033[34m{}'.format(lista))