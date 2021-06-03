# El bloque de las condicionales en python se rigen por identacion
# a diferencia de otros lenguajes de programacion que se rigen por
# un juego de llaves, por convencion se hace uso de 4 espacios como
# identacion para definir un nuevo bloque.

user_age = 12
# Ejemplo del uso de un condicional simple
if user_age >= 18 :
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')


# Ejemplo del uso de un condicional con operadores lógicos
simple_range  = 8
if simple_range >= 8 and simple_range <= 10:
    print('Estas dentro del rango :)')
else:
    print('No estas dentro del rango :(')

# Ejemplo del uso de uso de elif\
average = 5
if average == 10:
    print('Felicidades, promedio excelente!!')
elif average == 9 or average == 8:
    print('Felicidades, promedio aprobatorio')
elif average == 7 or average == 6:
    print('Promedio aprobatorio')
else:
    print('Promedio muy bajo (Reprobatorio)')

# Ejemplo de un operador ternario, permite condicionar el valor de una
# variable a partir del resultado de la expresion en una sola linea de codigo
average = 6
color = 'Verde' if average >= 6 and average <=10 else 'Rojo'
print(f'Promedio: {average} Color: {color}')