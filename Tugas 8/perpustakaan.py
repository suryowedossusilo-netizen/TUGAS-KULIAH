python_code=''''''
class Buku:
    def __init__(self, kodeBuku, judul, penulis, tahunTerbit, stok):
        self._kodeBuku = kodeBuku
        self._judul = judul
        self._penulis = penulis
        self._tahunTerbit = tahunTerbit
        self._stok = stok
        
    @property
    def kodeBuku(self):
        return self._kodeBuku
    
    @property
    def judul(self):
        return self._judul
    
    @property
    def penulis(self):
        return self._penulis
    
    @property
    def tahunTerbit(self):
        return self._tahunTerbit
    
    @property
    def stok(self):
        return self._stok
    
    @stok.setter
    def stok(self, value):
        if value < 0:
            print("Error: Stok tidak boleh kurang dari 0! Stok diatur ke 0.")
            self._stok = 0
        else:
            self._stok = value
            
    def tampilInfo(self):
        print(f"Kode Buku    : {self._kodeBuku}")
        print(f"Judul        : {self._judul}")
        print(f"Penulis      : {self._penulis}")
        print(f"Tahun Terbit : {self._tahunTerbit}")
        print(f"Stok         : {self._stok}")
        
class BukuPelajaran(Buku):
    def __init__(self, kodeBuku, judul, penulis, tahunTerbit, stok, mataPelajaran):
        super().__init__(kodeBuku, judul, penulis, tahunTerbit, stok)
        self._mataPelajaran = mataPelajaran
        
    @property
    def mataPelajaran(self):
        return self._mataPelajaran
    
    def tampilInfo(self):
        print("\n=== Buku Pelajaran ===")
        super().tampilInfo()
        print(f"Mata Pelajaran : {self._mataPelajaran}")
        
class Novel(Buku):
    def __init__(self, kodeBuku, judul, penulis, tahunTerbit, stok, genre):
        super().__init__(kodeBuku, judul, penulis, tahunTerbit, stok)
        self._genre = genre
        
    @property
    def genre(self):
        return self._genre
    
    def tampilInfo(self):
        print("\n=== Novel ===")
        super().tampilInfo()
        print(f"Genre          : {self._genre}")
        
        
class Majalah(Buku):
    def __init__(self, kodeBuku, judul, penulis, tahunTerbit, stok, edisi):
        super().__init__(kodeBuku, judul, penulis, tahunTerbit, stok)
        self._edisi = edisi
        
    @property
    def edisi(self):
        return self._edisi
    
    def tampilInfo(self):
        print("\n=== Majalah ===")
        super().tampilInfo()
        print(f"Edisi          : {self._edisi}")
        
class SistemManajemenBuku:
    def __init__(self):
        self.daftarBuku = []
        self._initData()
        
    def _initData(self):
        self.daftarBuku.append(BukuPelajaran("BP001", "Matematika Dasar", "Prof. Budi Santoso", 2020, 15, "Matematika"))
        self.daftarBuku.append(BukuPelajaran("BP002", "Fisika Modern", "Dr. Andi Wijaya", 2021, 10, "Fisika"))
        self.daftarBuku.append(BukuPelajaran("BP003", "Algoritma Pemrograman", "Rina Susanti, M.Kom", 2022, 20, "Informatika"))
        self.daftarBuku.append(Novel("NV001", "Laskar Pelangi", "Andrea Hirata", 2005, 8, "Drama"))
        self.daftarBuku.append(Novel("NV002", "Bumi", "Tere Liye", 2014, 12, "Fantasi"))
        self.daftarBuku.append(Novel("NV003", "Dilan 1990", "Pidi Baiq", 2014, 5, "Romantis"))
        self.daftarBuku.append(Majalah("MJ001", "National Geographic Indonesia", "NG Team", 2024, 30, "Januari 2024"))
        self.daftarBuku.append(Majalah("MJ002", "Tempo", "Tempo Media", 2024, 25, "Februari 2024"))

        print("8 data buku berhasil diinisialisasi!")
        
    def tambahBuku(self):
        print("\n--- Tambah Buku ---")
        print("Pilih jenis buku:")
        print("1. Buku Pelajaran")
        print("2. Novel")
        print("3. Majalah")
        jenis = input("Pilih: ")
        
        kode = input("Kode Buku    : ")
        judul = input("Judul        : ")
        penulis = input("Penulis      : ")
        tahun = int(input("Tahun Terbit : "))
        stok = int(input("Stok         : "))
        
        if stok < 0:
            print("Error: Stok tidak boleh kurang dari 0! Stok diatur ke 0.")
            stok = 0
            
        if jenis == "1":
            mapel = input("Mata Pelajaran : ")
            self.daftarBuku.append(BukuPelajaran(kode, judul, penulis, tahun, stok, mapel))
        elif jenis == "2":
            genre = input("Genre          : ")
            self.daftarBuku.append(Novel(kode, judul, penulis, tahun, stok, genre))
        elif jenis == "3":
            edisi = input("Edisi          : ")
            self.daftarBuku.append(Majalah(kode, judul, penulis, tahun, stok, edisi))
        else:
            print("Jenis buku tidak valid!")
            return
        
        print("Buku berhasil ditambahkan!")
        
    def cariBuku(self):
        cariJudul = input("\nMasukkan judul buku yang dicari: ").lower()
        ditemukan = False
        
        for b in self.daftarBuku:
            if cariJudul in b.judul.lower():
                b.tampilInfo()
                ditemukan = True
                
        if not ditemukan:
            print(f'Buku dengan judul "{cariJudul}" tidak ditemukan.')
            
    def tampilkanSemuaBuku(self):
        print("\n=== DAFTAR SEMUA BUKU ===")
        if not self.daftarBuku:
            print("Belum ada data buku.")
            return
        for b in self.daftarBuku:
            b.tampilInfo()
        print(f"\nTotal buku: {len(self.daftarBuku)}")
        
    def run(self):
        while True:
            print("\n===== MENU UTAMA =====")
            print("1. Tambah Buku")
            print("2. Cari Buku berdasarkan Judul")
            print("3. Tampilkan Semua Buku")
            print("4. Keluar")
            pilihan = input("Pilih menu: ")
            
            if pilihan == "1":
                self.tambahBuku()
            elif pilihan == "2":
                self.cariBuku()
            elif pilihan == "3":
                self.tampilkanSemuaBuku()
            elif pilihan == "4":
                print("Program selesai. Terima kasih!")
                break
            else:
                print("Pilihan tidak valid!")
                
if __name__ == "__main__":
    sistem = SistemManajemenBuku()
    sistem.run()
    
output_path = "/mnt/agents/output/sistem_manajemen_buku.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(python_code)

print(f"File berhasil disimpan ke: {output_path}")