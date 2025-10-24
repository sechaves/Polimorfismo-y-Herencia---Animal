# --- Archivo: firebase_service.py ---

import json
import os
from typing import Any, Dict, Optional

try:
    # Asegúrate de import 'db'
    import firebase_admin
    from firebase_admin import credentials, db
except Exception:
    firebase_admin = None
    credentials = None
    db = None

class FirebaseRealtime:
    """
    Servicio de acceso a Firebase Realtime Database.
    """

    def __init__(self, base_path: str = "zoologico"): # Cambié "accounts" por "zoologico"
        self._ensure_sdk()
        self.base_path = base_path.strip("/")

    def _ensure_sdk(self):
        if firebase_admin is None:
            raise RuntimeError(
                "firebase-admin no está instalado. Ejecuta: pip install firebase-admin"
            )

        if not firebase_admin._apps:
            
            db_url = "https://polimorfismo-y-herencia-53605-default-rtdb.firebaseio.com/"  # 👈 ¡¡CAMBIA ESTA URL!!
            creds_json_path = "credentials.json"
            
            if not os.path.isfile(creds_json_path):
                raise RuntimeError(f"No se encuentra el archivo '{creds_json_path}'. Descárgalo de Firebase.")

            if "tu-proyecto-default-rtdb" in db_url:
                 raise RuntimeError("¡No olvides cambiar la URL de la base de datos (db_url) en firebase_service.py!")

            cred = credentials.Certificate(creds_json_path)
            firebase_admin.initialize_app(cred, {"databaseURL": db_url})
            print("¡Conexión exitosa a Firebase!")


    def save_animal(self, animal_object):
        """
        Toma un objeto (Leon, Perro, etc.) y lo guarda en Firebase.
        """
        try:

            especie = animal_object.especie

            datos = animal_object.__dict__
            
            ref = db.reference(f"/{self.base_path}/{especie}")
            ref.push(datos)
            
            print(f"-> ¡{animal_object.especie} guardado en Firebase DB!")
            
        except Exception as e:
            print(f"ERROR: No se pudo guardar {animal_object.especie} en Firebase: {e}")