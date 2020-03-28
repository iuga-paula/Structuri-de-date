import random
import time


#functie verificare
def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1


#bubble sort
def bubblesort(list):
    last = len(list)
    swapped = True
    while swapped:
        swapped = False
        for j in range(1, last):
            if list[j - 1] > list[j]:
                list[j], list[j - 1] = list[j - 1], list[j]
                swapped = True
                last = j
    return list


#count sort
def countsort(list):
    if len(list) == 0:
        return list
    ma = max(list)+1
    freq = [0]*ma
    rez = []

    for elem in list:
        freq[elem] += 1

    for i in range(ma):
        for j in range(freq[i]):
            rez.append(i)
    return rez


#merge sort
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


#radix sort
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


#quick sort1
def concat(before, equal, after):
    newlist = []
    for items in before:
        newlist.append(items)
    for items in equal:
        newlist.append(items)
    for items in after:
        newlist.append(items)
    return newlist


def quicksort(list):
    smaller = []
    greater = []
    equal = []
    if len(list) <= 1:
        return list
    pivotVal = list[random.randint(0, len(list)-1)]
    list.remove(pivotVal)
    equal.append(pivotVal)
    for items in list:
        if items < pivotVal:
            smaller.append(items)
        elif items == pivotVal:
            equal.append(items)
        else:
            greater.append(items)
    return concat(quicksort(smaller), equal, quicksort(greater))


#quick sort2 cu media medianelor
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

def quicksort2(Alist, pivot_median):
    if len(Alist) == 0:
        return Alist
    rez = []
    for k in range(len(Alist)):
        rez.append(quickselect(Alist, k, pivot_median))
    return rez




#main

g1 = open("test1.txt", "w")
g2 = open("test2.txt", "w")
g3 = open("test3.txt", "w")
g4 = open("test4.txt", "w")
g5 = open("test5.txt", "w")

s = ""
while len(s.split()) < 10000: #creare fisier text cu numere mari
    x = random.randrange(100000, 10000000)
    s += str(x) + " "

g1.write(s)
g1.close()

s = ""
cifre = "123412341234577757"
while len(s.split()) < 100: #creare fisier text cu numere mici cifre repetitive
    x = "".join([random.choice((cifre)) for _ in range(3)])
    s += x + " "

g2.write(s)
g2.close()

s = ""
cifre = "0123456789"
while len(s.split()) < 5: #creare fisier text cu numere mici cifre repetitive
    x = "".join([random.choice((cifre)) for _ in range(2)])
    s += x + " "

while len(s.split()) < 20:
    s += s

g3.write(s)
g3.close()

s = "" #fiser cu sirul vid
g4.write(s)
g4.close()

s = ""
while len(s.split()) < 10000: #creare fisier text cu numere mici
    x = random.randrange(10, 1000)
    s += str(x) + " "

g5.write(s)
g5.close()

fisiere = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt"]

for x in fisiere:
    f = open(x)
    s = f.readline()
    lista = [int(x) for x in s.split()]

    start_time = time.time()
    sorted(lista)
    print("sortarea by default din python a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))

    bs = lista.copy()
    start_time = time.time()
    bubblesort(bs)
    print("Bubble sort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Bubble sort status:", end='')
    if verif_sort(bs) == 1:
        print("OK")
    else:
        print("Gresit")
    print("--------------------------------")

    cs = lista.copy()
    start_time = time.time()
    cs = countsort(cs)
    print("Count sort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Count sort status:", end='')
    if verif_sort(cs) == 1:
        print("OK")
    else:
        print("Gresit")
    print("--------------------------------")

    ms = lista.copy()
    start_time = time.time()
    ms = mergesort(ms)
    print("Merge sort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Merge sort status:", end='')
    if verif_sort(ms) == 1:
        print("OK")
    else:
        print("Gresit")
    print("--------------------------------")

    rs = lista.copy()
    start_time = time.time()
    rs = radixsort(rs)
    print("Radix sort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Radix sort status:", end='')
    if verif_sort(rs) == 1:
        print("OK")
    else:
        print("Gresit")
    print("--------------------------------")

    qs = lista.copy()
    start_time = time.time()
    qs = quicksort(qs)
    print("Quick sort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Quick sort  status:", end='')
    if verif_sort(qs) == 1:
        print("OK")
    else:
        print("Gresit")
    print("--------------------------------")

    qsm = lista.copy()
    start_time = time.time()
    qsm = quicksort2(qsm, pivot_median)
    print("Quick sort cu media medianelor a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Quick sort cu media medianelor status:", end='')
    if verif_sort(qsm) == 1:
        print("OK")
    else:
        print("Gresit")

    print("______________________________________________________________________________")












