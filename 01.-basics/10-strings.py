# En python es posible convertir un string a una lista
# por medio del metodo split, o tambien es posible converitir
# una lista a un string por medio del metodo join.
name = 'Jhon Smith Rain'
# Convirtiendo un string a una lista, el metodo split puede
# recibir por parametro el caracter por el cual queremos
# que se divida la lista, por defecto es ' '
list_name = name.split()
print(type(list_name))
print(list_name)

# Convirtiendo una lista a un string, entre las comillas se 
# especifica el caracter por el cual deseamos unir cada
# elemento de la lista
name = ' '.join(list_name)
print(type(name))
print(name)

print('---------------------------------------------------')

# Una de la formas de concatenar strings en python es mediante
# el operador +
name = 'Jhonny'
last_name = 'Smith'
full_name = name + ' ' + last_name
print(full_name)

# Una segunda forma de concatenar strings en python es mediante %s,
# para este metodo es necesario partir de un string base, y posteriormente
# indicar las variables que tomaran el lugar del %s,  de esta forma la
# concatenacion se hace un poco mas facil de realizar.
full_name = '%s %s' %(name, last_name)
print(full_name)

# Otra forma de concatenar en python es por medio de los placeholders
# al igual que con el %s, debemos partir de un string y apoyarnos del
# metodo format
full_name = '{} {}'.format(name, last_name)
print(full_name)

# Otra forma de usar los placeholders es por medio de parametros,
# dentro de las llaves especificaremos el nombre del parametro
# y dentro del meotodo format definir el valor de los parametros
# al pasar los parametros si observamos no importa el orden en el
# que se seteen, siempre respetaran la posicion del parametro
full_name = '{param1} {param2}'.format(
    param2 = last_name,
    param1 = name,
)
print(full_name)

# Una ultima forma y la mas sencilla es por medio de la interpolacion
# para poder interpolar variables es necesario anteponer una f al string
# que estamos generando.
full_name = f'{name} {last_name}'
print(full_name)

print('---------------------------------------------------')

# Para encontrar cuantas veces un string esta presente dentro de 
# otro strings nos apoyaremos del metodo count
some_text = 'Principales conceptos basicos de Python'
# el metodo count recibe por parametro la palabra o caracter que
# se desea buscar en el string, si el caracter o palabra no se
# encuentra el metodo counbt retorna 0
counter_word = some_text.count('o')
print(f'La letra o se encuentra {counter_word} vez')

# Para saber si un caracter se encuentra en un string solo hacemos
# uso de la palabra reservada in
print('x' in some_text)

# Para saber si un string comeinza con un caracter o palabra especifica
# nos apoyaremos del metodo startswith
print(some_text.startswith('Principales'))

# Para saber si un string termina con un caracter o palabra especifica
# nos apoyaremos del metodo endsswith
print(some_text.endswith('Java'))