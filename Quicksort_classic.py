
def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1

def find_pivot(Alist, min, max):
    i = min - 1
    pivot = Alist[max]

    for j in range(min ,max):
        if Alist[j] <= pivot:
            i += 1
            Alist[j], Alist[i] =  Alist[i], Alist[j]

    poz = Alist.index(pivot)
    Alist[i+1], Alist[poz] = Alist[poz], Alist[i+1]
    return i+1


def quicksort_classic(Alist, min ,max):
    if len(Alist) == 0:
        return Alist
    if min < max:
        pivot = find_pivot(Alist, min, max)

        quicksort_classic(Alist, min, pivot-1)
        quicksort_classic(Alist, pivot+1, max)
        rez = Alist.copy()
        return rez


arr = [10, 7, 8, 9, 1, 5]
arr1 = arr.copy()
rez = [0]*len(arr)
n = len(arr)



print(quicksort_classic(arr1, 0, n-1))
print(verif_sort(quicksort_classic(arr1, 0, n-1)))