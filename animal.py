#Autor: Sergio Gabriel Chaves Mosquera
#Asignación: Polimorfismo y Herencia

class Animal:
    def __init__(self, edad, especie, voz):
        self.edad = edad
        self.especie = especie
        self.voz = voz
        print(f"Creando un {self.especie} con {self.edad} años")
        
    def reproducir_voz(self):
        print(f"El {self.especie} dice: ¡{self.voz}!")
        
    def comer(self):
        print(f"El {self.especie} esta comiendo.")
        
        
        
        