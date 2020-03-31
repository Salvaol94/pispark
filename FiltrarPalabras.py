from operator import add

import FunctionsTexto
from pyspark.sql import SparkSession

texto = FunctionsTexto.leerfichero("Cuento.txt")
texto=FunctionsTexto.limpiar_acentos(texto)
texto=texto.upper()
palabras = FunctionsTexto.contarpalabras(texto)
palabras_nonstop=FunctionsTexto.stop_words(palabras)
palabras_agrupadas= FunctionsTexto.agrupar_palabras(palabras_nonstop)

print (palabras)
print(len(palabras))
print(palabras_agrupadas)


####lo mismo con spark

# Crear Sesion con un Spark
MI_MAESTRO = "local[2]"
sesion = SparkSession.builder.master(MI_MAESTRO).appName("Contar Palabras").getOrCreate()
# Crear RDD (lo hace la sesión): Paralelizamos la lista
texto = [FunctionsTexto.leerfichero("Cuento.txt")]
rdd= sesion.sparkContext.parallelize(texto)
rdd1=rdd.flatMap(FunctionsTexto.contarpalabras)
rdd2=rdd1.map(FunctionsTexto.limpiar_acentos)
rdd3= rdd2.map(lambda palabra:palabra.upper())
rdd4= rdd3.filter(FunctionsTexto.stop_words)
rdd5=rdd4.map(lambda palabra: (palabra,1))
rdd6=rdd5.reduceByKey(add)
rdd7=rdd6.map(lambda dupla: (dupla[1],dupla[0]))
rdd8=rdd7.sortByKey(False)
rdd9=rdd8.map(lambda dupla: (dupla[1],dupla[0]))
lista_puntuada=rdd9.collect()

for(palabra,ocurrencias) in lista_puntuada:
    print(str(palabra)+"   "+str(ocurrencias))
sesion.stop()