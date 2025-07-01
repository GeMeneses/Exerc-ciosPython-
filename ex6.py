num=int(input('Digite um número'))
d=num*2
t=num*3
r=num**0.5

print('O dobro de \033[31m{}\033[m é \033[32m{}!\033[m\n O triplo de \033[31m{}\033[m é \033[33m{}\033[m\n A raiz quadrada de \033[31m{}\033[m é \033[34m{:.2f}'.format(num, d, num, t, num, r))