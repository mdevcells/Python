print('\n>>> Aumneto Salarial <<<')
vs = float(input('Valor do Salário: R$'))
am = float(input('Porcentagem do Aumento:'))
va = am/100
vb = vs * va
vc = vs + vb
print('Valor total com aumento: R${:.2f}' .format(vc))
