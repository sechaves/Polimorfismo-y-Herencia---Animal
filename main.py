from animal import Animal
from model.leon import Leon
from model.aguila import Aguila
from model.gallo import Gallo
from model.gato import Gato
from model.perro import Perro

aguila1 = Aguila(edad=3, especie="Aguila", voz="Kaaauuuuu", habitat="Montañas")
leon1 = Leon(edad=12, especie="Leon", voz="Rooar!!", dominancia="Rey")
perro1 = Perro(edad=7, especie="Perro", voz="Guau", raza="Poodle")
gato1 = Gato(edad=5, especie="Gato", voz="Miaauuu", color_ojos="verdes")
gallo1 = Gallo(edad=1, especie="Gallo", voz="Kikiriki", hora_de_cantar="6:00")

zoologico = [aguila1, leon1, perro1, gato1, gallo1]

for animal in zoologico:
    animal.reproducir_voz()
    animal.comer()