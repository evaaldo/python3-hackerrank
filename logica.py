tempInt = int(input())
tempExt = int(input())
clima = input()

if clima == 'inverno':
    desumidificacao()
else:
    coccao()

print('inicio de desumidificação')
umidadeInt = int(input())
tempInt = int(input())

if tempInt > 15 and umidadeInt >= '40%':
    exaustor()
elif tempInt < 15 and umidadeInt >= '40%':
    aquecimento()
    exaustor()
