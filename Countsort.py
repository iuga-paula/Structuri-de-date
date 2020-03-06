def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1


def countsort(list):
    if len(list) == 0:
        return  list
    ma = max(list)+1
    freq = [0]*ma
    rez = []

    for elem in list:
        freq[elem] += 1

    for i in range(ma):
        for j in range(freq[i]):
            rez.append(i)

    return rez



arr = [10,7,9,10,7,5,5,8, 9, 1,1,1, 5]
arr1 = arr.copy()
rez = [0]*len(arr)
n = len(arr)
print(countsort(arr1))
print(verif_sort(countsort(arr1)))