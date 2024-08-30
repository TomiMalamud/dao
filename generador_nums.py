import random
from statistics import mean, stdev
from itertools import islice

# Generar 1000 números aleatorios entre -1000000 y 1000000
numbers = list(islice((random.randint(-1000000, 1000000) for _ in iter(int, 1)), 1000))

# El menor de todos
min_number = min(numbers)

# La cantidad de pares
even_count = sum(1 for num in numbers if num % 2 == 0)

# El promedio de los impares
odd_numbers = [num for num in numbers if num % 2 != 0]
odd_average = mean(odd_numbers) if odd_numbers else 0

# El cuadrado de todos los que se encuentren entre 10 y 100 sin incluirlos
squares = [num ** 2 for num in numbers if 10 < num < 100]

# Los múltiplos de 3 del punto anterior
multiples_of_3 = [num for num in squares if num % 3 == 0]

# Todos los múltiplos de 7 ordenados en forma descendente
multiples_of_7 = sorted((num for num in numbers if num % 7 == 0), reverse=True)

# El promedio de los impares negativos
negative_odd_numbers = [num for num in numbers if num % 2 != 0 and num < 0]
negative_odd_average = mean(negative_odd_numbers) if negative_odd_numbers else 0

# La desviación estándar de todos
standard_deviation = stdev(numbers)

# Si existe o no algún múltiplo de 127
exists_multiple_of_127 = any(num % 127 == 0 for num in numbers)

# Generar una lista que contenga únicamente los que terminan en 2 o 3
ending_in_2_or_3 = [num for num in numbers if num % 10 in (2, 3)]

# Imprimir resultados
print(f"El menor número: {min_number}")
print(f"Cantidad de números pares: {even_count}")
print(f"Promedio de números impares: {odd_average}")
print(f"Cuadrados de números entre 10 y 100: {squares}")
print(f"Múltiplos de 3 de los cuadrados: {multiples_of_3}")
print(f"Múltiplos de 7 en orden descendente: {multiples_of_7}")
print(f"Promedio de impares negativos: {negative_odd_average}")
print(f"Desviación estándar de todos los números: {standard_deviation}")
print(f"¿Existe algún múltiplo de 127?: {'Sí' if exists_multiple_of_127 else 'No'}")
print(f"Números que terminan en 2 o 3: {ending_in_2_or_3}")