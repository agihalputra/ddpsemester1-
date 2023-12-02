def duplikasi(list_buah):
    buah_duplikat = []

    for buah in list_buah:
        buah_duplikat.extend([buah, buah])

    return buah_duplikat

list_buah_asli = ['pepaya', 'mangga', 'pisang','durian','jambu']
list_buah_hasil_duplikasi = duplikasi(list_buah_asli)

print('list buah asli: ', list_buah_asli)
print('list buah dengan aplikasi: ', list_buah_hasil_duplikasi)
