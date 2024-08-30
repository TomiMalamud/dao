import csv

def read_personas():
    personas = {}
    with open('Material Practicos/personas.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) == 4:
                id_number, first_name, last_name, age = row
                personas[id_number] = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'age': int(age)
                }
    return personas

# Create the dictionary
personas_dict = read_personas()

print("-"*30)
print('Menu')
print('1. Buscar por DNI')
print('2. Buscar por apellido')
print('3. Mostrar promedio de edades')
print('4. Salir')

while True:
    print("-"*30)
    option = input('Ingrese una opción: ')
    if option == '1':
        dni = input('Ingrese el DNI: ')
        persona = personas_dict.get(dni)
        if persona:
            print(f'Nombre: {persona["first_name"]} {persona["last_name"]}, Edad: {persona["age"]} años')
        else:
            print('Persona no encontrada')
    elif option == '2':
        apellido = input('Ingrese el apellido: ')
        personas_con_apellido = [persona for persona in personas_dict.values() if persona['last_name'] == apellido]
        for persona in personas_con_apellido:
            print(f'DNI: {dni}, Nombre: {persona["first_name"]} {persona["last_name"]}, Edad: {persona["age"]}')
    elif option == '3':
        edades = [persona['age'] for persona in personas_dict.values()]
        promedio = sum(edades) / len(edades)
        print(f'El promedio de edades es: {promedio:.2f}')
    elif option == '4':
        break
    else:
        print('Opción no válida')