# test_motor.py
from percepcion.observador import ObservadorUniversal
import time

def iniciar_aprendizaje():
    mecanico = ObservadorUniversal()
    
    # 1. Lección Biológica: El ciclo de una planta en sequía
    print("Enviando datos biológicos...")
    mecanico.observar_reino("Biologico", {"humedad_suelo": 10, "exposicion_solar": 95, "ritmo_crecimiento": 2})
    
    time.sleep(2) # El tiempo fluye...

    # 2. Lección Financiera: BTC frente a la liquidez
    print("Enviando datos de energía financiera...")
    mecanico.observar_reino("Financiero", {"btc_precio": 65000, "miedo_mercado": 80, "liquidez_fed": 15})

    print("Observación completada. Revisa la bitacora_estelar.json")

if __name__ == "__main__":
    iniciar_aprendizaje()
