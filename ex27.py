nome=str(input('Digite seu nome completo')).strip().title()
separa=nome.split()
print('Muito prazer em te conhecer\nSeu primeiro nome é \033[35m{}\033[m\nSeu ultimo nome é \033[36m{}'.format(separa[0], separa[-1]))