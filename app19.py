# Loops aninhados

import os
os.system('cls')

pessoas = [
    ("Joca", "joca@email.com", "2000-10-14", "Senha@123", 'foto01.jpg'),
    ("Maria", "maria@email.com", "1984-08-08", "Senha@123"),
    ("Setembrino", "set@brino.com", "1978-12-15", "Senha@123", 'foto01.jpg'),
    ("Hemengarda", "hemen@garda.com", "1982-01-17", "Senha@123"),
]

# Data de nascimento do Joca
# print(pessoas[2][2])

for pessoa in pessoas:
    # Feio
    # print(pessoa)
    for dado in pessoa:
        print('•', dado)
    print()