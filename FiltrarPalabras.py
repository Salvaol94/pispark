import FunctionsTexto

texto = FunctionsTexto.leerfichero("Cuento.txt")
texto=FunctionsTexto.limpiar_acentos(texto)
texto=texto.upper()
palabras = FunctionsTexto.contarpalabras(texto)
palabras_nonstop=FunctionsTexto.stop_words(palabras)
palabras_agrupadas= FunctionsTexto.agrupar_palabras(palabras_nonstop)

print (palabras)
print(len(palabras))
print(palabras_agrupadas)
