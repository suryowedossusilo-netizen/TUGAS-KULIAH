class PemainSepakbola:
    def __init__(self, nama, nomor_punggung, posisi, klub):
        self.nama = nama
        self.nomor_punggung = nomor_punggung
        self.posisi = posisi
        self.klub = klub
        self.gol = 0  # default 0 gol
    
    def cetakInfo(self):
        print(f"Nama: {self.nama}")
        print(f"No Punggung: {self.nomor_punggung}")
        print(f"Posisi: {self.posisi}")
        print(f"Klub: {self.klub}")
        print(f"Gol: {self.gol}")
    
    def cetakGol(self):
        print(f"{self.nama} telah mencetak {self.gol} gol")
    
    def tambahGol(self, jumlah):
        self.gol += jumlah
        print(f"{self.nama} mencetak {jumlah} gol! Total gol: {self.gol}")
    
    def pindahKlub(self, klub_baru):
        print(f"{self.nama} pindah dari {self.klub} ke {klub_baru}")
        self.klub = klub_baru

# Scenario penggunaan
print("=" * 40)
print("TUGAS 1: PEMAIN SEPAKBOLA")
print("=" * 40)
pemain1 = PemainSepakbola("Lionel Messi", 10, "Penyerang", "Inter Miami")
pemain1.cetakInfo()
print("-" * 20)
pemain1.tambahGol(2)
pemain1.tambahGol(1)
pemain1.cetakGol()
print("-" * 20)
pemain1.pindahKlub("Barcelona")
pemain1.cetakInfo()