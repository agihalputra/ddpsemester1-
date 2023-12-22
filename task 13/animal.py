class Animal:

    #Atribut/properti
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class badak(Animal):
    def __init__ (self, name, makanan, hidup, berkembang_biak, jenis, tinggi_badan):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.tinggi_badan = tinggi_badan

    def info(self):
        print(f"""\t\t  Nama \t\t  : {self.name}
                  Makanan \t  : {self.makanan}
                  Hidup \t  : {self.hidup}
                  Berkembang Biak : {self.berkembang_biak}
                  Jenis \t  : {self.jenis}
                  Tinggi badan \t  : {self.tinggi_badan}
                  """)
        
class ikan(Animal):
    def __init__ (self, name, makanan, hidup, berkembang_biak, jenis, panjang):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.panjang = panjang

    def info(self):
        print(f"""\t\t  Nama \t\t  : {self.name}
                  Makanan \t  : {self.makanan}
                  Hidup \t  : {self.hidup}
                  Berkembang Biak : {self.berkembang_biak}
                  Jenis \t  : {self.jenis}
                  Tinggi badan \t  : {self.panjang}
                  """)
class ular(Animal):
    def __init__ (self, name, makanan, hidup, berkembang_biak, jenis, panjang):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.panjang = panjang

    def info(self):
        print(f"""\t\t  Nama \t\t  : {self.name}
                  Makanan \t  : {self.makanan}
                  Hidup \t  : {self.hidup}
                  Berkembang Biak : {self.berkembang_biak}
                  Jenis \t  : {self.jenis}
                  Tinggi badan \t  : {self.panjang}
                  """)
        

x = badak('Badak Bercula', 'Rumput', 'Hutan','Melahirkan',"Badak gihal","300cm")
x.info()
x = ikan('Tongkol', 'Cacing','Laut','Bertelur', 'Ovipar', '25cm')
x.info()
x = ular('Python', 'Telur', 'Huan', 'Bertelur', 'Berbisa','10m' )
x.info()


