# Import
import os

# Variabel
waktu_luang, daftar_kegiatan, kegiatan_terpilih, total_waktu = 0, [], [], 0

# Function
def cekInputWaktu(kata):
    temp = 0
    while True:
        try:
            temp = int(input(f"Masukkan waktu {kata}(dalam menit): "))
            if temp > 0:
                break
            else:
                print("Waktu > 0! ")
        except:
            print("Masukkan angka!!")
    return temp

# Waktu luang
waktu_luang = cekInputWaktu("luang")

# Daftar kegiatan
while True:
    nama_kegiatan = input("Masukkan nama kegiatan: ")
    if nama_kegiatan.lower() not in [a[0].lower() for a in daftar_kegiatan]:
        waktu_kegiatan, temp = cekInputWaktu("kegiatan"), -1

        # Urutkan
        for a in range(len(daftar_kegiatan)):
            if waktu_kegiatan > daftar_kegiatan[a][1]:
                temp = a
                break
        daftar_kegiatan.insert(temp, [nama_kegiatan, waktu_kegiatan]) if temp > -1 else daftar_kegiatan.append([nama_kegiatan, waktu_kegiatan])
    else:
        print("Nama kegiatan sudah ada")

    if input("Masukkan 'y' untuk input lagi: ") != "y":
        break

# Tampilkan
os.system("cls")
print("Daftar kegiatan: ")
for a in range(len(daftar_kegiatan)):
    print(f"{a + 1}. {daftar_kegiatan[a][0]}({daftar_kegiatan[a][1]} menit)")

# Cari dan tampilkan
print(f"\nWaktu luang: {waktu_luang} menit\nKegiatan terpilih:")
for a in daftar_kegiatan:
    if waktu_luang >= (total_waktu + a[1]):
        kegiatan_terpilih.append(a)
        total_waktu += a[1]
        print(f"{len(kegiatan_terpilih)}. {a[0]}({a[1]} menit)")
        if waktu_luang == total_waktu:
            break
print(f"Total waktu: {total_waktu}")