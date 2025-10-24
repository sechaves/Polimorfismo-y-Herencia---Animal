from animal import Animal

class Leon(Animal):
    def __init__(self, edad, especie, voz, dominancia):
        super().__init__(edad, especie, voz)
        self.dominancia = dominancia #dominancia se refiere a la posicion o rango en la estructura social de la manada
        print(f"Su rango en la manada es el de {self.dominancia}.")
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! ¡Soy un {self.especie} y soy el {self.dominancia} en esta selva!")
