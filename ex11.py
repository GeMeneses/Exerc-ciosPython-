from math import ceil
alt=float(input('Digite a altura da parede:'))
lar=float(input('Agora digite a largura: '))
tinta= ceil(alt*lar/2) #calculo da quantidade de tinta necessária
print('Para uma parede de {}m de altura e {}m de largura, é necessário {} lata(s) de tinta '.format(alt, lar, tinta))