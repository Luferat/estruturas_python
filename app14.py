# Mais testes com 'for in'

import os
os.system('cls')

# Uma string é uma coleção de caracteres
fruta = 'abacate'
print(len(fruta))
print()
print(fruta[0])
print()
for letra in fruta:
    print(letra)

# Uma coleção de números
print()
numeros = [0, 1, 2, 3]
for num in  numeros:
    print(num)

# Range é uma coleção de números
# Referências: https://www.w3schools.com/python/python_range.asp
print()
for num in range(10):
    print(num)        