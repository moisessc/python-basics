# Definicion de una tupla por medio de parentesis
months = ('January', 'February', 'March', 'April', 'May', 'Jun', 'July', 
'Agust', 'September', 'October', 'November', 'December')
print(months)

# Definicion de una tupla por medio de la funcion tuple
months = tuple(('January', 'February', 'March', 'April', 'May', 'Jun', 'July', 
'Agust', 'September', 'October', 'November', 'December'))
print(months)

print('----------------------------------------------')

# Para obtener un un elemento de la tupla nos apoyamos de los indices de la misma,
# los indices de las tuplas siempre comienzan a partir de 0 por ejemplo obtengamos
# de la siguiete tupla el elemento de la posicion 0 y 4

# por default la tupla se puede decir que se comienza a leer de izquierda a derecha
# Indices de la tupla:      0       1       2      3       4           5
# Indices de la tupla:     -6      -5      -4     -3      -2          -1
programming_languages = ('Python', 'Go', 'Java', 'Rust', 'Ruby', 'JavaScript')
print('Elemento posicion 0: ' + programming_languages[0])
print('Elemento posicion 4: ' + programming_languages[4])

# Pero en python es posible acceder a los elementos leyendolos de derecha a izquierda
# por medio de indices negativos
print('Elemento posicion -1: ' + programming_languages[-1])
print('Elemento posicion -3: ' + programming_languages[-3])

print('----------------------------------------------')

# En python es posible crear subtuplas a partir de una tupla existente
# Indices:      0              1           2         3        4
frameworks = ('ReactJs', 'Spring boot', 'Flask', 'Django', 'Vuejs')
print(f'Tupla completa: {frameworks}')

# [inicio:final] --> Obtenemos una subtupla a partir de los indices especificados
sub_list = frameworks[2:4]
print(f'Sub tupla [2:4]: {sub_list}')

# [inicio:] --> Obtenemos una subtupla a partir del indice especificado
# hasta el final de la tupla
sub_list = frameworks[2:]
print(f'Sub tupla del indice [2:]: {sub_list}')

# [:final] --> Obtenemos una subtupla a partir del inicio
# hasta el indice especificado de la tupla
sub_list = frameworks[:3]
print(f'Sub tupla del indice [:3]: {sub_list}')

# [inicio:final:salto] --> Obtenemos una subtupla a partir de los indices
# especificados pero en saltos de acuerdo a la cantidad especificada
sub_list = frameworks[1:4:2]
print(f'Sub tupla del indice [1:4:2]: {sub_list}')

# [inicio:final:salto negativo] --> Obtenemos una subtupla a partir de los indices
# especificados pero invertida
sub_list = frameworks[::-1]
print(f'Sub tupla del indice [::-1]: {sub_list}')

print('----------------------------------------------')

# En python es posible convertir una tupla a una lista y vicerversa.
databases = ('MongoDB', 'Bigtable', 'Postgresql', 'MySql')

# Convercion de una tupla a una lista
list_databases = list(databases)
print(f'Lista a partir de una tupla: {list_databases}')
print(type(list_databases))

# Conversion de una lista a una tupla
tuple_databases = tuple(list_databases)
print(f'Tupla a partir de una lista: {tuple_databases}')
print(type(tuple_databases))

print('----------------------------------------------')

# En python existe un concepto en las tuplas llamado
# desempaquetado de tuplas, el cual hace referencia 
# a obtener elementos de una tupla declarando variables
# que almacenaran el valor deacuerdo a la posicion del mismo 
# en la tupla
users = ('Jhon', 'Jhonny', 'Sam', 'Sthep', 'Carl', 'Jannet')
# Desempaquetado de una typla
user1, user2, user3, user4, user5, user6 = users
print(user1)
print(user2)
print(user3)
print(user4)
print(user5)
print(user6)
print('----')

# Si por ejemplo solo requerimos los primeros 2 elementos de la tupla
# es posible indicarselo a python, de la siguiente manera, loq ue python 
# hara es desempaquetar los primeros 2 elementos de la tupla y los
# restantes los almacenara en una lista de nombre more_users, python
# sabe que debera almacenarlos en una lista debido a que con el * le
# indicamos a python que esa variable se trata de una lista.
user1, user2, *more_users = users
print(user1)
print(user2)
print(more_users)
print('----')

# Ahora supongamos que solo queremos obtener el elmento de la posicion
# 0, el elemento de la posicion 2 y el ultimo elemento de la tupla, para
# poder realizarlo debemos ignorar ciertos elementos de la tupla y genera
# una lista con los elementos sobrantes, lo haremos de la siguiente manera:
# para ignorar un valor del desempaquetado podemos apoyarnos del _, esto 
# le indicara a python que no usaramos dicho elemento, notese que no solo
# se puede usar con 1 solo elemento sino con una lista completa.
user1, _, user3, *_, user6 = users
print(user1)
print(user3)
print(user6)

print('----------------------------------------------')

# En python con la funcion zip podemos empaquetar tuplar y listas
# de la siguiente manera
list_one = [1, 2, 3, 4, 5]
tuple_one = [10, 20, 30, 40, 50]
zip_result = tuple(zip(list_one, tuple_one))
print(f'Primer empaquetado: {zip_result}')
# con la funcion zip podemos empaquetar cuantas listas y tuplas querramos
list_two = [100, 200, 300, 400, 500]
tuple_two = [1000, 2000, 3000, 4000, 5000]
zip_result = tuple(zip(list_one, tuple_one, list_two, tuple_two))
print(f'Segundo empaquetado: {zip_result}')
# La longitud del empaquetado va en funcion de la tupla o lista de menor longitud
# es decir que la longitus de los paquetes generados por la funcion zip seran
# de la misma longitud de la lista o tupla mas pequeña, y los elementos restantes
# seran ignorados por la funcion zip como se muestra a continuacion
test_numbers = [1, 2, 3]
test_tuple_numbers = [10, 20, 30, 40, 50]
test_result = tuple(zip(test_numbers, test_tuple_numbers))
print(test_result)