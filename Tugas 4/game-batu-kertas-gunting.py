import random
import sys

def batu_kertas_gunting():
    print("=" * 50)
    print("🎮  SELAMAT DATANG DI GAME BATU KERTAS GUNTING  🎮")
    print("=" * 50)
    print("Aturan:")
    print("• Kamu punya 3 nyawa (kesempatan)")
    print("• Menang = +10 poin")
    print("• Seri = 0 poin (tidak berubah)")
    print("• Kalah = nyawa berkurang 1")
    print("• Game over jika nyawa habis")
    print("=" * 50)
    
    nyawa = 3
    poin = 0
    pilihan_valid = ['batu', 'kertas', 'gunting']
    
    while nyawa > 0:
        print(f"\n❤️  Nyawa: {nyawa}  |  🏆 Poin: {poin}")
        print("-" * 30)

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
        komputer = random.choice(pilihan_valid)
        
        print(f"\n🧑 Kamu: {pemain}")
        print(f"🤖 Komputer: {komputer}")
        if pemain == komputer:
            print("🤝 HASIL: SERI! Poin tidak berubah.")
            
        elif (
            (pemain == "batu" and komputer == "gunting") or
            (pemain == "kertas" and komputer == "batu") or
            (pemain == "gunting" and komputer == "kertas")
        ):
            poin += 10
            print("🎉 HASIL: MENANG! +10 poin!")
            
        else:
            nyawa -= 1
            print("💔 HASIL: KALAH! Nyawa berkurang 1.")
    print("\n" + "=" * 50)
    print("💀  G A M E   O V E R  💀")
    print("=" * 50)
    print(f"🏆 Total Poin Akhir: {poin}")
    print("-" * 50)

    while True:
        try:
            lanjut = input("\n🔄 Ingin lanjutkan permainan? (ya/tidak): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Terima kasih sudah bermain!")
            break
        
        if lanjut in ['ya', 'y', 'yes']:
            batu_kertas_gunting()
            break
        elif lanjut in ['tidak', 't', 'no', 'n']:
            print("\n👋 Terima kasih sudah bermain!")
            print(f"🏆 Poin akhir Anda: {poin}")
            break
        else:
            print("❌ Masukkan 'ya' atau 'tidak' saja!")

if __name__ == "__main__":
    batu_kertas_gunting()