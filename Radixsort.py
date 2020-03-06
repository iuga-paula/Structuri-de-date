

def countsort1(list, exp):
    rez = [0]*len(list)
    freq = [0]*10

    for i in range(len(list)):
        nr = list[i] // exp
        freq[nr % 10] += 1

    for i in range(1, 10):
        freq[i] += freq[i - 1]

    i = len(list) - 1

    while i >= 0:
        nr = list[i]//exp
        rez[freq[nr % 10]-1] = list[i]
        freq[nr % 10] -= 1
        i -= 1

    #print(rez)

    for i in range(len(list)):
        list[i] = rez[i]


def radixsort(list):
    if len(list) == 0:
        return list
    ma = max(list)
    #nr = number_of_digits(max)
    exp = 1
    while ma/exp > 0:
        countsort1(list, exp)
        exp *= 10

    return list

def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1



arr = [112,80,23,13,603,60,12]
arr1 = arr.copy()


print(radixsort(arr1))
print(verif_sort(radixsort(arr1)))
