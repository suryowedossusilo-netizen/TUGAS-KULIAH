class FPB_KPK:
    def __init__(self, bil1, bil2):
        self.bil1 = bil1
        self.bil2 = bil2
    
    def hitungFPB(self):
        # Algoritma Euclidean
        a = self.bil1
        b = self.bil2
        while b != 0:
            a, b = b, a % b
        return a
    
    def hitungKPK(self):
        # KPK = (bil1 * bil2) / FPB
        fpb = self.hitungFPB()
        return abs(self.bil1 * self.bil2) // fpb
    
    def cetakHasil(self):
        print(f"Bilangan 1: {self.bil1}")
        print(f"Bilangan 2: {self.bil2}")
        print(f"FPB: {self.hitungFPB()}")
        print(f"KPK: {self.hitungKPK()}")

# Scenario penggunaan
print("\n" + "=" * 40)
print("TUGAS 5: FPB & KPK")
print("=" * 40)

# Contoh 1
print("--- Contoh 1 ---")
fpb_kpk1 = FPB_KPK(12, 18)
fpb_kpk1.cetakHasil()

# Contoh 2
print("\n--- Contoh 2 ---")
fpb_kpk2 = FPB_KPK(25, 35)
fpb_kpk2.cetakHasil()

# Contoh 3
print("\n--- Contoh 3 ---")
fpb_kpk3 = FPB_KPK(7, 13)
fpb_kpk3.cetakHasil()