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

lista_invertida = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
selection_sort(lista_invertida)
print(lista_invertida)