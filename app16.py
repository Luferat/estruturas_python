# Loop while

import os
os.system('cls')

while True:
    os.system('cls')
    print('''
    1) Estou com fome
    2) Estou com sede
    3) Quero minha mãe

    0) Sair
    ''')

    x = input("Escolha uma opção: ")

    match x:
        case '0':
            print('\nAcabou')

            # Esse break interrompe o 'while'
            break

        case '1':
            print('\nVai comer')

        case '2':
            print('\nBeba água')

        case '3':
            print('\nGrite: MAMÃE!!!')

        # Nenhuma das opções acima é válida
        case _:
            print('\nNão entendi!')

    input('Tecle [Enter] para continuar.')