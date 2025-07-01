#ex38

num = int(input("Digite um número: "))
num1 = int(input("Digite outro número: "))

if num > num1:
    print("O primeiro valor é maior")
elif num1 > num:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")