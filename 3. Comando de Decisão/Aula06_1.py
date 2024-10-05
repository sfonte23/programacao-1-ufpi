a=float(input('Informe o comprimento do lado 1:'))
b=float(input('Informe o comprimento do lado 2:'))
c=float(input('Informe o comprimento do lado 3:'))
texto=''
ehTriangulo=True if a<b+c and b<a+c and c<b+a else False
if ehTriangulo:
    texto='É triângulo'
    if a==b and b==c:
        texto+=' equilátero.'
    elif a!=b and b!=c and a!=c:
        texto+=' escaleno.'
    else:
        texto+=' isóceles.'
else:
    texto='Não é triângulo.'
print(texto)
