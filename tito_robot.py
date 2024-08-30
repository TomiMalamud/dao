import random
from typing import Tuple, Callable
from functools import reduce

Posicion = Tuple[int, int]
Direccion = str
Estado = Tuple[Posicion, Direccion]

def mover_norte(posicion: Posicion) -> Posicion:
    x, y = posicion
    return (x, min(400, y + 10))

def mover_sur(posicion: Posicion) -> Posicion:
    x, y = posicion
    return (x, max(0, y - 20))

def mover_este(posicion: Posicion) -> Posicion:
    x, y = posicion
    return (min(400, x + 10), y)

def mover_oeste(posicion: Posicion) -> Posicion:
    x, y = posicion
    return (max(0, x - 20), y)

movimientos: dict[str, Callable[[Posicion], Posicion]] = {
    'N': mover_norte,
    'S': mover_sur,
    'E': mover_este,
    'O': mover_oeste
}

def mover_robot(estado: Estado, comando: str) -> Estado:
    posicion, _ = estado
    if comando in movimientos:
        nueva_posicion = movimientos[comando](posicion)
        return (nueva_posicion, comando)
    return estado

def ejecutar_comandos(estado_inicial: Estado, comandos: str) -> Estado:
    return reduce(mover_robot, comandos, estado_inicial)

def generar_posicion_inicial() -> Posicion:
    return (random.randint(0, 400), random.randint(0, 400))

def mostrar_posicion(posicion: Posicion) -> str:
    x, y = posicion
    return f"Posición: ({x}, {y})"

def procesar_entrada(entrada: str) -> str:
    return ''.join(c for c in entrada.upper() if c in 'NSEOF')

def main():
    posicion_inicial = generar_posicion_inicial()
    estado_inicial = (posicion_inicial, 'N')
    print("Posición inicial del robot:", mostrar_posicion(posicion_inicial))

    while True:
        print("\nOpciones de movimiento:")
        print("N: Girar al norte y avanzar 10 pasos")
        print("S: Girar al sur y avanzar 20 pasos")
        print("E: Girar al este y avanzar 10 pasos")
        print("O: Girar al oeste y avanzar 20 pasos")
        print("F: Finalizar")

        entrada = input("Ingrese su comando (puede ser una secuencia, ej. 'NNEENSSNO'): ")
        comandos = procesar_entrada(entrada)

        if 'F' in comandos:
            print("Programa finalizado.")
            break

        estado_final = ejecutar_comandos(estado_inicial, comandos)
        posicion_final, _ = estado_final
        print(mostrar_posicion(posicion_final))
        estado_inicial = estado_final

if __name__ == "__main__":
    main()