import os

os.system('cls')

alunas = [
    ('Maria', '2000-10-14', 'A'),
    ('Joana', '1997-08-10', 'a'),
    ('Pedra', '1997-08-10', 'I'),
    ('Manoela', '1997-08-10', 'A'),
    ('Zuleica', '1997-08-10', 'I'),
    # ...
]
'''
print(f'{alunas[1][0]} nasceu em {alunas[1][1]} e tem conceito {alunas[1][2]}')
print(alunas[1][0] + ' nasceu em ' + alunas[1][1])
print(alunas[1][0], 'nasceu em', alunas[1][1])
'''

for aluna in alunas:

    if aluna[2].upper() == 'A':
        print(f'{aluna[0]} nasceu em {aluna[1]} e tem conceito {aluna[2]}')

