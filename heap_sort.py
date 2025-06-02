"""
Heap sort, ordenação baseado em estrutura de heap (árvore binária)

Vantagens:
- Complexidade de tempo consistente: O(n log n) em todos os casos (melhor, médio e pior)
- Não depende da ordem inicial dos dados
- in-place: utiliza memória constante, não requer estrutura auxiliar como o merge sort

Desvangens:
- Ele não se beneficia se a lista já estiver parcialmente ordenada
- Mais complexo, implementação mais difícil que algoritmos simples (Bubble, Insertion).

Uso recomendado:
- Construção de estruturas de dados como filas de prioridade (priority queues), onde a lógica de heap já é necessária
-  Útil em sistemas com **restrição de memória**, já que é um algoritmo in-place (diferente do Merge Sort que usa memória extra).

"""

def heapify(lista, n, i):       # Função para transformar uma subárvore em um heap máximo (max-heap)
    maior = i
    esquerda = 2 * i + 1        # Índice do filho à esquerda
    direita = 2 * i + 2         # Índice do filho à direita

    if esquerda < n and lista[esquerda] > lista[maior]:     # Verifica se o filho à esquerda existe e é maior que a raiz
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:       # Verifica se o filho à direita existe e é maior que o maior atual
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]     # Se o maior valor não está na raiz, faz a troca
        heapify(lista, n, maior)

# Constrói um heap máximo a partir da lista


def heap_sort(lista):       # Começa do último nó pai (n//2 - 1) até a raiz (índice 0)
    n = len(lista)

    for i in range (n // 2 - 1, - 1, - 1):      
        heapify(lista, n, i)
    for i in range (n - 1, 0, -1):      # Um a um, extrai os elementos do heap e coloca no final da lista
        lista[i], lista[0] = lista[0], lista[i]         # Troca a raiz (maior elemento) com o último elemento não ordenado
        heapify(lista, i, 0)                   # Reconstroi o heap na parte não ordenada da lista
