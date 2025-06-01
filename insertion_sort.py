# insertion sort, ordenação por inserção

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave

lista = [5, 8, 2, 9, 3, 10]
insertion_sort(lista)
print(lista)

lista_invertida = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
insertion_sort(lista_invertida)
print(lista_invertida)