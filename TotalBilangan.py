N = int(input("Masukkan Jumlah Mahasiswa : "))
print("----------------------------")
sum = 0

for i in range(1, N+1):
    data = int(input("Masukkan Nilai Mahasiswa ke- " + str(i) + " : "))
    sum += data

avg = float(sum) / float(N)
print("------------------------------")
print("Rata - Rata Nilai Mahasiswa : ", avg)
