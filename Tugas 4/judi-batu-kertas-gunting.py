import random
import sys

def batu_kertas_gunting_judi():
    print("=" * 60)
    print("🎰  SELAMAT DATANG DI GAME BATU KERTAS GUNTING  🎰")
    print("=" * 60)
    print("")
    print("Aturan:")
    print("• Kamu punya 3 nyawa (kesempatan)")
    print("• Menang = +10 poin")
    print("• Seri = 0 poin (tidak berubah)")
    print("• Kalah = nyawa berkurang 1")
    print("• Game over jika nyawa habis")
    print("=" * 60)
    
    nyawa = 3
    poin = 0
    pilihan_valid = ['batu', 'kertas', 'gunting']
    total_main = 0
    total_menang = 0
    total_kalah = 0
    total_seri = 0
    
    while nyawa > 0:
        print(f"\n❤️  Nyawa: {nyawa}  |  🏆 Poin: {poin}")
        print("-" * 40)

        try:
            pemain = input("Pilih (batu/kertas/gunting): ").strip().lower()
        except EOFError:
            print("\n❌ Input dibatalkan!")
            break
        except KeyboardInterrupt:
            print("\n\n👋 Game dihentikan!")
            sys.exit()
        
        if not pemain:
            print("❌ Input tidak boleh kosong!")
            continue
        
        if pemain not in pilihan_valid:
            print("❌ Pilihan tidak valid! Pilih: batu/kertas/gunting")
            continue
        
        total_main += 1
        
        komputer = pilih_komputer_judi(pemain, pilihan_valid)
        
        print(f"\n🧑 Kamu: {pemain}")
        print(f"🤖 Komputer: {komputer}")
        if pemain == komputer:
            total_seri += 1
            print("🤝 HASIL: SERI! Poin tidak berubah.")
            
        elif (
            (pemain == "batu" and komputer == "gunting") or
            (pemain == "kertas" and komputer == "batu") or
            (pemain == "gunting" and komputer == "kertas")
        ):
            total_menang += 1
            poin += 10
            print("🎉 HASIL: MENANG! +10 poin!")
            print("   💰 Sistem judi bekerja dengan baik!")
            
        else:
            total_kalah += 1
            nyawa -= 1
            print("💔 HASIL: KALAH! Nyawa berkurang 1.")
    print("\n" + "=" * 60)
    print("💀  G A M E   O V E R  💀")
    print("=" * 60)
    print(f"🏆 Total Poin Akhir: {poin}")
    print("-" * 60)
    while True:
        try:
            lanjut = input("\n🔄 Ingin lanjutkan permainan? (ya/tidak): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Terima kasih sudah bermain!")
            break
        
        if lanjut in ['ya', 'y', 'yes']:
            batu_kertas_gunting_judi()
            break
        elif lanjut in ['tidak', 't', 'no', 'n']:
            print("\n👋 Terima kasih sudah bermain!")
            print(f"🏆 Poin akhir Anda: {poin}")
            break
        else:
            print("❌ Masukkan 'ya' atau 'tidak' saja!")


def pilih_komputer_judi(pemain, pilihan_valid):
    lawan_pemain = {
        'batu': 'gunting',      
        'kertas': 'batu',      
        'gunting': 'kertas'     
    }
    mengalahkan_pemain = {
        'batu': 'kertas',       
        'kertas': 'gunting',    
        'gunting': 'batu'      
    }
    peluang = random.randint(1, 100)
    if peluang <= 30:
        return lawan_pemain[pemain]
    elif peluang <= 65:
        return pemain
    else:
        return mengalahkan_pemain[pemain]
def hitung_persen(nilai, total):
    """Hitung persentase dengan aman"""
    if total == 0:
        return 0
    return round((nilai / total) * 100, 1)
if __name__ == "__main__":
    batu_kertas_gunting_judi()