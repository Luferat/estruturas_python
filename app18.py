# Testes com while e break

import os
os.system('cls')

contador = 1

while contador <= 10:
    print(contador)
    contador = contador + 1
    if contador == 6:
        print('Gotcha!')
        continue
    print('Pin')