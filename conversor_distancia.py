from conversor_basico import ConversorBasico

class ConversorDistancia(ConversorBasico):
    def metros_a_centimetros(self, metros):
        self._conversion_generica(metros, 1, 100)
        self._mostrar_resultados(metros)

    def centimetros_a_kilometros(self, centimetros):
        self._conversion_generica(centimetros, 100000, 1)
        self._mostrar_resultados(centimetros)
