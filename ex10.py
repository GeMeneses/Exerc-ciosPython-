real=float(input('Quanto você tem na carteira?'))
dolar= real / 5.83
print('Com \033[35mR${}\033[m você consegue comprar \033[34mU${:.2f}\033[m!'.format(real, dolar))