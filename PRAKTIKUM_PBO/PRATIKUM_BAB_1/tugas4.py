class TV:
    def __init__(self):
        self.status = False  # False = mati, True = nyala
        self.saluran = 1
        self.daftar_saluran = ["TVRI", "RCTI", "SCTV", "Trans TV", "Metro TV", 
                              "Indosiar", "ANTV", "NET TV", "Trans 7", "GTV"]
    
    def nyalakan(self):
        if not self.status:
            self.status = True
            print("TV dinyalakan!")
            self.info()
        else:
            print("TV sudah menyala!")
    
    def matikan(self):
        if self.status:
            self.status = False
            print("TV dimatikan!")
        else:
            print("TV sudah mati!")
    
    def gantiSaluran(self, nomor):
        if self.status:
            if 1 <= nomor <= len(self.daftar_saluran):
                self.saluran = nomor
                print(f"Berpindah ke saluran {nomor}")
                self.info()
            else:
                print(f"Saluran tidak tersedia! Pilih 1-{len(self.daftar_saluran)}")
        else:
            print("TV mati! Nyalakan TV terlebih dahulu.")
    
    def saluranSelanjutnya(self):
        if self.status:
            if self.saluran < len(self.daftar_saluran):
                self.saluran += 1
            else:
                self.saluran = 1
            self.info()
        else:
            print("TV mati! Nyalakan TV terlebih dahulu.")
    
    def saluranSebelumnya(self):
        if self.status:
            if self.saluran > 1:
                self.saluran -= 1
            else:
                self.saluran = len(self.daftar_saluran)
            self.info()
        else:
            print("TV mati! Nyalakan TV terlebih dahulu.")
    
    def info(self):
        if self.status:
            print(f"Status: MENYALA | Saluran {self.saluran}: {self.daftar_saluran[self.saluran-1]}")
        else:
            print("Status: MATI")

# Scenario penggunaan
print("\n" + "=" * 40)
print("TUGAS 4: TV")
print("=" * 40)
tv = TV()
tv.info()  # TV mati
tv.gantiSaluran(5)  # Gagal, TV mati
tv.nyalakan()
tv.gantiSaluran(3)
tv.saluranSelanjutnya()
tv.saluranSelanjutnya()
tv.saluranSebelumnya()
tv.matikan()
tv.info()