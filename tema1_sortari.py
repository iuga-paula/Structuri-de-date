import random
import time

def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1

def bubblesort(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(list) - 1):
            if list[i] >= list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted =  False

    return list

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
    print(lista)

    ps = lista.copy()
    start_time = time.time()
    ps.sort()
    print("sortarea by default din python a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    bs = bubblesort(lista)
    print("bubblesort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))


    if verif_sort(bs) != 1:
        print("bubblesort nu a sortat bine lista")
    else:
        print("bubblesort a sortat bine lista")
    print("--------------------------------")

    start_time = time.time()
    cs = countsort(lista)
    print("countsort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))

    if verif_sort(cs) != 1:
        print("countsort nu a sortat bine lista")
    else:
        print("countsort a sortat bine lista")
    print("--------------------------------")

    start_time = time.time()
    ms = mergesort(lista)
    print("mergesort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))

    if verif_sort(ms) != 1:
        print("mergesort nu a sortat bine lista")
    else:
        print("mergesort a sortat bine lista")
    print("--------------------------------")

    start_time = time.time()
    rs = radixsort(lista)
    print("radixsort a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))

    if verif_sort(rs) != 1:
        print("radixsort nu a sortat bine lista")
    else:
        print("radixsort a sortat bine lista")
    print("--------------------------------")

    start_time = time.time()
    qsm = quicksort(lista, pivot_median)
    print("quicksort cu pivot media medianelor a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))

    if verif_sort(qsm) != 1:
        print("quicksort cu pivot media medianelor  nu a sortat bine lista")
    else:
        print("quicksort cu pivot media medianelor  a sortat bine lista")
    print("--------------------------------")

    start_time = time.time()
    qss = quicksort_classic(lista, 0, len(lista) - 1)
    print("quicksort classic a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))

    if verif_sort(qss) != 1:
        print("quicksort classic  nu a sortat bine lista")
    else:
        print("quicksort classic a sortat bine lista")












