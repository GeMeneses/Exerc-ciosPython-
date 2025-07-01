import random
from time import sleep

número=random.randint(0,5) #faz o computador pensar
print('\033[34m Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('\033[35m-=-\033[m'*20)
adivinhe=int(input('Em que número eu pensei?')) #jogador tenta adivinhar
print('\033[37mPROCESSANDO...')
sleep(2)
if adivinhe == número:
    print('Você acertou, eu pensei em \033[34m {}'.format(número))
else:
    print('Não foi dessa vez, eu pensei no \033[35m{}\033[m e você no \033[35m{}'.format(número,adivinhe))