print("============= Perulangan by Arya ============")
print()

for angka in range(0,7): # ----> Maksudnya, i akan Mengurutkan Angka Pada Range 
    print(angka)         # ----> Yaitu Dimulai Dari Angka 0 Hingga 6 Angka Seterusnya
print()


hewan = ['Anjing', 'Babi', 'Ayam', 'Kambing', 'Kamu'] # ----> List

for i in hewan:
    print(i)   # i Merupakan Fungsi Untuk Membuat List Terhadap Nilai Yang Terdapat Pada Variabel 'Hewan'
print()

"""
    PERULANGAN FOR ELSE
    For Else Berfungsi untuk Menampilkan Suatu List dan
    Menampilkan Pesan Bahwa List Telah Ditampilkan Seluruhnya
"""
acak = ['Mobil', 'Motor', 'Pesawat', 'Helikopter']
for i in acak:
    print(i, "Memiliki Huruf Sebanyak : ", len(i))
else:
    print("Semua List Sudah Di Tampilkan")

print()
