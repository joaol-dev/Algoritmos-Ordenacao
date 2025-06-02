"""
Bubble sort, ordenação por flutuação

Vantagens:
- Fácil de entender e implementar, ideal para aprendizado
- Não usa memória extra (in-place)
- Útil para pequenos conjuntos de dados

Desvantagens:
- Ineficiente para listas grandes (complexidade O(n²))
- Realiza muitas comparações e trocas
- Pouco prático - Não é usado em aplicações reais com muitos dados

Uso recomendado:
- Geralmente é usado para fins educacionais, pois é fácil de entender e de implementar

"""

def bubble_sort(lista):
    n = len(lista)
    for j in range(n - 1):          # Loop externo percorre a lista (n - 1) vezes no pior caso
        trocou = False              # Flag para verificar se houve troca nesta iteração

        for i in range(n - 1 - j):      # Loop interno evita comparar os últimos elementos já ordenados
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]     # Troca os elementos se estiverem fora de ordem
                trocou = True
        if not trocou:          # Se não houve trocas, a lista já está ordenada
            break
