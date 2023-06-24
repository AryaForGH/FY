print("=============== DATA LIST BY ARYA ===============")
# Contoh Sederhana Data List
list1 = ['Arya', 'Ganteng', 'Iyain']   # Data List String 
list2 = [1, 5, 10]                      # Data List Integer
list3 = [7, 'Megawati', 11]             # Data List Campuran

print()
print("------------ Data List ------------")
print(list1)        # Function Untuk Mengambil Seluruh Data Di List 1
print(list2)        # Function Untuk Mengambil Seluruh Data Di List 2
print(list3)        # Function Untuk Mengambil Seluruh Data Di List 3

""" 
    Lalu, Kita Akan Membuat Function Mengambil Data
    Maksudnya, Kita Akan Mengambil Salah Satu Data di Antara List di Atas
    Excample : 
    Pada Data List 1, Kita Akan Mengambil Data Pertama
    Maka     :
"""
print()
print("---------- Get Data List ----------")
print(list1[0])       # ----> Arya
print(list2[-1])      # ----> 5
print(list3[0:2])     # ----> 7 Megawati 


    # Lalu, Kita Akan Mempelajari Fungsi Append
    # Append Berfungsi Untuk Menambah Nilai Baru Pada Sebuah Data List
print()
print("------------- APPEND --------------")
list_petinggi_negara = ['Jokowi', 'Puan', 'Megawati']   # ----> Jokowi, Puan, Megawati
list_petinggi_negara.append('Asep, Joni')
print(list_petinggi_negara)

    # Fungsi Lain Yang Tidak Kalah Penting Adalah Fungsi Remove
    # Fungsi Remove Berfungsi Untuk Menghapus Nilai Pada Sebuah Data List
print()
print("------------- REMOVE -------------")
macam = ['Balmond', 'Idihhh', 'Apasih', 'Hadeuh', 'Blog'] # ----> 'Balmond', 'Idihhh', 'Apasih', 'Hadeuh', 'Blog'
macam.remove("Balmond")
print(macam)

print()