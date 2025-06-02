"""
Quick sort, ordenação rápida

Vantagens:
- Um dos algoritmos mais rápidos na prática para ordenação interna
- Ordenação in-place, não requer espaço extra significativo
- Adaptável a Dados Parcialmente Ordenados

Desvantagens:
- Vulnerável a ataques de entrada maliciosa, se um adversário conhece a estratégia de pivô, pode forçar o pior caso
- Pior caso O(n²) se o pivô é mal escolhido
- overhead de Recursão chamadas recursivas podem levar a stack overflow em listas muito grandes

Uso recomendado:
- Grandes conjuntos de dados em memória (onde velocidade média é crítica)
- Ambientes com restrição de memória (in-place)

"""

def quick_sort(lista, inicio = 0, fim = None):
    if fim is None:             # Define o valor inicial de 'fim' na primeira chamada
        fim = len(lista) - 1
    if inicio < fim:            # Executa a ordenação apenas se ainda houver mais de um elemento
        p = partition(lista, inicio, fim)       # Particiona a lista e obtém o índice do pivô já na posição correta
        quick_sort(lista, inicio, p - 1)        # Aplica recursivamente o quick sort à sublista da esquerda
        quick_sort(lista, p + 1, fim)           # Aplica recursivamente o quick sort à sublista da direita

def partition(lista, inicio, fim):
    pivot = lista[fim]      # Define o pivô como o último elemento da sublista
    i = inicio              # Índice do menor elemento
    for j in range(inicio, fim):        # Percorre a sublista da posição 'inicio' até 'fim - 1'
        if lista[j] <= pivot:           # Se o elemento atual for menor ou igual ao pivô
            lista[j], lista[i] = lista[i], lista[j]          # Troca o elemento atual com o elemento da posição i
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]         # Coloca o pivô na posição correta (entre menores e maiores)
    return i            # Retorna a posição do pivô
