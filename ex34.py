#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario=float(input('Digite o salario atual do funcionário: R$'))

if salario <= 1250:
    aumento= (salario * 0.15 ) + salario
else:
    aumento= (salario * 0.10) + salario
print('O salário que era \033[31m{:.2f}\033[m passa a ser \033[34m{:.2f}\033[m'.format(salario, aumento))