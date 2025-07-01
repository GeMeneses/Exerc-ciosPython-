from math import cos, tan, sin,radians
#solicitação de ângulo
angulo=float(input('Digite o ângulo que você deseja:º'))

#descobrindo o sen, cos, tan
cos=cos(radians(angulo))
sen=sin(radians(angulo))
tan=tan(radians(angulo))

#exibindo o resultado
print('O ângulo {} tem o SENO \033[34m{:.2f}\033[m!\nO ângulo de {} possui o COSSENO \033[34m{:.2f}\033[m!\nO ângulo de {} tem a TANGENTE \033[34m{:.2f}\033[m!'.format(angulo,sen,angulo, cos,angulo, tan))