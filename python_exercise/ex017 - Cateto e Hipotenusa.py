print('-' * 21)
print('Calculo da Hipotenusa')
print('-' * 21)
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hi))
