print('-' * 20)
print('Aluguel de Carros')
print('-' * 20)
d = int(input('Quantidade de dias alugado:'))
k = float(input('Qunatidade de Km rodado:'))
va = d * 60
vb = k * 0.15
vv = va + vb
print("\n Valor dos dias Alugados = R${:.2f} \n Valor por Quilometragem = R${:.2f} \n Valot total do Aluguel: "
      "R${:.2f}".format(va, vb, vv))
