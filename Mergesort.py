

def merge(list1, list2):
    i = j = 0
    rez = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            rez.append(list1[i])
            i += 1
        else:
            rez.append(list2[j])
            j += 1

    rez.extend(list1[i:])
    rez.extend(list2[j:])
    return rez

def mergesort(list):
    if len(list) <= 1:
        return list
    else:
        mid = len(list) // 2
        left_list = mergesort(list[:mid])
        right_list = mergesort(list[mid:])

        return merge(left_list, right_list)

def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1

arr = [1,3,45,340,30,12]
arr1 = arr.copy()
rez = [0]*len(arr)
n = len(arr)
print(mergesort(arr1))
print(verif_sort(mergesort(arr1)))