"""
Insertion sort, ordenação por inserção

Vantagens:
- Simples de entender e fácil de implementar
- Eficiente para listas pequenas ou quase ordenadas
- Adaptativo: se os dados já estiverem parcialmente ordenados, é muito rápido (quase O(n))

Desvantagens:
- Desempenho ruim em listas grandes e desordenadas (complexidade O(n²) no pior caso)
- Não é adequado para grandes volumes de dados
- Ineficiente comparado a algoritmos como Merge Sort, Quick Sort e Heap Sort em listas grandes.

Uso recomendado:
- Muito eficiente quando os dados estão quase ordenados, pois se adapta bem e pode rodar em tempo quase linear
- Bom para inserção dinâmica de dados ordenados, como ao inserir um novo elemento em uma lista já ordenada.

"""

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):       # Começa do segundo elemento (índice 1), pois o primeiro já é considerado ordenado
        chave = lista[i]        # Armazena o valor atual a ser inserido na parte ordenada
        j = i - 1               # Índice do último elemento da parte ordenada

        # Move os elementos maiores que a chave uma posição à frente
        # Isso cria espaço para inserir a chave na posição correta
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave            # Insere a chave na posição correta dentro da parte ordenada
