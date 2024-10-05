a=int(input('Informe o 1º valor:'))
b=int(input('Informe o 2º valor:'))
c=int(input('Informe o 3º valor:'))
maior=inter=menor=0
if a>b and a>c: maior=a
elif b>a and b>c: maior=b
else: maior=c

if a<b and a<c: menor=a
elif b<a and b<c: menor=b
else: menor=c

if menor < a < maior: inter=a
elif menor < b < maior: inter=b
else: inter=c

print('maior=%d, inter=%d, menor=%d'%(maior, inter, menor))
