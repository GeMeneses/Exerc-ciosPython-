#solicitando velocidade ao usuário
vel=float(input('Em qual velocidade você está?'))

#mostrando resultado
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[31mATENÇÃO!!!\033[m Você utrapassou o limite de velocidade e irá pagar uma multa de R$\033[31m{:.2f}\033[m!'.format(multa))
print('Dirija com segurança')
