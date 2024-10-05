print('5=',bin(5))

'''
  Nossos PCs usam complemento de 2 (pesquisar).
  Precisamos converter c2 em C1.
  C2(x)=-x   
  C1(x)+1=-x
  C1(x)=-x-1
'''
print('C1(',bin(5),')=',bin(-5-1),bin(~5))
print('C1(',bin(5),')=',bin(5-1))
print('5<<1=',5<<1)      #101 --> 1010
print('5<<2=',5<<2)      #1010 --> 10100
print('5>>1=',5>>1)      #101 --> 010
print('5>>2=',5>>2)      #010 --> 001
print('5&3=',5&3)        #101 & 011 --> 001
print('5^3=',5^3)        #101 ^ 011 --> 110
print('5|3=',5|3)        #101 | 011 --> 111



'''
  Nossos PCs usam complemento de 2 (pesquisar).
  Precisamos converter c2 em C1.
  C2(x)=~x+1   
  C2(x)-1=~x   
'''
