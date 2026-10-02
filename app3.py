# Tomando decisões com 'if elif else'

age = 22
has_invitation = False
is_vip = True

if is_vip:
    print('Que bom ver você novamente')    

elif age >= 18 and has_invitation:
    print("Entrada permitida") 

else: 
    print("Entrada não permitida") 

print("Acabou")

