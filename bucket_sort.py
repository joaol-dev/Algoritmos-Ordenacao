"""
Bucket sort, ordenação por "baldes"

Vantagens:
- Muito eficiente para entradas uniformemente distribuídas (especialmente entre 0 e 1)
- Simples de implementar quando os dados seguem uma distribuição conhecida
- Estável se implementado corretamente

Desvantagens:
- Depende da distribuição dos dados, a performance degrada rapidamente se a distribuição for muito desigual ou desconhecida
- Requer memória extra, não é in-place
- Requer conhecimento prévio sobre a faixa dos dados (geralmente entre 0 e 1)

Uso recomendado:
- Dados com distribuição uniforme (ex.: números reais em um intervalo conhecido)
- Ordenação de floats/doubles (comum em aplicações gráficas e científicas)

"""

def bucket_sort(lista):
    n = len(lista)      # Tamanho da lista

    if n == 0:          # Se a lista estiver vazia, não há o que ordenar
        return  

    buckets = [[] for _ in range(n)]        # Cria 'n' baldes vazios (listas internas)

    for num in lista:               # Distribui os elementos nos baldes com base no valor
        index = int(num * n)        # Define o índice do balde (assume que os valores estão entre 0 e 1)
        buckets[index].append(num)
    for bucket in buckets:          # Ordena individualmente cada balde (usa o sort interno do Python)
        bucket.sort()

    index = 0                       # Junta os baldes de volta na lista original
    for bucket in buckets:
        for num in bucket:
            lista[index] = num
            index += 1
