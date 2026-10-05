'''
Exercício 3
Tabuada: Peça um número ao usuário e mostre sua tabuada de 1 a 10. 
'''

import os
os.system('cls')

# Debug
# print(numero, type(numero))

num1 = 1

while num1 < 11:
    print('---------------------------')

    num2 = 1
    
    while num2 < 11:
        print(f'{num1} x {num2} = {num1 * num2}')
        num2 = num2 + 1

    num1 = num1 + 1
