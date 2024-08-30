def suma(a, b):
    return a + b

def diferencia(a, b):
    return a - b

def producto(a, b):
    return a * b

def cociente(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por 0"    

def calculadora():
    while True:
        print("\nCalculadora Básica")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        
        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                print("Resultado:", suma(num1, num2))
            elif opcion == '2':
                print("Resultado:", diferencia(num1, num2))
            elif opcion == '3':
                print("Resultado:", producto(num1, num2))
            elif opcion == '4':
                print("Resultado:", cociente(num1, num2))
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    calculadora()
