import random

def game_tebak_angka():
    print("=" * 40)
    print("SELAMAT DATANG DI GAME TEBAK ANGKA")
    print("=" * 40)
    print("saya sudah memilih angka rahasia dari angka 1 - 10")
    print("coba tebak angakanya !")
    print("-" * 40)

    # komputer akan memilih angka sesuai perintah 1-10
    angka_rahasia = random.randint(1, 10)

    percobaan = 0  # Sebaiknya mulai dari 0, bukan 5

    while True:
        try:
            # input dari pemain
            tebakan = input("\nMasukan tebakan mu (1-10): ")

            # menu untuk cek pemain ingin melanjutkan game atau ingin menyudahi permainan
            if tebakan.lower() == 'exit':
                print("terimakasih sudah bermain")
                break

            tebakan = int(tebakan)
            percobaan += 1

            # validasi Range perintah angka
            if tebakan < 1 or tebakan > 10:
                print("!! angka harus antara 1 - 10")
                continue

            # untuk cek tebakan benar atau salah
            if tebakan < angka_rahasia:
                print("terlalu kecil ! coba angka yang lebih besar.")
            elif tebakan > angka_rahasia:
                print("terlalu besar ! coba angka yang lebih kecil.")
            else:
                print("\n" + "=" * 40)
                print(f"YEEAAAYYY!, tebakan kamu benar!")
                print(f"Angka rahasia adalah: {angka_rahasia}")
                print(f"jumlah percobaan: {percobaan}")
                print("=" * 40)

                # program akan bertanya apakah pemain ingin melanjutkan game
                main_lagi = input("\nMau main lagi? (ya / tidak): ").lower()
                if main_lagi == 'ya':
                    game_tebak_angka()
                    break  # Penting: break setelah recursive call
                else:
                    print("Terimakasih sudah bermain! sampai jumpa!")
                    break

        except ValueError:
            print("MAsukan angka yang valid!")

if __name__ == "__main__":
    game_tebak_angka()