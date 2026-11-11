import math

# Data lokasi (nama, x, y)
lokasi = {
    'A': (2, 3), 'B': (5, 7), 'C': (9, 2), 'D': (12, 8),
    'E': (15, 4), 'F': (7, 11), 'G': (14, 14), 'H': (4, 1)
}

def jarak(p, q):
    return math.hypot(lokasi[p][0] - lokasi[q][0],
                      lokasi[p][1] - lokasi[q][1])

def greedy_terdekat(awal):
    belum = set(lokasi) - {awal}
    rute, total, posisi = [awal], 0.0, awal
    while belum:
        berikutnya = min(belum, key=lambda t: jarak(posisi, t))
        total += jarak(posisi, berikutnya)
        rute.append(berikutnya)
        belum.remove(berikutnya)
        posisi = berikutnya
    total += jarak(posisi, awal)   # kembali ke titik awal
    rute.append(awal)
    return rute, total

rute, total = greedy_terdekat('A')
print("Rute akhir :", ' -> '.join(rute))
print(f"Total jarak: {total:.2f}")