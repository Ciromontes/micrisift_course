class Asignaciones:
    def __init__(self, colaborador):
        self.plataforma = colaborador
        self.acomodador = colaborador
        self.microfonos = colaborador

asignaciones_plataforma= Asignaciones
asignaciones_plataforma.plataforma = (str("hermano 1"))

asignaciones_microfono= Asignaciones
asignaciones_microfono.microfonos= (str("hermano 2"))

asignaciones_acomodador = Asignaciones
asignaciones_acomodador.acomodador= (str("hermano3"))
print(asignaciones_plataforma.plataforma) # "The Elevator company"
print(asignaciones_microfono.microfonos)
print(asignaciones_acomodador.acomodador) # "The Elevator company"
