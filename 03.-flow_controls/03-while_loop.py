# El ciclo while nos permite repetir un bloque hasta que cierta 
# condicion se cumpla y en pytho se define de la siguiente manera:

number = 12345678
digits_counter = 0
copy_number = number

while copy_number >= 1:
    digits_counter += 1
    copy_number /= 10
# Una peculiaridad del ciclo while en python es que nos permite
# definir una sentencia else cuando la exprecion no se cumple, lo
# cual hace posible definir cierto comportamiento especificamente
# cuando la condicion que rige el ciclo ya no se cumple
else:
    print(f'Número: {number} - Dígitos: {digits_counter}')
