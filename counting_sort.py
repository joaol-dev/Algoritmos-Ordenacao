"""
Counting sort, ordenação por contagem

Vantagens:
- Complexidade O(n + k), onde n = número de elementos e k = valor máximo
- Estável (mantém a ordem relativa de elementos iguais)
- Eficiente para dados inteiros com alcance limitado

Desvantagens:
- Só funciona para inteiros não negativos
- Ineficiente quando k é muito maior que n
- Requer memória adicional O(n + k)

Uso recomendado:
- Dados inteiros, não negativos
- O valor máximo de k é da mesma ordem de grandeza que n
- Excelente com elementos repetidos
"""

def counting_sort(lista):
    if not lista:
        return lista
    
    maior = max(lista)          # Encontra o maior valor na lista para saber o tamanho do array de contagem

    contagem = [0] * (maior + 1)    # Cria uma lista de contagem com zeros, com índice até o maior número da lista
                                    # Cada posição representará quantas vezes aquele número aparece

    for num in lista:               # Conta quantas vezes cada número aparece na lista original
        contagem[num] += 1

    i = 0
    for numero in range(len(contagem)):        # Percorre todos os números possíveis (de 0 até o maior número da lista)
        for _ in range(contagem[numero]):      # Para cada ocorrência do número atual (isto é, quantas vezes ele apareceu)
            lista[i] = numero                  # Insere esse número na posição atual da lista original

            i += 1             # Avança para próxima posição da lista original