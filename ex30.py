número=int(input('Digite um número:'))

if número % 2 == 0:
    print('O número \033[34m{}\033[m é par'.format(número))
else:
    print('O número \033[345m{}\033[m é impar'.format(número))
