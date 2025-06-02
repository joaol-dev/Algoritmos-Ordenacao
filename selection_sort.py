"""
Selection sort, ordenação por seleção 

Vantagens
- Número de trocas é mínimo, no máximo (n - 1), o que pode ser útil quando trocas são custosas
- In-place: não requer memória extra significativa
- Funciona bem para listas pequenas

Desvantagens:
- Complexidade de tempo O(n²) em todos os casos, mesmo que a lista esteja ordenada
- Ineficiente para listas grandes comparado a algoritmos mais avançados
- Realiza muitas comparações, mesmo se a lista já estiver quase ordenada

Uso recomendado:
- Bom para sistemas com memória muito limitada, pois é um algoritmo in-place
- Usado principalmente para fins educacionais e didáticos, para ensinar conceitos básicos de ordenação, assim como o bubble sort

"""

def selection_sort(lista):
    n = len(lista)          # Obtém o tamanho da lista

    for p in range(n - 1):  # Percorre cada posição da lista, exceto a última
        min_indice = p      # Assume que o menor elemento está na posição atual

        for i in range(p, n):       # Busca o menor elemento no restante da lista (do índice p até o fim)
            if lista[i] < lista[min_indice]:
                min_indice = i      # Atualiza o índice do menor elemento encontrado
                
        if lista[p] > lista[min_indice]:    # Se o menor elemento encontrado for menor que o elemento na posição p, troca-os
            aux = lista[p]
            lista[p] = lista[min_indice]
            lista[min_indice] = aux
