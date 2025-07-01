frase=str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece \033[34m{}\033[m vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição \033[35m{}\033[m'.format(frase.find('A')+1))
print('A utima letra A apareceu na posição \033[36m{}\033[m'.format(frase.rfind('A')+1))