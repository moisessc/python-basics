# El ciclo foreach en python permite iterar estructuras de
# datos como las listas

# Ejemplo de un ciclo foreach iterando una lista
users = ['user1', 'user2', 'user3']
for user in users:
    print(f'{user}')

print('---------------------------------------')

# Ejemplo de un ciclo foreach iterando un objeto range,
# la funcion range nos permite generar una secuencia de numeros
# teniendo como limite el valor que pasemos por parametro
# de esta forma es como en python hariamos un ciclo for
# convencional, range tambien nos permite definir a partir
# de que numero se desea iniciar la iteracion, ademas tambien
# nos permute definir saltos de n canrtidad al momento de generar
# los valores
# range(6) --> genera numeros del 0 al 5 (Por defecto range inicia en 0)
# range(1, 11) --> genera numeros a partir del 1 hasta el 10
# range(1, 11, 2) --> genera numeros a partir del 1 hasta el 10 dando
#                     saltos de 2 en 2
for value in range(1, 11, 2):
    print(value)

print('---------------------------------------')

# Ejemplo de un ciclo foreach iterando un objeto enumerate, 
# el cual nos permite generar un iterable con indices a
# partir de por ejemplo una lista o una tupla.
# la funcion enumerate permite definir a partir de que numero
# se desea que comience la generacion de indices indicandolo
# como segundo parametro, por defeco comienza en 0.
frameworks = ['Reactjs', 'Vuejs', 'Svelt', 'Angular']
for index, user in enumerate(frameworks, 10):
    print(f'Index: {index} Framework: {user}')

print('---------------------------------------')

# Ejemplo de un ciclo foreach iterando un diccionario
user = {'name': 'Jhon', 'age': 23, 'country':'USA'}
for _, value in user.items():
    print(value)
