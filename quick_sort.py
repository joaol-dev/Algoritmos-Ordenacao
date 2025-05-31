# quick sort, ordenação por partição

def quick_sort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quick_sort(lista, inicio, p - 1)
        quick_sort(lista, p + 1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

lista = [4, 7, 2, 6, 4, 1, 8, 3]
quick_sort(lista)
print(lista)