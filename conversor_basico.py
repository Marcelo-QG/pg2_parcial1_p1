class ConversorBasico:
    def __init__(self):
        self._unidad_origen = ""
        self._unidad_destino = ""
        self._resultado = 0

    def _conversion_generica(self, cantidad, origen, destino):
        self._unidad_origen = origen
        self._unidad_destino = destino
        self._resultado = cantidad * (destino / origen)

    def _mostrar_resultados(self, cantidad):
        print(f"{cantidad} {self._unidad_origen} son {self._resultado} {self._unidad_destino}")
