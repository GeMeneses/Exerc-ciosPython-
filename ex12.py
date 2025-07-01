produto= float(input(' Qual o valor atual do produto? R$'))
#calculo de desconto
desc= produto- (produto * 5 / 100 )
#exibe o resultado
print('O produto que custava \033[31mR${:.2f}\033[m, com 5% de desconto passará a custar \033[34mR${:.2f}\033[m '.format(produto, desc))

