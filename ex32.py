from datetime import date
ano=int(input('Que ano você quer analisar? Digite 0 para analisar o atual'))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[35m{}\033[m é um ano bissexto'.format(ano))
else:
    print('O ano \033[35m{}\033[m \033[31mnão\033[m é um ano Bissexto!!!'.format(ano))