num=float(input('Qual a distância em metros:'))
km= num / 1000
hm= num / 100
dam= num  /10
dm= num * 10
cm= num * 100
mm= num * 1000
cores= {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','roxo':'\033[35m'}
print('A medida de {:.2f}m corresponde a :'.format(num))
print('{}{}{}km'.format(cores['azul'],km,cores['limpa']))
print('{}{:.2f}{}hm'.format(cores['amarelo'],hm,cores['limpa']))
print('{}{:.2f}{}dam'.format(cores['roxo'],dam,cores['limpa']))
print('{}{:.0f}{}dm'.format(cores['azul'],dm,cores['limpa']))
print('{}{:.0f}{}cm'.format(cores['amarelo'],cm,cores['limpa']))
print('{}{:.0f}{}mm'.format (cores['roxo'],mm,cores['limpa']))
