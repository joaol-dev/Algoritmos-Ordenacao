"""
Merge sort, ordenação por intercalação

Vantagens:
- Muito eficiente para listas grandes e para dados armazenados em dispositivos externos (como discos)
- Muito mais rápido que algoritmos O(n²) (Bubble, Insertion, Selection Sort) para grandes conjuntos
- Pode ser implementado de forma dividir-e-conquistar em múltiplos núcleos/threads, ideal para processadores que usam multi-threading

Desvantagens:
- Não aproveita listas parcialmente ordenadas (sempre executa O(n log n))
- Não é in-place → Requer O(n) de espaço auxiliar para mesclagem
- Pode ser menos eficiente em termos de uso de memória comparado a algoritmos in-place como Quick Sort e Heap Sort

Uso recomendado:
- Ordenação externa (arquivos grandes em disco)
- Ambientes onde previsibilidade é crítica (evitando piores casos do Quick Sort)

"""

def merge_sort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)

    if (fim - inicio > 1):      # Só divide a lista se o tamanho for maior que 1 (caso base da recursão)
        meio = (fim + inicio) // 2      # Calcula o meio para dividir a lista em duas partes

        merge_sort(lista, inicio, meio)     # Chamada recursiva para ordenar a primeira metade
        merge_sort(lista, meio, fim)        # Chamada recursiva para ordenar a segunda metade
        merge(lista, inicio, meio, fim)     # Une (merge) as duas metades ordenadas

def merge(lista, inicio, meio, fim):
    left = lista[inicio : meio]         # Sublista esquerda
    right = lista[meio : fim]           # Sublista direita
    top_left, top_right = 0, 0          # Índices para percorrer as sublistas esquerda e direita

    for k in range(inicio, fim):        # Percorre a faixa da lista original para reconstruir ordenadamente
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):       # Se todos os elementos da direita já foram usados, pega da esquerda
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:      # Se o elemento da esquerda é menor, insere ele primeiro
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]              # Caso contrário, insere o elemento da direita
            top_right = top_right + 1
