import csv
from abc import ABC, abstractmethod


class Inmueble(ABC):
    def __init__(self, codigo, propietario, alquiler_base, superficie):
        self.codigo = codigo
        self.propietario = propietario
        self.alquiler_base = alquiler_base
        self.superficie = superficie

    def __str__(self) -> str:
        return f"{self.propietario}, Alquiler base: $ {self.alquiler_base}, Superficie {self.superficie} m2"

    @property
    @abstractmethod
    def importe(self):
        pass


class Casa(Inmueble):
    def __init__(
        self, codigo, propietario, alquiler_base, superficie, habitaciones, tiene_pileta
    ):
        super().__init__(codigo, propietario, alquiler_base, superficie)
        self.habitaciones = habitaciones
        self.tiene_pileta = tiene_pileta

    def __str__(self) -> str:
        return f"{super().__str__()}, Habitaciones: {self.habitaciones}, {'Tiene Pileta' if self.tiene_pileta == 1 else 'No Tiene Pileta'}"
    
    @property
    def importe(self):
        return (
            self.alquiler_base + self.habitaciones * 30000 + self.tiene_pileta * 100000
        )

class Departamento(Inmueble):
    def __init__(self, codigo, propietario, alquiler_base, superficie, expensas, piso):
        super().__init__(codigo, propietario, alquiler_base, superficie)
        self.expensas = expensas
        self.piso = piso

    def __str__(self) -> str:
        return f"{super().__str__()}, Expensas ${self.expensas}, Piso {self.piso}"

    @property
    def importe(self):
        return self.alquiler_base + self.expensas + (20000 if self.piso < 3 else 0)


class Inmobiliaria:
    def _cargar_csv(self, file_path):
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                tipo, codigo, propietario, alquiler_base, superficie, *extras = row
                alquiler_base = float(alquiler_base)
                superficie = float(superficie)

                if int(tipo) == 1:
                    habitaciones, tiene_pileta = map(int, extras)
                    inmueble = Casa(
                        codigo,
                        propietario,
                        alquiler_base,
                        superficie,
                        habitaciones,
                        tiene_pileta,
                    )
                else:
                    expensas, piso = float(extras[0]), int(extras[1])
                    inmueble = Departamento(
                        codigo, propietario, alquiler_base, superficie, expensas, piso
                    )
                self.inmuebles.append(inmueble)

    def __init__(self, file_path="modelo_parcial_3/inmuebles.csv") -> None:
        self.inmuebles = []
        self._cargar_csv(file_path)

    def __str__(self) -> str:
        return (
            "-- Informe para Inmobiliaria -- \n"
            + "\n".join(str(i) for i in self.inmuebles)
            + "\n"
            + "-" * 30
        )

    def suma_alquileres(self):
        return sum(i.importe for i in self.inmuebles)
    
    def cantidad_casas_premium(self):
        casas = [i for i in self.inmuebles if isinstance(i, Casa)]        
        return sum(1 for casa in casas if (casa.superficie > 150 and casa.habitaciones > 2 and casa.tiene_pileta == 1))        
    
    def propietario_alquiler_minimo(self):
        departamentos = [i for i in self.inmuebles if isinstance(i, Departamento)]
        minimo = min(departamentos, key=lambda d:d.importe)
        return minimo.propietario