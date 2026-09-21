name = input("Qual seu nome? ")
age = input("Qual sua idade? ")

print(type(name))
print(type(age))

age = int(age)

older = age + 10
print(f"{name} terá {older} daqui a 10 anos.")