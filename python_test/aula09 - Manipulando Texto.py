print('-' * 175)
print('Ideia de analise(quantidade de palavras letras etc) /  pesquisa (de palavras e elemnetos do texto) /'
      ' localização da pesquisa / trasformação do texto (maiscula, menuscula etc)')
print('-' * 175)
texto = input('Insira o texto á ser analisado:')
txts = texto.strip()
sptxt = texto.split()
qletras = len(sptxt)
print('Quantidade de palavras: {}'.format(qletras))
psq = input('elemento á procurar: ')
add = (texto.count(psq))
print('Quantidade de elementos encontrados no texto: {}'.format(add))


