from animal import Animal

class Gato(Animal):
    def __init__(self, edad, especie, voz, color_ojos):
        super().__init__(edad, especie, voz)
        self.color_ojos = color_ojos 
        print(f"Su color de ojos es: {self.color_ojos}.")
        
    def reproducir_voz(self):
        print(f"¡{self.voz.upper()}! ¡Soy un {self.especie} y soy el unico gato con ojos de color {self.color_ojos} en la casa.")
