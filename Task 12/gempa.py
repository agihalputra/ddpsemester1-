class Gempa:

# atribut
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            return(f'Gempa di {self.lokasi}, dengan skala : {self.skala} Dampak Gempa tidak berasa.')
        elif 2 <= self.skala < 4:
            return(f'Gempa di {self.lokasi}, dengan skala : {self.skala} Dampak Gempa bangunan retak-retak')
        elif 4 <= self.skala < 6:
            return(f'Gempa di {self.lokasi}, dengan skala : {self.skala} Dampak Gempa Bangunan roboh')
        elif self.skala > 6:
            return(F'Gempa di {self.lokasi}, dengan skala : {self.skala} Dampak Gempa bangunan roboh dan berpotensi Tsunami')



