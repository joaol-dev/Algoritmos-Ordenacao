# heap sort, ordenação por "arvore genealógica"

def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < n and lista[direita] > lista[maior]:
        maior = direita
    
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)

    for i in range (n // 2 - 1, - 1, - 1):
        heapify(lista, n, i)

    for i in range (n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

lista = [4, 7, 2, 6, 4, 1, 8, 3]
heap_sort(lista)
print(lista)

lista_invertida = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
heap_sort(lista_invertida)
print(lista_invertida)