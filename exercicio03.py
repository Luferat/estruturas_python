'''
Exercício 3
Tabuada: Peça um número ao usuário e mostre sua tabuada de 1 a 10. 
'''

import os
os.system('cls')

numero = int(input("Digite um número: "))

# Debug
# print(numero, type(numero))

for num in range(1, 11):
    print(f'{numero} x {num} = {numero * num}')