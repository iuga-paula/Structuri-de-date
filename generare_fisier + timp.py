import random
import time

def verif_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return -1
    return 1

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
    start_time = time.time()
    lista.sort()
    print("sortarea by default din python a durat:", end='')
    print("--- %s seconds ---" % (time.time() - start_time))
    if verif_sort(lista) != 1:
        print("sort nu a sortat bine lista")
    else:
        print("sort a sortat bine lista")
    print("--------------------------------")
    # print(lista)
    # print(verif_sort(lista))

# g1 = open("test1.txt")
# s = g1.readline()
# print(s)
# g1.close()
#
# f = open("test4.txt")
# s = f.readlines()
# print(len(s))
# f.close()




