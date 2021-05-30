# String
"""
En python para poder definir una variable de tipo string
basta con definir el valor de la variable con '' ó ""
de esta forma python interpreta que la variable almacenara
un tipo de dato string.
"""
print("==========================")
print("          STRING          ")
print("==========================")
user_full_name = 'James Potter'
print(user_full_name)
print("-----------------------")
"""
Cuando usar '' y cuando "", es completamente a gusto del desarrollador
pero es habitual user una u otra cuando el texto que almacenara contenga
'' ó "" por ejemplo:
"Hello world" ==> para este caso lo ideal es que usemos ''
'Hello world' ==> para este caso lo ideal es que usemos ""
"""
message_one = '"Hello world"'
message_two = "'Hello world'"
print(message_one)
print(message_two)
print("-----------------------")
"""
Si el texto a almacenar contiene saltos de lineas podemos almacenarlo en
una variable de la siguiente manera
"""
message = '''Message:
Hello world
Hello world
Hello world'''
print(message)

# Int
"""
En python para definir una variable con un tipo de dato entero solo es necesario
definir el valor, obviamente el valor debe ser de tipo entero, es decir sin punto
decimal y python lo interpretara como un valor de tipo int.
"""
print("==========================")
print("            INT           ")
print("==========================")
user_age = 12
print(user_age)

# Float
"""
En python para definir una variable con un tipo de dato flotante solo es necesario
definir el valor, obviamente el valor debe ser de tipo flotante, es decir con punto
decimal y python lo interpretara como un valor de tipo float.
"""
print("==========================")
print("          FLOAT           ")
print("==========================")
product_price = 59.90
print(product_price)

# Bool
"""
En python para definir una variable con un tipo de dato booleano solo es necesario
definir el valor, para definir el valor booleano haremos uso de las palabras reservadas
True y False
"""
print("==========================")
print("           Bool           ")
print("==========================")
is_empty = False
print(is_empty)