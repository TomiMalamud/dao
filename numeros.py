# Leer los números del archivo y crear un conjunto
with open('Material Practicos/numeros.txt', 'r') as file:
    numbers = set(map(int, file.read().split()))

# Calcular la suma del conjunto
total_sum = sum(numbers)

# Contar números impares
odd_count = sum(1 for num in numbers if num % 2 != 0)

# Calcular el promedio de los números pares
even_numbers = [num for num in numbers if num % 2 == 0]
even_average = sum(even_numbers) / len(even_numbers) if even_numbers else 0

# Print results
print(f"Non-duplicate numbers: {len(numbers)}")
print(f"Sum of non-duplicate numbers: {total_sum}")
print(f"Quantity of odd numbers: {odd_count}")
print(f"Average of even numbers: {even_average:.2f}")
