# selection sort, ordenação por seleção 

def selection_sort(lista):
    n = len(lista)
    for p in range(n - 1):
        min_indice = p
        for i in range(p, n):
            if lista[i] < lista[min_indice]:
                min_indice = i
        if lista[p] > lista[min_indice]:
            aux = lista[p]
            lista[p] = lista[min_indice]
            lista[min_indice] = aux

lista = [5, 8, 2, 9, 3, 10]
selection_sort(lista)
print(lista)
