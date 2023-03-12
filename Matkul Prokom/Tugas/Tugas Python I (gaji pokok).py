print("==================================")
Nama          = str(input("Masukkan nama lengkap karyawan  = "))
Kel_jam_kerja = float(input("Masukkan kelebihan jam kerja    = "))
Golongan      = int(input("Masukkan golongan karyawan      = "))
Gaji_pokok    = Golongan * 1000000
Lembur        = Golongan * 200000
Pendapatan    = Gaji_pokok + Lembur
print("==================================")
print("Nama Karyawan    =" , Nama)
print("Golongan         =" , Golongan)
print("Gaji Pokok       =" , Gaji_pokok)
print("Uang Lembur      =" , Lembur)
print("Take Home Pay    =" , Pendapatan)
print("==================================")