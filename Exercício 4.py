# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do,
#objeto tupla para verificar quantas vezes o número 4 aparece na tupla

import collections
numeros = [ 1, 2, 2, 3, 4, 4, 4, 5]
repetidos = collections.Counter(numeros)
print('O número 4 repete:')
print(repetidos[4])
print('vezes')