# La palabra reservada break nos permite finalizar
# de forma abrupta el flujo de un ciclo
for number in range(11):
    if number == 7:
        break
    print(number)

print('------------------------------------------')

# La palabra reservada continue nos permite saltar
# una iteracion de un cilo.
for number in range(11):
    if number == 7:
        continue
    print(number)