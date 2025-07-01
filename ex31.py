#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia=float(input('Qual a distância da viagem em km:'))

if distancia <= 200:
    preço= distancia * 0.50
    print('O valor da viagem para uma distância de \033[34m{:.0f}\033[m é de R$\033[34m{:.2f}\033[m!'.format(distancia, preço))

else:
    preço= distancia * 0.45
    print('O valor da viajem para uma distância de \033[35m{:.0f}\033[m é de R$\033[35m{:.2f}\033[m!!!'.format(distancia, preço))