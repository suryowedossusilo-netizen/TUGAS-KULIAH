class Segitiga:
    def __init__(self, sisi_a, sisi_b, sisi_c, tinggi):
        self.sisi_a = sisi_a
        self.sisi_b = sisi_b
        self.sisi_c = sisi_c
        self.tinggi = tinggi
    
    def jenisSegitiga(self):
        # Cek segitiga sama sisi
        if self.sisi_a == self.sisi_b == self.sisi_c:
            return "Segitiga Sama Sisi"
        # Cek segitiga sama kaki
        elif self.sisi_a == self.sisi_b or self.sisi_b == self.sisi_c or self.sisi_a == self.sisi_c:
            return "Segitiga Sama Kaki"
        # Cek segitiga siku-siku (Teorema Pythagoras)
        # Urutkan sisi untuk memudahkan pengecekan
        sisi = sorted([self.sisi_a, self.sisi_b, self.sisi_c])
        if sisi[0]**2 + sisi[1]**2 == sisi[2]**2:
            return "Segitiga Siku-Siku"
        else:
            return "Segitiga Sembarang"
    
    def hitungLuas(self):
        # Luas = 1/2 * alas * tinggi (menggunakan sisi_a sebagai alas)
        return 0.5 * self.sisi_a * self.tinggi
    
    def hitungKeliling(self):
        return self.sisi_a + self.sisi_b + self.sisi_c
    
    def cetakInfo(self):
        print(f"Sisi A: {self.sisi_a}")
        print(f"Sisi B: {self.sisi_b}")
        print(f"Sisi C: {self.sisi_c}")
        print(f"Tinggi: {self.tinggi}")
        print(f"Jenis: {self.jenisSegitiga()}")
        print(f"Luas: {self.hitungLuas()}")
        print(f"Keliling: {self.hitungKeliling()}")

# Scenario penggunaan
print("\n" + "=" * 40)
print("TUGAS 3: SEGITIGA")
print("=" * 40)

# Segitiga sama sisi
segitiga1 = Segitiga(5, 5, 5, 4.33)
print("--- Segitiga 1 ---")
segitiga1.cetakInfo()

# Segitiga sama kaki
segitiga2 = Segitiga(5, 5, 8, 3)
print("\n--- Segitiga 2 ---")
segitiga2.cetakInfo()

# Segitiga siku-siku (3, 4, 5)
segitiga3 = Segitiga(3, 4, 5, 4)
print("\n--- Segitiga 3 ---")
segitiga3.cetakInfo()

# Segitiga sembarang
segitiga4 = Segitiga(3, 5, 7, 4)
print("\n--- Segitiga 4 ---")
segitiga4.cetakInfo()