from classes import *


def main():
    maquina = Maquina()
    print(maquina)

    print(f"Costo total de los mantenimientos: {maquina.suma_gastos()}")
    print(f"Cantidad de mantenimientos 'caros': {maquina.cantidad_mant_caros()}")
    fecha, operario = maquina.rotura_mas_larga()
    print(f"Rotura más larga: Fecha: {fecha}, Operario: {operario}")


if __name__ == "__main__":
    main()
