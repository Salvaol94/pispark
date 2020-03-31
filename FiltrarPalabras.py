import FunctionsTexto

texto = FunctionsTexto.leerfichero("Cuento.txt")
texto=FunctionsTexto.limpiar_acentos(texto)
texto=texto.upper()
palabras = FunctionsTexto.contarpalabras(texto)
palabras_agrupadas= FunctionsTexto.agrupar_palabras(palabras)
print (palabras)
print(len(palabras))
print(palabras_agrupadas)