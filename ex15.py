#solicitação ao usuário
km= float(input(' Quantos km você percorreu com o carro?  ))
dias= int( input( 'Quantos dias você permaneceu com o carro'))

#calculo do preço
preço= (dias * 60) + (km * 0.15)
if preço <= 300:
    cor ='\033[34m'

else:
    cor = '\033[31m'

#exibição do resultado
print('O total a pagar é {}R$ {:.2f}'.format(cor,preço))