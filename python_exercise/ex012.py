print('>>> Calculadora de Descontos <<<')
v = float(input('Valor do Produto:'))
d = float(input('Valor do Desconto:'))
vv = d / 100
vd = v * vv
vf = v - vd
print('>>> Valor com desconto: R${}' .format(vf))
