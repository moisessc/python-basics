"""   
    Los operadores lógicos son los siguientes:
    AND
    OR
    NOT
"""
#         ( false )    ( true )    (       false        )
result = 100 < 90 and 200 > 100 and (200 == 10 or 50 < 20)

#  El resultado seria false
print(result)

# El resultado seria true
print(not result)
