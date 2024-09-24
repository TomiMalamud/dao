import csv
from abc import ABC, abstractmethod

class Mantenimiento(ABC):
    def __init__(self, operario, fecha, importe):
        self.operario = operario
        self.fecha = fecha
        self.importe = importe

    def __str__(self):
        return f"Operario: {self.operario}, Fecha: {self.fecha}, Importe: {self.importe}"

    @abstractmethod
    def get_costo(self):
        pass

class Correctivo(Mantenimiento):
    def __init__(self, operario, fecha, importe, horas, importe_tecnico):
        super().__init__(operario, fecha, importe)
        self.horas = horas
        self.importe_tecnico = importe_tecnico

    def __str__(self):
        return f"{super().__str__()}, Horas: {self.horas}, Importe del Técnico: {self.importe_tecnico}"

    def get_costo(self):
        return self.importe + self.importe_tecnico

class Preventivo(Mantenimiento):
    def __init__(self, operario, fecha, importe, resultado, insumos):
        super().__init__(operario, fecha, importe)
        self.resultado = resultado
        self.insumos = insumos
    
    def __str__(self):
        return f"{super().__str__()}, Resultado: {self.resultado}, Insumos: {self.insumos}"

    def get_costo(self):
        return self.importe + self.insumos

class Maquina:
    def __init__(self, file_path="modelo_parcial_1/mantenimientos.csv"):
        self.mantenimientos = []
        self._cargar_csv(file_path)

    def _cargar_csv(self, file_path):
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                tipo, fecha, operario, importe, *extra = row
                importe = float(importe)
                
                if int(tipo) == 1:
                    resultado, insumos = map(int, extra)
                    mantenimiento = Preventivo(operario, fecha, importe, resultado, insumos)
                else:
                    horas, importe_tecnico = int(extra[0]), float(extra[1])
                    mantenimiento = Correctivo(operario, fecha, importe, horas, importe_tecnico)
                
                self.mantenimientos.append(mantenimiento)

    def __str__(self):
        return "-- Informe de Mantenimientos --\n" + \
               "\n".join(str(m) for m in self.mantenimientos) + \
               "\n" + "-" * 30

    def suma_gastos(self):
        return sum(m.get_costo() for m in self.mantenimientos)

    def cantidad_mant_caros(self):
        return sum(1 for m in self.mantenimientos if m.get_costo() > 10000)

    def rotura_mas_larga(self):
        mantenimientos_correctivos = [m for m in self.mantenimientos if isinstance(m, Correctivo)]
        if not mantenimientos_correctivos:
            return "No hay mantenimientos correctivos."
        
        mant_max_duracion = max(mantenimientos_correctivos, key=lambda m: m.horas)
        return mant_max_duracion.operario, mant_max_duracion.fecha