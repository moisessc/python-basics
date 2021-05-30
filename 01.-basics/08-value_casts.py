age = '12'
height = '1.67'
is_empty = 'False'

# Para castear tipos de datos nos apoyamos de la funcion correspondiente
# al valor que deseamos castear.
age = int(age)
print(type(age))

height = float(height)
print(type(height))

is_empty = bool(is_empty)
print(type(is_empty))

age = str(age)
print(type(age))