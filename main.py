# --- Archivo: main.py ---

# 1. Importaciones de tus animales (¡perfecto!)
from animal import Animal
from model.leon import Leon
from model.aguila import Aguila
from model.gallo import Gallo
from model.gato import Gato
from model.perro import Perro

# 2. ¡IMPORTAMOS EL SERVICIO DE FIREBASE!
from firebase_config import FirebaseRealtime

try:
    # 3. INICIALIZAMOS LA CONEXIÓN A FIREBASE
    #    (Asegúrate de poner tu URL y JSON en firebase_service.py)
    print("Conectando a Firebase...")
    db_service = FirebaseRealtime(base_path="zoologico")

    print("\n--- Creando instancias ---")
    
    # 4. Tu código de creación de animales (¡perfecto!)
    aguila1 = Aguila(edad=3, especie="Aguila", voz="Kaaauuuuu", habitat="Montañas")
    leon1 = Leon(edad=12, especie="Leon", voz="Rooar!!", dominancia="Rey")
    perro1 = Perro(edad=7, especie="Perro", voz="Guau", raza="Poodle")
    gato1 = Gato(edad=5, especie="Gato", voz="Miaauuu", color_ojos="verdes")
    gallo1 = Gallo(edad=1, especie="Gallo", voz="Kikiriki", hora_de_cantar="6:00")
    
    # Tu zoológico (¡perfecto!)
    zoologico = [aguila1, leon1, perro1, gato1, gallo1]

    # 5. ¡GUARDAMOS CADA ANIMAL EN FIREBASE!
    print("\n--- Guardando en Firebase ---")
    for animal in zoologico:
        # El método 'save_animal' lo añadimos a firebase_service.py
        db_service.save_animal(animal)

    # 6. Tu demostración de Polimorfismo (¡perfecto!)
    print("\n--- Demostración de Polimorfismo (Consola) ---")
    for animal in zoologico:
        animal.reproducir_voz()
        animal.comer()

except Exception as e:
    # Capturamos cualquier error (ej. si falla la conexión a Firebase)
    print(f"\n--- ERROR CRÍTICO ---")
    print(f"No se pudo ejecutar el programa: {e}")
    print("Revisa tu 'credentials.json' y la URL en 'firebase_service.py'")