"""
    Los operadores relacionales son los siguientes:
    > Mayor que
    < Menor que
    >= Mayor igual que
    <= Menor igual que
    == Igual que
    != Diferente de
"""
	
result  = False
age = 24
name = "Jhonny"

# El resultado seria false, por que age es mayor que 10
result = age < 10
print(result)

#  El resultado seria true, por que age es mayor que 10
result = age > 10
print(result)

#  El resultado seria true, por que age es igual que 24
result = age >= 24
print(result)

# // El resultado seria false, por que age es mayor que 23
result = age <= 23
print(result)

# // El resultado seria true, por que age es igual que 24
result = age == 24
print(result)

# // El resultado seria true, por que age es diferente de 20
result = age != 20
print(result)

# // El resultado seria true, por que name es igual a Moises
result = name == "Jhon"
print(result)

# // El resultado seria true, por que name es diferente de Carlos
result = name != "Carlos"
print(result)
