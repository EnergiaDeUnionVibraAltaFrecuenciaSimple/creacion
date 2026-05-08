# percepcion/observador.py

import json
from datetime import datetime

class ObservadorUniversal:
    def __init__(self):
        self.ruta_bitacora = 'bitacora_estelar.json'

    def observar_reino(self, reino, datos):
        """
        reino: 'Biologico', 'Financiero', 'Social' o 'Elemental'
        datos: Un diccionario con las variables observadas
        """
        print(f"Observando el reino {reino}...")
        
        captura = {
            "timestamp": str(datetime.now()),
            "reino": reino,
            "datos_crudos": datos,
            "mecanica_detectada": self.extraer_mecanica(reino, datos),
            "vibracion_neta": self.calcular_intensidad(datos)
        }
        
        self.registrar_en_bitacora(captura)
        return captura

    def extraer_mecanica(self, reino, datos):
        # El corazón del aprendizaje: busca el engranaje oculto
        if reino == "Biologico":
            # Ejemplo: datos={'agua': 0.2, 'sol': 0.8}
            return "Crecimiento bajo tensión: la luz guía la expansión a pesar de la sed."
        elif reino == "Financiero":
            return "Flujo de valor: la liquidez busca el vacío donde el miedo es alto."
        elif reino == "Social":
            return "Inercia de masas: la manipulación crea una realidad temporal."
        return "Sincronicidad elemental detectada."

    def calcular_intensidad(self, datos):
        # Una lógica simple para medir la 'energía' del evento
        valores = [v for v in datos.values() if isinstance(v, (int, float))]
        return sum(valores) / len(valores) if valores else 0

    def registrar_en_bitacora(self, dato):
        with open(self.ruta_bitacora, 'a', encoding='utf-8') as f:
            f.write(json.dumps(dato, ensure_ascii=False) + "\n")
