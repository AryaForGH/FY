print("=============== GAJI KARYAWAN ===============")

jabatan = int(input("Masukkan Jabatan (1. Direktur) (2. Staff) : "))

while (jabatan != 1 and jabatan != 2):
    print("Input Jabatan Tidak Valid")
    jabatan = int(input("Masukkan Jabatan (1. Direktur) (2. Staff) : "))

jumlah_kerja = int(input("Masukkan Jumlah Hari Kerja   : "))

jumlah_lembur = int(input("Masukkan Jumlah Hari Lembur : "))

while (jumlah_lembur > jumlah_kerja):
    print("Hari Lembur Tidak Bisa Lebih Dari Hari Kerja")
    jumlah_lembur = int(input("Masukkan Jumlah Hari Lembur : "))

gaji_total = 0

gaji_pokok = 3_000_000 if jabatan == 1 else 2_000_000
gaji_total = gaji_pokok
print("\nGaji Pokok     : %d" % (gaji_pokok))

uang_transport = 25_000 * jumlah_kerja
gaji_total += gaji_pokok
print("\nUang Transport : %d" % (uang_transport))

uang_lembur = 100_000 * jumlah_lembur
gaji_total += uang_transport
print("\nUang Lembur    : %d" % (uang_lembur))

if (jumlah_kerja > 24 and jumlah_lembur > 5):
    gaji_total += 500_000
    print("Anda Mendapatkan Bonus 500.000")

print("\nGaji Yang Diterima : %d" % (gaji_total))
print()