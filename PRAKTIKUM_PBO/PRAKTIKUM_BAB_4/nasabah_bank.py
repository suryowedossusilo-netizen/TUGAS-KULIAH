
# 
class Tabungan:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def getSaldo(self):
        return self.__saldo
    
    def simpanUang(self, jumlah):
        self.__saldo += jumlah
    
    def ambilUang(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        else:
            return False


class Nasabah:
    def __init__(self, namaAwal, namaAkhir):
        self.__namaAwal = namaAwal
        self.__namaAkhir = namaAkhir
        self.__tabungan = None
    
    def getNamaAwal(self):
        return self.__namaAwal
    
    def getNamaAkhir(self):
        return self.__namaAkhir
    
    def setTabungan(self, tabungan):
        self.__tabungan = tabungan
    
    def getTabungan(self):
        return self.__tabungan


class Bank:
    def __init__(self):
        self.__nasabah = []
    
    def tambahNasabah(self, namaAwal, namaAkhir):
        nasabah = Nasabah(namaAwal, namaAkhir)
        self.__nasabah.append(nasabah)
    
    def getNasabah(self, index):
        return self.__nasabah[index]
    
    def getJumlahNasabah(self):
        return len(self.__nasabah)


print("=" * 50)
print("TUGAS 1: BANK - NASABAH - TABUNGAN")
print("=" * 50)
print("\n--- Latihan: Komposisi Nasabah-Tabungan ---")
nasabah = Nasabah("Agus", "Daryanto")
print(f"Nasabah atas nama {nasabah.getNamaAwal()} {nasabah.getNamaAkhir()}")
tabungan = Tabungan(1500000)
nasabah.setTabungan(tabungan)
print(f"Saldo awal tabungan: Rp {nasabah.getTabungan().getSaldo()}")
nasabah.getTabungan().simpanUang(500000)
print("Menyimpan uang sebesar: 500000")
print("Saldo sekarang: ", nasabah.getTabungan().getSaldo())
cek = nasabah.getTabungan().ambilUang(2200000)
print("Mengambil uang sebesar: 2200000")
if cek == True:
    print("Pengambilan Uang Berhasil")
else:
    print("Pengambilan Uang Gagal")
print("Saldo sekarang: ", nasabah.getTabungan().getSaldo())
cek = nasabah.getTabungan().ambilUang(1000000)
print("Mengambil uang sebesar: 1000000")
if cek == True:
    print("Pengambilan Uang Berhasil")
else:
    print("Pengambilan Uang Gagal")
print("Saldo sekarang: ", nasabah.getTabungan().getSaldo())
print("\n--- Tugas 1: Agregasi Bank-Nasabah ---")
bank = Bank()
bank.tambahNasabah("Malik", "Ibrahim")
bank.getNasabah(0).setTabungan(Tabungan(500000))
bank.tambahNasabah("Tutik", "Amaliah")
bank.getNasabah(1).setTabungan(Tabungan(300000))
bank.tambahNasabah("Wahid", "Elyasa")
bank.getNasabah(2).setTabungan(Tabungan(100000))
print("Jumlah nasabah: ", bank.getJumlahNasabah())
for i in range(bank.getJumlahNasabah()):
    print(f"Nasabah ke-{i+1}: {bank.getNasabah(i).getNamaAwal()} {bank.getNasabah(i).getNamaAkhir()} ; Saldo: Rp {bank.getNasabah(i).getTabungan().getSaldo()}")