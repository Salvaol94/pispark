import re
import unidecode
import pandas as pd

def leerfichero(string):
    with open(string,"r") as fichero:
        texto = fichero.read()
    return texto

def contarpalabras(texto):
    palabras = re.split(
        "[.]|" +
        "[,]|" +
        "[;]|" +
        "[:]|" +
        "[-]|" +
        "[_]|" +
        "[=]|" +
        "[ç]|" +
        "[]]|" +
        "[#]|" +
        "[+]|" +
        "[*]|" +
        "[!]|" +
        "[>]|" +
        "[<]|" +
        "[$]|" +
        "[~]|" +
        "[%]|" +
        "[&]|"+
        "[(]|" +
        "[)]|" +
        "[/]|" +
        "[?]|" +
        "[¿]|" +
        "[0-9]|" +
        "[\]]|" +
        "[\[]|" +
        "[”]|"+
        "[“]|" +
        "\s",texto)
    filtrado= [palabra for palabra in palabras if len(palabra)>0]
    return filtrado

def limpiar_acentos(texto):
    return unidecode.unidecode(texto)

def agrupar_palabras(lista):
    cuenta_de_palabras=[(palabra,1) for palabra in lista]
    df =pd.DataFrame(cuenta_de_palabras)
    df.columns= ["Palabras", "Repeticiones"]
    df=df.groupby("Palabras").sum()
    df=df.sort_values("Repeticiones",ascending=False)

    return df