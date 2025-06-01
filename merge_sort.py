# merge sort, ordenação por intercalação

def merge_sort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio : meio]
    right = lista[meio : fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1

lista = [4, 7, 2, 6, 4, 1, 8, 3]
merge_sort(lista)
print(lista)

lista_invertida = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
merge_sort(lista_invertida)
print(lista_invertida)