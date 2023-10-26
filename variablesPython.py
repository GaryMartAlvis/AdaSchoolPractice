var_numero_int = 52
var_numero_float = 2.5235
var_string = 'Hola mundo'
var_boolean = True

var_concatenada = f'Concatenacion de variables: {str(var_numero_int)} + {str(var_numero_float)} + {var_string} + {str(var_boolean)}'
print(var_concatenada)

'''
El tipo de variable int permite almacenar números enteros, pero solo puede almacenar números desde -231 hasta 231-1, es decir, el 
número más pequeño que puede almacenar es el -2.147.483.648 y el número más grande que puede almacenar es el 2.147.483.647.

El tipo de datos FLOAT contiene una aproximación de exponente y fracción, en base 2, de 64 bits, de un número real. Esto da un 
rango de valores entre +-1.7E-308 and +- 1.7E+308.
'''

'''
Ejercicio.
Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar 
el resultado en una variable.
Imprimir los resultados de las tareas anteriores
'''

numero = [2,6,5,8,9,10,45,15,12,8,9,5]
suma_numeros_pares = 0

for i in numero:
    if i % 2 == 0:
        suma_numeros_pares += i

print(suma_numeros_pares)



