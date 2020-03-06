def pivot_median(Alist): #alg BFPRT pt media medianelor returneaza un element
    if len(Alist) <= 5:
        return sorted(Alist)[len(Alist)//2]
    sublists = [sorted(Alist[i:i+5]) for i in range(0, len(Alist),5)]
    medians = [sl[len(sl)//2] for sl in sublists]

    return pivot_median(medians)


def quickselect(Alist, k, pivot_median):
    pivot = pivot_median(Alist)
    L = []
    E = []
    G = []

    for x in Alist:
        if x < pivot:
            L.append(x)
        elif x == pivot:
            E.append(x)
        else:
            G.append(x)

    if k < len(L):
        return quickselect(L, k, pivot_median)
    elif k < len(L) + len(E):
        return E[0]
    else:
        return quickselect(G, k - len(L) - len(E), pivot_median)

def quicksort(Alist, pivot_median):
    if len(Alist) == 0:
        return  Alist
    rez  = []
    for k in range(len(Alist)):
        rez.append(quickselect(Alist, k, pivot_median))
    return rez

def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1

arr = [10, 7, 8, 9, 1, 5]
arr1 = arr.copy()
rez = [0]*len(arr)
n = len(arr)
#print(quickselect(arr, 0, pivot_median))
print(quicksort(arr, pivot_median))
print(verif_sort(quicksort(arr, pivot_median)))
