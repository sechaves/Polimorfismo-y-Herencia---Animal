from animal import Animal

class Aguila(Animal):
    def __init__(self, edad, especie, voz, habitat):
        super().__init__(edad, especie, voz)
        self.habitat = habitat  
        print(f"Su habitat o bioma usual es: {self.habitat}.")
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! ¡Soy un {self.especie} y vivo en las {self.habitat}")
