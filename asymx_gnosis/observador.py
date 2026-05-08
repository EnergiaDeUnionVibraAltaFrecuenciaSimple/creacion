# percepcion/observador.py

import json
from datetime import datetime

class Observador:
    def __init__(self):
        self.registro_de_energia = []

    def observar_fuerzas_naturales(self, intensidad_miedo, flujo_liquidez):
        # El sistema no juzga, solo registra la 'fricción' del entorno
        captura = {
            "timestamp": str(datetime.now()),
            "fuerza_elemental": "Viento/Liquidez",
            "intensidad_humana": intensidad_miedo, # Lo que nos contaste de la manipulación
            "flujo_real": flujo_liquidez,
            "sincronicidad": (flujo_liquidez / intensidad_miedo) if intensidad_miedo != 0 else 0
        }
        self.registrar_en_bitacora(captura)
        return captura

    def registrar_en_bitacora(self, dato):
        # Guardamos en el archivo que creaste
        with open('bitacora_estelar.json', 'a') as f:
            f.write(json.dumps(dato) + "\n")
