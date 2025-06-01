# bubble sort, ordenação por flutuação

def bubble_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i] 

lista = [5, 8, 2, 9, 3, 10]
bubble_sort(lista)
print(lista)

lista_invertida = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
bubble_sort(lista_invertida)
print(lista_invertida)