"""
    Para obtener datos del usuario por medio del teclado nos apoyamos de
    la funcion input, esta funcion devolvera todo lo que el usuario haya 
    escrito hasta que presione enter, toda la informacion ingresada por
    el usuario es devuelta en un tipo de dato string, por lo que si es
    necesario debera ser parseada al tipo de dato que se requiera.
"""
user_name = input('Ingrese su nombre: ')
# Parseo de un string a un int
user_age = int(input('Ingrese su edad: '))	
# Parseo de un string a un float
user_height = float(input('Ingresa tu estatura: '))

"""
De esta forma tambien se puede formatear un mensaje por pantalla, para el
caso especifico del tipo de dato flotante se formatea que solo muestre
2 digitos despues del punto decimal.
"""
print(f'Hola {user_name} tu edad es: {user_age} años, tu altura es: {user_height} mts.')


	

