nilai = int(input('masukan nilai? '))

def kelulusan(nilai):
    if nilai < 0:
        return 'Nilai tidak valid'
    elif nilai <= 60:
        return 'gagal'
    elif nilai <= 70:
        return 'baik'
    elif nilai <= 80:
        return 'Sangat Baik'
    elif nilai <= 100:
        return 'Istimewa'
    else:
        return 'nilai tidal valid'
    
print(kelulusan(nilai))
