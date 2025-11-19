# Import
import os

# Variabel
waktu_luang, daftar_kegiatan, kegiatan_terpilih, total_waktu, kegiatan_tdkterpilih, salinan_terpilih = 0, [], [], 0, [], []

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

def convertWaktu(jenis, waktu):
    if waktu == 0:
        print(f"{jenis}: Habis")
    elif waktu % 60 == 0:
        print(f"{jenis}: {waktu // 60}jam")
    elif waktu > 60:
        print(f"{jenis}: {waktu // 60}jam {waktu % 60}menit")
    else:
        print(f"{jenis}: {waktu}menit")

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

# Tampilkan daftar
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
convertWaktu("Total waktu", total_waktu)
convertWaktu("Sisa waktu", waktu_luang - total_waktu)

# Cari kegiatan yang tidak masuk terpilih
salinan_terpilih = [a[0] for a in kegiatan_terpilih]
for a in daftar_kegiatan:
    if a[0] not in salinan_terpilih:
        kegiatan_tdkterpilih.append(a)

# Jika ada kegiatan tidak terpilih
if len(kegiatan_tdkterpilih) >= 1:
    # Tampilkan kegiatan tidak terpilih dan input tambahan waktu luang
    print("\nKegiatan tidak terpilih:")
    for a in range(len(kegiatan_tdkterpilih)):
        print(f"{a + 1}. {kegiatan_tdkterpilih[a][0]}({kegiatan_tdkterpilih[a][1]}menit)")
    waktu_luang += cekInputWaktu("luang tambahan")

    # Cek untuk memasukkan kegiatan tidak terpilih
    flag_tdkterpilih = True
    for a in kegiatan_tdkterpilih:
        if waktu_luang >= (total_waktu + a[1]):
            kegiatan_terpilih.append(a)
            total_waktu += a[1]
            flag_tdkterpilih = False
            if waktu_luang == total_waktu:
                break
    
    # Jika true maka tidak ada kegiatan baru yang ditambahkan
    if flag_tdkterpilih:
        print("Waktu luang tidak cukup, tidak bisa menambahkan kegiatan")
        exit()

# Jika ada waktu sisa
elif (waktu_luang - total_waktu) > 0:
    #Keluar program jika tidak ingin input kegiatan lagi
    if input("Masih ada sisa waktu, ingin input kegiatan lagi?(y/t): ") != "y":
        exit()
    
    # Input kegiatan dan cek dan masukkan
    kegiatan = [input("Masukkan nama kegiatan: "), cekInputWaktu("kegiatan")]
    if kegiatan[1] > (waktu_luang - total_waktu):
        print("Waktu luang tidak cukup, tidak bisa menambahkan kegiatan")
        exit()
    daftar_kegiatan.append(kegiatan)
    kegiatan_terpilih.append(kegiatan)
    total_waktu += kegiatan[1]

# #Tampilkan daftar
os.system("cls")
print("Diperbarui!!\nDaftar kegiatan: ")
for a in range(len(daftar_kegiatan)):
    print(f"{a + 1}. {daftar_kegiatan[a][0]}({daftar_kegiatan[a][1]} menit)")

# Tampilkan kegiatan terpilih
print(f"\nWaktu luang: {waktu_luang} menit\nKegiatan terpilih:")
for a in range(len(kegiatan_terpilih)):
    print(f"{a + 1}. {kegiatan_terpilih[a][0]}({kegiatan_terpilih[a][1]} menit)")
convertWaktu("Total waktu", total_waktu)
convertWaktu("Sisa waktu", waktu_luang - total_waktu)
