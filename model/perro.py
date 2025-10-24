from animal import Animal

class Perro(Animal):
    def __init__(self, edad, especie, voz, raza):
        super().__init__(edad, especie, voz)
        self.raza = raza
        print(f"Es un {self.especie} de raza {self.raza}")
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! ¡Soy un {self.especie} de raza {self.raza} y mi labor es cuidar a mis dueños")
