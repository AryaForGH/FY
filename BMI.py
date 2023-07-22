import tkinter as tk 

def hitung_bunga():
    try:
        jumlah_pokok = float(jumlah_pokok_entry.get())
        tingkat_bunga = float(tingkat_bunga_entry.get())
        periode = float(periode_entry.get())

        bunga = jumlah_pokok * (tingkat_bunga / 100) * periode
        hasil_label.config(text=f"Bunga yang diperoleh : {bunga:.2f}")
    except ValueError:
        hasil_label.config(text="Masukkan Angka")

def hitung_cicilan():
    try:
        jumlah_pinjaman = float(jumlah_pinjaman_entry.get())
        tingkat_bunga = float(tingkat_bunga_entry.get())
        periode = float(periode_entry.get())

        tingkat_bunga_bulanan = (tingkat_bunga / 100) / 12
        jumlah_cicilan = jumlah_pinjaman * (tingkat_bunga_bulanan * (1 + tingkat_bunga_bulanan) ** periode) / (((1 +        tingkat_bunga_bulanan) ** periode) -1)

        hasil_label.config(text=f"Cicilan bulanan : {jumlah_cicilan:.2f}")
    except ValueError:
        hasil_label.config(text="Masukkan Angka")

def hitung_investasi():
    try:
        investasi_awal = float(investasi_awal_entry.get())
        tingkat_bunga = float(tingkat_bunga_entry.get())
        periode = float(periode_entry.get())

        hasil_investasi = investasi_awal*((1+(tingkat_bunga/100))**periode)

        hasil_label.config(text=f"Nilai Investasi setelah {periode} tahun : {hasil_investasi:.2f}")
    except ValueError:
        hasil_label.config(text="Masukkan Angka")

root = tk.Tk()
root.title("Kalkulator Keuangan")

jumlah_pokok_label = tk.Label(root, text="Jumlah Pokok")
jumlah_pokok_label.pack()
jumlah_pokok_entry = tk.Entry(root)
jumlah_pokok_entry.pack()

jumlah_pinjaman_label = tk.Label(root, text="Jumlah Pinjaman")
jumlah_pinjaman_label.pack()
jumlah_pinjaman_entry = tk.Entry(root)
jumlah_pinjaman_entry.pack()

investasi_awal_label = tk.Label(root, text="Investasi Awal")
investasi_awal_label.pack()
investasi_awal_entry = tk.Entry(root)
investasi_awal_entry.pack()

tingkat_bunga_label = tk.Label(root, text="Tingkat Bunga (%)")
tingkat_bunga_label.pack()
tingkat_bunga_entry = tk.Entry(root)
tingkat_bunga_entry.pack()

periode_label = tk.Label(root, text="Periode (Tahun)")
periode_label.pack()
periode_entry = tk.Entry(root)
periode_entry.pack()

hitung_bunga_button = tk.Button(root, text="Hitung Bunga", command=hitung_bunga)
hitung_bunga_button.pack()

hitung_cicilan_button = tk.Button(root, text="Hitung Cicilan", command=hitung_cicilan)
hitung_cicilan_button.pack()

hitung_investasi_button = tk.Button(root, text="Hitung Investasi", command=hitung_investasi)
hitung_investasi_button.pack()

hasil_label = tk.Label(root, text="")
hasil_label.pack()

root.mainloop()