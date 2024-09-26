from classes import *

def main():
    inmobiliaria = Inmobiliaria()
    print(inmobiliaria)
    
    print(f"La suma de alquileres es de {inmobiliaria.suma_alquileres()}")
    print(f"Cantidad de casas premium: {inmobiliaria.cantidad_casas_premium()}")
    print(f"Propietario del alquier más bajo: {inmobiliaria.propietario_alquiler_minimo()}")

if __name__ == "__main__":
    main()