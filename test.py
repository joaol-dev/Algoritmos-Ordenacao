import random
from selection_sort import selection_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from counting_sort import counting_sort
from radix_sort import radix_sort
from bucket_sort import bucket_sort

any_numbers = random.sample(range(1, 1000), 42)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 
                    32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]

if __name__ == "__main__":
    test_cases = {'Números aleatórios': any_numbers, 
                    'Já ordenados': already_sorted, 
                    'Ordem inversa': inversed, 
                    'Elementos repetidos': repeated
                }
    print("*******************************")
    for name, lista in test_cases.items():
        print("\nCaso de teste: {}".format(name))
        print(lista)
        selection_sort(lista)
        print("\n Ordenado:")
        print(lista)
    print("*******************************")

#  teste apenas do bucket sort

print("\nTeste exclusivo bucket sort")
bucketlista = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print("\nLista original:", bucketlista)
bucket_sort(bucketlista)
print("\nLista ordenada:", bucketlista)
