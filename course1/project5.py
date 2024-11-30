def reducir_lista(lista):
    lista_duplicate = []
    for index, n in enumerate(lista):
        if n not in lista_duplicate:
            lista_duplicate.append(n)
        else:
            pass
    lista = sorted(lista_duplicate)
    lista.pop()
    return lista

def promedio(lista):
    length = len(lista)
    suma = 0
    for n in lista:
        suma += n
    return suma/length

lista_numeros = [1, 2, 15, 7, 2]
lista_numeros = reducir_lista(lista_numeros)
promedio = promedio(lista_numeros)
print(lista_numeros)
print(promedio)
