

def bubblesort(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(list) - 1):
            if list[i] >= list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted =  False

    return list

def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1






arr = []
arr1 = arr.copy()
rez = [0]*len(arr)
n = len(arr)
print(bubblesort(arr1))
print(verif_sort(bubblesort(arr1)))