from random import random as rnd
from operator import add
from pyspark.sql import SparkSession


def estimar_pi(calculos):
    dentro_del_circulo = 0
    for I in range(calculos):
        x = rnd()
        y = rnd()
        distancia_al_centro = x * x + y * y
        if distancia_al_centro <= 1:
            dentro_del_circulo += 1;
    return (dentro_del_circulo / calculos) * 4

def estimar_pi_bloques(calculos, bloques):
    lista=[int((calculos/bloques))for i in range(bloques)]
    return sum(list(map(estimar_pi, lista)))/bloques


def estimar_pi_spark(calculos, bloques):
    #Crear Sesion con un Spark
    MI_MAESTRO="local[2]"
    sesion=SparkSession.builder.master(MI_MAESTRO).appName("Mi Estimador de PI").getOrCreate()
    #Crear RDD (lo hace la sesión): Paralelizamos la lista
    lista=[int((calculos/bloques))for i in range(bloques)]
    return sesion.sparkContext.parallelize(lista).map(estimar_pi).reduce(add)/bloques

print(estimar_pi_spark(100*1000*1000,2))