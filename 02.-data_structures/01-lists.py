# Definicion de una lista a partir de corchetes
days_of_the_week = [['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']]
print(days_of_the_week)

# Definicion de una lista a partir de la funcion list
days_of_the_week = list(['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])
print(days_of_the_week)

print('----------------------------------------------')


# Para ontener un un elemento de la lista nos apoyamos de los indices de la misma,
# los indices de las listas siempre comienzan a partir de 0 por ejemplo obtengamos
# de la siguiete lista el elemento de la posicion 0 y 4

# por default la lista se puede decir que se comienza a leer de izquierda a derecha
# Indices de la lista:      0       1       2      3       4           5
# Indices de la lista:     -6      -5      -4     -3      -2          -1
programming_languages = ['Python', 'Go', 'Java', 'Rust', 'Ruby', 'JavaScript']
print('Elemento posicion 0: ' + programming_languages[0])
print('Elemento posicion 4: ' + programming_languages[4])

# Pero en python es posible acceder a los elementos leyendolos de derecha a izquierda
# por medio de indices negativos
print('Elemento posicion -1: ' + programming_languages[-1])
print('Elemento posicion -3: ' + programming_languages[-3])

print('----------------------------------------------')


"""
Para actualiza el valor de un elemento en python es muy sencillo, basta con indicar
el indice del elemento a actualizar seguido del nuevo valor que se asignara,
"""
animals = ['dog', 'cat', 'rabbit']
print(animals)
animals[2] = 'horse'
print(animals)

print('----------------------------------------------')

# En python es posible crear subslistas a partir de una lista creada
# Indices:      0              1           2         3        4
frameworks = ['ReactJs', 'Spring boot', 'Flask', 'Django', 'Vuejs']
print(f'Lista completa: {frameworks}')

# [inicio:final] --> Obtenemos una sublista a partir de los indices especificados
sub_list = frameworks[2:4]
print(f'Sub lista [2:4]: {sub_list}')

# [inicio:] --> Obtenemos una sublista a partir del indice especificado
# hasta el final de la lista
sub_list = frameworks[2:]
print(f'Sub lista del indice [2:]: {sub_list}')

# [:final] --> Obtenemos una sublista a partir del inicio
# hasta el indice especificado de la lista
sub_list = frameworks[:3]
print(f'Sub lista del indice [:3]: {sub_list}')

# [inicio:final:salto] --> Obtenemos una sublista a partir de los indices
# especificados pero en saltos de acuerdo a la cantidad especificada
sub_list = frameworks[1:4:2]
print(f'Sub lista del indice [1:4:2]: {sub_list}')

# [inicio:final:salto negativo] --> Obtenemos una sublista a partir de los indices
# especificados pero invertida
sub_list = frameworks[::-1]
print(f'Sub lista del indice [::-1]: {sub_list}')

print('----------------------------------------------')

# Para modificar las listas en python, es decir eliminar y agregar valores
# es necesario apoyarnos del metodo append, insert, extend, remove y la palabra
# reservada del
databases = ['MongoDB', 'Bigtable', 'Postgresql', 'MySql']
print(f'Lista antes de agregar un elemento: {databases}')
# El metodo append agrega el elemento al final de la lista
databases.append('DynamoDB')
print(f'Lista despues de append: {databases}')

# El metodo insert agrega el elemento en el indice especificado
databases.insert(2, 'SQL Server')
print(f'Lista despues de insert: {databases}')

# El metodo extend agrega una lista completa a una lista ya existente sin modificar
# o afectar la lista que se agregara
other_databses = ['Redis', 'BigQuery', 'MariaDB']
databases.extend(other_databses)
print(f'Lista que se incorporara: {other_databses}')
print(f'Lista despues de extend: {databases}')

# Para eliminar un elemento de una lista es posible hacerlo de 2 formas, por medio
# del objeto perse o por medio del indice perteneciente al elemento que deseamos
# eliminar
databases.remove('Redis')
del databases[0]
del databases[1]
print(f'Lista despues de remove y del: {databases}')

# Para eliminar todos los elementos de la lista hacemos uso del metodo clear
databases.clear()
print(f'Lista despues de clear: {databases}')

print('----------------------------------------------')

# Algunos de los metodos mas utiles y usados de las listas son los siguientes:
numbers = [10, 600, 1, 400, 40, 10, 23, 340, 458]

# el metodo sort nos permite ordenar de menor a mayor una lista
numbers.sort()
print(numbers)

# Si lo que requerimos es que el ordean sea inversio, es decir de mayor a menor
# solo es necesario pasar por parametro reverse en True al metodo
numbers.sort(reverse=True)
print(numbers)

# Para obtener el valor mayor de la lista podemos usar el metodo max y para
# obtener el valor menor el metodo min
min_number = min(numbers)
max_number = max(numbers)
print(f'Numero menor:  {min_number}')
print(f'Numero mayor: {max_number}')

# Para saber si existe un elmento dentro de una lista nos apoyamos de la palabra
# reservada in
exist_12_in_numbers = 12 in numbers
print(f'Existe el numero 12 en la lista: {exist_12_in_numbers}')

# Para poder obtener el indice de un elemento en una lista nos apoyamos del metodo
# index, pero antes de otilizar el metodo es necesario estar seguros que el elemento
# existe dentro de la lista de lo contrario python nos marcara un error, el metodo
# index siempre regresara el indice de la primer coincidencia al elemento pasado
# por parametro
if 10 in numbers:
    print(f'El elemento 10, se encuentra en el indice: {numbers.index(10)}')
else:
    print('El elemento no existe en la lista')

print('----------------------------------------------')

# Debido a que en python, en las listas es posible almacenar cualquier tipo de dato,
# inclusive otras listas podemos crear matrices aprovechandonos de esto,
first_row = [1, 2, 3]
second_row = [10, 20, 30]
matrix =  [first_row, second_row]
print(f'Matriz de 2x3: {matrix}')

# Obteniendo un elemento de la matriz
print(f'Elemento en la posicion 1,1: {matrix[1][1]}')