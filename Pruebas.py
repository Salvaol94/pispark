def function(item):
    return item*2



lista=(1,2,3,4,5,6,7,8,9)

nueva_lista = list(map(function,lista))

print(nueva_lista)


def impar(numero):
    return numero%2==1

impares =list(filter(impar, lista))
print(impares)


