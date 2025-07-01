n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
m=(n1+n2)/2
print('A média das notas {:.1f} e {:.1f} é igual a {:.1f}'.format(n1,n2,m))

print('A média de \033[31m{:.1f}\033[m e \033[32m{:.1f}\033[m é igual a \033[33m{:.1f} \033[m!!!'.format(n1,n2,m))