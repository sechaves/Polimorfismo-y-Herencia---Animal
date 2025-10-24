from animal import Animal

class Gallo(Animal):
    def __init__(self, edad, especie, voz, hora_de_cantar):
        super().__init__(edad, especie, voz)
        self.hora_de_cantar = hora_de_cantar 
        print(f"Su hora de cantar es a las: {self.hora_de_cantar} de la mañana.")
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! ¡Soy un {self.especie} mi labor es cantar a las {self.hora_de_cantar} de la mañana.")
