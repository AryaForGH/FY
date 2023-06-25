from array import * 

N = int(input("Masukkan Banyak N : "))

T = array('i',[])

print("Masukkan Bilangan : ")
for i in range(0, N):
    ins = int(input(""))
    T.append(ins)

print("Hasil Bubble Sort : ")
if (len(T) > 1):
    for Pass in range(0, len(T)-1):
        for K in range (len(T)-1, Pass, -1):
            if (T[K] < T[K-1]):
                Temp = T[K]
                T[K] = T[K]
                T[K-1] = Temp

for K in range (0, len(T)):
    print(T[K])