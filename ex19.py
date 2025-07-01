import random
aluno=str(input('Primeiro aluno:'))
aluno2=str(input('Segundo aluno:'))
aluno3=str(input('Terceiro aluno:'))
aluno4=str(input('Quarto aluno:'))
#Soreio
#lista=[aluno,aluno2,aluno3,aluno4]
sorteio=random.choice(lista)
#exibindo o resultado
print('O aluno sorteado foi o \033[35m{}\033[m!!!'.format(sorteio))