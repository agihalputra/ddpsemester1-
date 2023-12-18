from gempa import *
    
# Membuat objek-objek gempa
gempa_Banten = Gempa("Banten", 1.2)
gempa_Palu = Gempa("Palu", 6.1)
gempa_Cianjur = Gempa("Cianjur", 5.6)
gempa_Jayapura = Gempa("Jayapura", 3.3)
gempa_Garut = Gempa("Garut", 4.0)
gempa_jakarta = Gempa("Jakarta",5.0)

# Menampilkan Informasi Penting
print(gempa_Banten.dampak())
print(gempa_Palu.dampak())
print(gempa_Cianjur.dampak())
print(gempa_Jayapura.dampak())
print(gempa_Garut.dampak())
print(gempa_jakarta.dampak())



