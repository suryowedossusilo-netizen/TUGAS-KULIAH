print("=" * 60)
print("TUGAS 2: EXCEPTION UNTUK ImportError")
print("=" * 60)

print("\n>>> Kasus 1: Modul tidak ada")
try:
    import modul_tidak_ada_xyz
except ImportError as e:
    print(f"ImportError tertangkap!")
    print(f"     Modul 'modul_tidak_ada_xyz' tidak ditemukan.")
    print(f"     Detail: {e}")
    print(f"\n  Penjelasan: Python mencari modul di sys.path")
    print(f"     tetapi tidak menemukan file 'modul_tidak_ada_xyz.py'")

print("\n>>> Kasus 2: Submodul tidak ada")
try:
    from os import submodul_tidak_ada_xyz
except ImportError as e:
    print(f"ImportError tertangkap!")
    print(f"Submodul 'submodul_tidak_ada_xyz' tidak ada di dalam 'os'")
    print(f"Detail: {e}")
    print(f"\n Penjelasan: Modul 'os' ada, tetapi atribut/fungsi")
    print(f"'submodul_tidak_ada_xyz' tidak didefinisikan di dalamnya")

print("\n>>> Kasus 3: Import berhasil")
try:
    import math
    print(f"Modul 'math' berhasil diimport!")
    print(f"math.pi = {math.pi}")
except ImportError as e:
    print(f"ImportError: {e}")