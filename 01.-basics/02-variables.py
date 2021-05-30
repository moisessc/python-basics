"""
Estructura de las variables en python
<nombre_variable> = <valor>
"""
name = 'Jhon'
print(name)

"""
Para modificar el valor de una variable en tiempo de ejecución ya definida, 
solo es necesario volver a llamarla y setear el nuevo valor.
"""
name = "New value"
print(name)

"""
Siempre que el nombre de una variable contenga 2 palabras se hara uso 
de la nomenclatura snake case, en donde las palabras se separan por _ 
y todas las letras se colocan en minuscula.
"""
user_age = 15
print(user_age)

"""
Si se requiere declarar multiples variables en python es posible hacerlo
en una solo linea, es recomendable no declarar mas de 3 variables en una sola
linea debido a que el codigo se hace dificil de leer.
"""
country, city, cp = 'USA', 'LA', 1234
print(country)
print(city)
print(cp)
