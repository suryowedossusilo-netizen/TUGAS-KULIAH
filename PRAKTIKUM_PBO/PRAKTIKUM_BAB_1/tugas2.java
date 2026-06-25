import random

class Pintu:
    def __init__(self, status_awal=False):
        self.status = status_awal
        self.respon_buka = [
            "🚪 Pintu terbuka dengan suara berdecit...",
            "🚪 Pintu terbuka halus tanpa suara.",
            "🚪 Pintu terbuka dengan keras! BANG!",
            "🚪 Pintu terbuka perlahan dengan suara misterius...",
            "🚪 Pintu terbuka dan angin sejuk masuk.",
            "🚪 Pintu terbuka dengan bunyi 'CREEEEAK' lama.",
            "🚪 Pintu terbuka, ada seseorang di baliknya?!",
            "🚪 Pintu terbuka dengan mudah, seolah mengundang masuk."
        ]
        
        self.respon_tutup = [
            "🚪 Pintu ditutup dengan lembut...",
            "🚪 Pintu ditutup dengan keras! BAM!",
            "🚪 Pintu ditutup dan terkunci otomatis.",
            "🚪 Pintu ditutup dengan suara berdecit aneh.",
            "🚪 Pintu ditutup, suasana menjadi sunyi.",
            "🚪 Pintu ditutup dengan bunyi 'THUD' berat.",
            "🚪 Pintu ditutup, tapi ada suara ketukan dari luar!",
            "🚪 Pintu ditutup rapat, aman dan nyaman."
        ]
    
    def buka(self):
        if self.status:
            print("⚠️  Pintu sudah terbuka! Tidak perlu dibuka lagi.")
        else:
            self.status = True
            indeks_acak = random.randint(0, len(self.respon_buka) - 1)
            print(self.respon_buka[indeks_acak])
            print("   Status: PINTU TERBUKA ✅\n")
    
    def tutup(self):
        if not self.status:
            print("⚠️  Pintu sudah tertutup! Tidak perlu ditutup lagi.")
        else:
            self.status = False
            indeks_acak = random.randint(0, len(self.respon_tutup) - 1)
            print(self.respon_tutup[indeks_acak])
            print("   Status: PINTU TERTUTUP ❌\n")
    
    def is_terbuka(self):
        return self.status
    
    def get_status(self):
        return "TERBUKA" if self.status else "TERTUTUP"
    
    def cetak_info(self):
        print("╔══════════════════════════════════════╗")
        print("║           INFORMASI PINTU            ║")
        print("╠══════════════════════════════════════╣")
        print(f"║ Status: {self.get_status():<27} ║")
        print("╚══════════════════════════════════════╝")


# Contoh penggunaan:
if __name__ == "__main__":
    pintu = Pintu()
    pintu.cetak_info()
    pintu.buka()
    pintu.tutup()
    pintu.buka()
    pintu.cetak_info()
