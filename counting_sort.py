# counting sort, ordenação por contagem

def counting_sort(lista):
    if not lista:
        return lista

    maior = max(lista)
    contagem = [0] * (maior + 1)

    for num in lista:
        contagem[num] += 1
    i = 0
    for numero in range(len(contagem)):
        for _ in range(contagem[numero]):
            lista[i] = numero
            i += 1

lista = [4, 7, 2, 6, 4, 1, 8, 8, 3, 3]
counting_sort(lista)
print(lista)
