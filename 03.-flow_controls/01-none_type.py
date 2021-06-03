# El tipo de dato None permite definir un valor vacio, regularmente
# None es usado para representar la ausencia de algun valor, esto nos
# ayuda a definir variables que simplemente por el momento no tendran
# algun valor pero que a lo largo de la ejecucion del programa puedan
# llegar a tenerlo.

# Una caracteristica interesante de None es que python lo toma como un
# valor False en estructuras condicionales, de hecho en pytho existen 8
# formas diferentes de representar un valor False:
# 1.- False
# 2.- None
# 3,- 0
# 4.- 0.0
# 5.- '' / ""
# 6.- []
# 7.- ()
# 8.- {}
# Por consiguiente todas las representaciones anteriores que contengan
# algun valor seran representadas como True por python
simple_varible = None
print(simple_varible)
print(type(simple_varible))

simple_varible = [1, 2, 3]
print(simple_varible)
print(type(simple_varible))


