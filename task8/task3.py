def cari_ganjil(angka):
    for i in range(angka + 1):
        if i % 2 != 0:
            print('angka ganjil ditemukan: ',i)
        
cari_ganjil(100)