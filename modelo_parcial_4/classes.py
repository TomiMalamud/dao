import csv
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, matricula, modelo, costo_base_mantenimiento) -> None:
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.costo_base_mantenimiento = costo_base_mantenimiento

    def __str__(self) -> str:
        return f"{self.matricula} - {self.marca} {self.modelo} - $ {self.costo_base_mantenimiento}"
    
    @property
    @abstractmethod
    def costo_mantenimiento(self):
        pass

class Auto(Vehiculo):
    def __init__(self, marca, matricula, modelo, costo_base_mantenimiento, kilometraje) -> None:
        super().__init__(marca, matricula, modelo, costo_base_mantenimiento)
        self.kilometraje = kilometraje
    
    def __str__(self) -> str:
        return f"{super().__str__()} - {self.kilometraje} km"
    
    @property
    def costo_mantenimiento(self):
        return self.costo_base_mantenimiento + (self.costo_base_mantenimiento * 0.1 if self.kilometraje > 100000 else 0)


class Camioneta(Vehiculo):
    def __init__(self, marca, matricula, modelo, costo_base_mantenimiento, capacidad) -> None:
        super().__init__(marca, matricula, modelo, costo_base_mantenimiento)
        self.capacidad = capacidad
    
    def __str__(self) -> str:
        return f"{super().__str__()} - {self.capacidad} kg"
    
    @property
    def costo_mantenimiento(self):
        return self.costo_base_mantenimiento + (self.costo_base_mantenimiento * 0.15 if self.capacidad > 1000 else 0)
    
class Moto(Vehiculo):
    def __init__(self, marca, matricula, modelo, costo_base_mantenimiento, cilindrada) -> None:
        super().__init__(marca, matricula, modelo, costo_base_mantenimiento)
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        return f"{super().__str__()} - {self.cilindrada} cc"
    
    @property
    def costo_mantenimiento(self):
        return self.costo_base_mantenimiento + (self.costo_base_mantenimiento * 0.2 if self.cilindrada > 500 else 0)
    

class Empresa():
    def _cargar_csv(self, file_path):
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                tipo, marca, matricula, modelo, costo_base_mantenimiento, extra = row[:6]            
                costo_base_mantenimiento, extra = float(costo_base_mantenimiento), float(extra)

                if int(tipo) == 1:
                    vehiculo = Auto(marca, matricula, modelo, costo_base_mantenimiento, extra) # Kilometraje
                elif int(tipo) == 2:
                    vehiculo = Camioneta(marca, matricula, modelo, costo_base_mantenimiento, extra) # Capacidad
                else: 
                    vehiculo = Moto(marca, matricula, modelo, costo_base_mantenimiento, extra) # Cilindrada

                self.vehiculos.append(vehiculo)

    def __init__(self, file_path="modelo_parcial_4/vehiculos.csv") -> None:
        self.vehiculos = []
        self._cargar_csv(file_path)
    
    def __str__(self) -> str:
        return f"---- Listado de vehículos ----\n" + "\n".join(str(v) for v in self.vehiculos) + "\n" + "-" * 30
