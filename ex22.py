nome= str (input(' Digite seu nome completo:')).strip()

#Letras maiúsculas
print('\33[34m{}\33[m'.format(nome.upper()))

#Letras minúsculas
print('\33[36m{}\33[m'.format(nome.lower()))

#Quantas letras tem
print('Seu nome completo tem \33[35m{}\33[m letras'.format(len(nome)- nome.count(' ')))

#primeiro nome
separa=nome.split()
print('Seu primeiro nome é \33[36m{}\33[m e ele tem \33[37m{}\33[m letras'.format(separa[0].capitalize(),len(separa[0])))

