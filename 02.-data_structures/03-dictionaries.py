# Definicion de un diccionario en python mediante llaves
user = {'name': 'jhon', 'age': 23}
print(user)

# Definicion de un diccionario en python mediante la funcion dict
user = dict({'name': 'jhon', 'age': 23})
print(user)


# para obtener un valor dentro del diccionario debemos
# indicar la llave que almacena dicho valor dentro del diccionario
framework = {'name': 'Reactjs', 'language': 'JavaScript'}
framework_name = framework['name']
print(framework_name)

# para actualizar un valor dentro del diccionario debemos
# indicar la llave que almacena dicho valor dentro del diccionario
# e indicar el nuevo valor que almacenara
framework['name'] = 'Vuejs'
print(framework)

# Para obtener todas las llaves de un diccionario nos apoyaremos 
# del metodo keys
print(tuple(framework.keys()))

# Para obtener todas los valores de un diccionario nos apoyaremos 
# del metodo values
print(tuple(framework.values()))

# Para recorrer un diccionaria lo haremos apoyandonos de un ciclo
# for y el metodo items
for k, v in framework.items():
    print(k, v)

# Otra forma de obtener un elemento del diccionario es por medio
# del metodo get, lo interesante de hacerlo de esta forma es 
# que si la llave no existe dentro del diccionario podemos
# setear un default, si el default no es seteado el metodo get, 
# retorna none protegiendonos de cualquier error que pudiese
# lanzar el programa al no encontar la llave
framework_age = framework.get('age', 'No disponible')
print(framework_age)

# Para agregar elementos al diccionario basta con definir el nombre
# de la llave entre corchetes y su valor, si la llave ya existe python
# solo actualiza el valor de la llave
framework['age'] = 3
print(framework)

# Para saber si una llave existe en el diccionario nos apoyamos de la
# palabra reservada in
print('someKey' in framework)

# Otra forma de obtener una llave de un diccionario es por medio
# del metodo setdefault, si la llave no existe sera creada en el
# diccionario y nos sera devuelta
some_key_value = framework.setdefault('someKey', 'someValue')
print(some_key_value)
print(framework)

# Para eliminar una llave de un diccionario nos apoyaremos en 
# la palabra reservada del, es necesario antes de eliminar una
# llave de un diccionario validar que esta exista
del framework['someKey']
print(framework)

# Otra forma de eliminar una llave es por medio del metodo pop
framework.pop('age')
print(framework)

# Para eliminar todos los elementos de un diccionario lo hacemos
# mediante el metodo clear.
framework.clear()
print(framework)