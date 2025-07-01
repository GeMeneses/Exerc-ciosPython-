#nome da cidade
'''cidade=str(input('Em que cidade você nasceu:')).strip().upper()
separa=cidade.split()
if separa[0] == 'SANTO':
    print('true')
else:
    print('false')'''

cid=str(input('Em que cidade você nasceu?')).strip().lower()
print('\033[34m', cid[:5]=='santo')