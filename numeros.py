# Leer los números del archivo y crear un conjunto
with open('Material Practicos/numeros.txt', 'r') as file:
    numbers = set(map(int, file.read().split())) # Mejor implementación que con readlines().

# Calcular la suma del conjunto
total_sum = sum(numbers)

# Contar números impares
odd_count = sum(1 for num in numbers if num % 2 != 0)

# Calcular el promedio de los números pares
even_numbers = [num for num in numbers if num % 2 == 0]
even_average = sum(even_numbers) / len(even_numbers) if even_numbers else 0

# Print results
print(f"Números no repetidos: {len(numbers)}") # Los conjuntos no tienen elementos repetidos.
print(f"Suma de números no repetidos: {total_sum}")
print(f"Cantidad de números impares: {odd_count}")
print(f"Promedio de números pares: {even_average:.2f}")
