from classes import *

def main():
    empresa = Empresa()
    print(empresa)

    print(f"La suma de ganancias es {empresa.suma_ganancia()}")
    print(f"Cantidad de locales no rentables {empresa.no_rentables()}")
    nro, tipo = empresa.mas_rentable()
    print(f"Local más rentable es el nro. {nro}, es un {tipo}")
    
if __name__ == "__main__":
    main()