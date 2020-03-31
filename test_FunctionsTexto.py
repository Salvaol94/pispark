from unittest import TestCase
import FunctionsTexto

class Test(TestCase):
    def test_contarpalabras(self):
        texto=FunctionsTexto.leerfichero("Pruebatexto.txt")
        palabras= FunctionsTexto.contarpalabras(texto)
        self.assertEqual(len(palabras),6)

    def test_quitar_acentos(self):
        texto="Hóla añigo"
        self.assertEqual(FunctionsTexto.limpiar_acentos(texto),'Hola anigo')

    def test_quitar_acentos(self):
        texto="Hola Hola Hola amigo conocido amigo"
        self.assertEqual(FunctionsTexto.agrupar_palabtas(texto),'Hola anigo')