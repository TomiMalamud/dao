import csv
from abc import ABC, abstractmethod


class Sucursal(ABC):
    def __init__(self, numero: int, superficie: float, facturacion: float) -> None:
        self.numero = numero
        self.superficie = superficie
        self.facturacion = facturacion
    
    def __str__(self) -> str:
        return f"Sucursal Nro. {self.numero}, {self.superficie} m2, ${self.facturacion}, Rentabilidad: {self.rentabilidad:.2f}"

    @abstractmethod
    def rdo_comercial(self):
        pass
    
    @property
    def rentabilidad(self):
        if self.superficie > 0:
            return self.rdo_comercial() / self.superficie
        else:
            raise ValueError("La superficie debe ser mayor a 0.")


class Hiper(Sucursal):
    def __init__(
        self,
        numero: int,
        superficie: float,
        facturacion: float,
        importe_alquileres: float,
    ):
        super().__init__(numero, superficie, facturacion)
        self.importe_alquileres = importe_alquileres
        self.minimo_rentable = 50

    def rdo_comercial(self):
        return self.facturacion + self.importe_alquileres

    def __str__(self) -> str:
        return f"{super().__str__()}, Resultado Comercial: {self.rdo_comercial()}"

class Super(Sucursal):
    def __init__(
        self, numero: int, superficie: float, facturacion: float, es_mayorista: int
    ):
        super().__init__(numero, superficie, facturacion)
        self.es_mayorista = es_mayorista
        self.minimo_rentable = 45 if es_mayorista == 1 else 40

    def rdo_comercial(self):
        return self.facturacion

    def __str__(self) -> str:
        return f"{super().__str__()}, Resultado Comercial: {self.rdo_comercial()}"

class Mini(Sucursal):
    def __init__(
        self, numero: int, superficie: float, facturacion: float, alquiler_pagado: float
    ):
        super().__init__(numero, superficie, facturacion)
        self.alquiler_pagado = alquiler_pagado
        self.minimo_rentable = 35

    def rdo_comercial(self):
        return self.facturacion - self.alquiler_pagado

    def __str__(self) -> str:
        return f"{super().__str__()}, Resultado Comercial: {self.rdo_comercial()}"

class Empresa:
    def _cargar_csv(self, file_path):
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                tipo, numero, superficie, facturacion, extra = line

                if int(tipo) == 1:
                    sucursal = Hiper(
                        int(numero), float(superficie), float(facturacion), float(extra)
                    )  # Extra es importe_alquileres
                elif int(tipo) == 2:
                    sucursal = Super(
                        int(numero), float(superficie), float(facturacion), int(extra)
                    )  # Extra es es_mayorista
                else:
                    sucursal = Mini(
                        int(numero), float(superficie), float(facturacion), float(extra)
                    )  # Extra es alquiler_pagado

                self.sucursales.append(sucursal)

    def __init__(self, file_path="modelo_parcial_2/sucursales.csv"):
        self.sucursales = []
        self._cargar_csv(file_path)

    def __str__(self) -> str:
        return f"--- Lista de Sucursales ---\n" + "\n".join(str(s) for s in self.sucursales) + "\n" + "-" * 30
    
    def suma_ganancia(self):
        return sum(s.rdo_comercial() for s in self.sucursales)
    
    def no_rentables(self):
        return sum(s.rentabilidad < s.minimo_rentable for s in self.sucursales)

    def mas_rentable(self):
        max_rentabilidad = max(self.sucursales, key=lambda s: s.rentabilidad)
        return max_rentabilidad.numero, type(max_rentabilidad).__name__