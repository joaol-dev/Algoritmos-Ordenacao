"""
Radix sort,

Vantagens: 
- Muito consistente, sem casos degenerados (performance não varia como no QuickSort)
- Bom para dados inteiros ou strings curtas, como CPFs, números de telefone, datas, etc
- Mais rápido que algoritmos de comparação (como quick sort ou merge sort) em listas com muitos números inteiros pequenos ou com número fixo de dígitos

Desvantagens:
- Restrito a dados com estrutura de chave bem definida, como inteiros, strings ou floats de tamanho fixo
- Pode ser ineficiente em listas pequenas algoritmos simples como Insertion Sort podem ser melhores nesses casos
- Tempo de execução fixo baseado no número de dígitos, independente da ordenação inicial

Uso recomendado:
- Quando se deseja ordenar muitos números inteiros de tamanho fixo ou similar, especialmente não negativos
- Quando a estabilidade na ordenação é importante, por exemplo, ordenações múltiplas (como por data, depois por nome).

"""

# Função auxiliar que faz o Counting Sort baseado no dígito atual (exp)
def countingSortPorDigito(lista, exp):
    n = len(lista)  # Tamanho do array
    output = [0] * n  # Lista temporária para armazenar a ordenação parcial
    count = [0] * 10  # Lista de contagem para os dígitos de 0 a 9

    for i in range(n):      # Conta a ocorrência de cada dígito na posição atual (exp)
        indice = (lista[i] // exp) % 10  # Extrai o dígito atual
        count[indice] += 1  

    for i in range(1, 10):   # Atualiza a contagem acumulada para saber as posições corretas
        count[i] += count[i - 1]

    # Constrói a saída ordenada com base no dígito atual (do fim para o início, para estabilidade)
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        output[count[indice] - 1] = lista[i] 
        count[indice] -= 1 
        i -= 1  

    for i in range(n):          # Copia a ordenação parcial de volta para a lista original
        lista[i] = output[i]

# Função principal do Radix Sort
def radixSort(lista):
    max_val = max(lista)     # Encontra o maior número na lista (para saber o número de dígitos)

    exp = 1         # Representa a posição do dígito (1 = unidade, 10 = dezena, 100 = centena, etc.)
    while max_val // exp > 0:
        countingSortPorDigito(lista, exp)       # Ordena os elementos com base no dígito atual
        exp *= 10                               # Move para o próximo dígito (da direita para a esquerda)