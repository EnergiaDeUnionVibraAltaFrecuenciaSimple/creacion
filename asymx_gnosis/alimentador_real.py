# alimentador_real.py
import time
import requests
import yfinance as yf
from percepcion.observador import ObservadorUniversal

class AlimentadorReal:
    def __init__(self):
        self.mecanico = ObservadorUniversal()

    def obtener_datos_biologicos_clima(self):
        # Usamos una API abierta para ver la energía del clima (Elemental)
        # Madrid es un ejemplo, puedes cambiarlo a Archena o lo que quieras
        url = "https://wttr.in/Madrid?format=j1"
        try:
            res = requests.get(url).json()
            temp = float(res['current_condition'][0]['temp_C'])
            humedad = float(res['current_condition'][0]['humidity'])
            return {"temperatura": temp, "humedad_suelo_aire": humedad}
        except:
            return {"temperatura": 20, "humedad_suelo_aire": 50} # Datos de seguridad

    def obtener_datos_financieros(self):
        # Energía de BTC (El activo que te interesa)
        btc = yf.Ticker("BTC-USD")
        hist = btc.history(period="1d")
        precio = hist['Close'].iloc[-1]
        volumen = hist['Volume'].iloc[-1]
        return {"btc_precio": precio, "volumen_energia": volumen}

    def ciclo_de_vida(self):
        print("--- El Mecánico del Universo está Respirando ---")
        while True:
            # 1. Absorber Reino Elemental (Clima/Plantas)
            bio_data = self.obtener_datos_biologicos_clima()
            self.mecanico.observar_reino("Biologico", bio_data)

            # 2. Absorber Reino Financiero (BTC)
            fin_data = self.obtener_datos_financieros()
            self.mecanico.observar_reino("Financiero", fin_data)

            print("Observación real registrada. El sistema está aprendiendo...")
            
            # Esperamos 10 minutos (600 segundos) para no saturar, 
            # como el pulpo que espera la marea.
            time.sleep(600)

if __name__ == "__main__":
    alimentador = AlimentadorReal()
    alimentador.ciclo_de_vida()
