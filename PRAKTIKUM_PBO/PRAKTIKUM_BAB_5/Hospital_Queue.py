import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('hospital_queue.db')
    cursor = conn.cursor()
   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            umur INTEGER,
            tingkat_urgensi INTEGER,
            status TEXT DEFAULT 'Menunggu',
            waktu_masuk TEXT DEFAULT CURRENT_TIMESTAMP,
            waktu_dipanggil TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print(" Database berhasil diinisialisasi!")

class Patient:
    def __init__(self, nama, umur, tingkat_urgensi):
        self.nama = nama
        self.umur = umur
        self.tingkat_urgensi = tingkat_urgensi
    def __repr__(self):
        return f"Patient({self.nama}, umur={self.umur}, urgensi={self.tingkat_urgensi})"

    def __lt__(self, other):
        return self.tingkat_urgensi > other.tingkat_urgensi


class HospitalQueue:
    def __init__(self):
        self.queue = []
        self.loadFromDB()

    def loadFromDB(self):
        """Memuat pasien yang masih menunggu dari database"""
        conn = sqlite3.connect('hospital_queue.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT nama, umur, tingkat_urgensi 
            FROM patients 
            WHERE status = 'Menunggu'
            ORDER BY tingkat_urgensi DESC, waktu_masuk ASC
        ''')
        rows = cursor.fetchall()
        conn.close()
        
        self.queue = []
        for row in rows:
            self.queue.append(Patient(row[0], row[1], row[2]))

    def addPatient(self, nama, umur, tingkat_urgensi):
        conn = sqlite3.connect('hospital_queue.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO patients (nama, umur, tingkat_urgensi)
            VALUES (?, ?, ?)
        ''', (nama, umur, tingkat_urgensi))
        conn.commit()
        conn.close()
        self.loadFromDB()
        print(f"\n Pasien {nama} ditambahkan ke antrian (Urgensi: {tingkat_urgensi})")

    def getNextPatient(self):
        if not self.queue:
            print("  Antrian kosong!")
            return None
        
        patient = self.queue.pop(0)
        conn = sqlite3.connect('hospital_queue.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE patients 
            SET status = 'Selesai', waktu_dipanggil = ?
            WHERE nama = ? AND status = 'Menunggu'
        ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), patient.nama))
        conn.commit()
        conn.close()
        
        return patient

    def displayQueue(self):
        self.loadFromDB()
        if not self.queue:
            print("  Antrian kosong!")
            return
        
        print(f"\n  {'No':<4} {'Nama':<20} {'Umur':<8} {'Urgensi':<10}")
        print("  " + "-" * 45)
        for i, p in enumerate(self.queue, 1):
            print(f"  {i:<4} {p.nama:<20} {p.umur:<8} {p.tingkat_urgensi:<10}")

    def getHistory(self):
        conn = sqlite3.connect('hospital_queue.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT nama, umur, tingkat_urgensi, status, waktu_masuk, waktu_dipanggil
            FROM patients
            ORDER BY id DESC
        ''')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def clearCompleted(self):
        """Hapus pasien yang sudah selesai"""
        conn = sqlite3.connect('hospital_queue.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM patients WHERE status = 'Selesai'")
        conn.commit()
        conn.close()
        print(" Riwayat pasien selesai telah dibersihkan.")

def menu_header(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def input_patient():
    menu_header("TAMBAH PASIEN BARU")
    
    nama = input("  Nama Pasien: ").strip()
    if not nama:
        print(" Nama tidak boleh kosong!")
        return
    
    try:
        umur = int(input("  Umur: ").strip())
        if umur <= 0:
            print(" Umur harus lebih dari 0!")
            return
    except ValueError:
        print(" Umur harus berupa angka!")
        return
    
    print("\n  Pilih Tingkat Urgensi:")
    print("  [1] Rendah  - Penyakit ringan")
    print("  [2] Sedang  - Perlu perhatian")
    print("  [3] Tinggi  - Darurat ringan")
    print("  [4] Kritis  - Darurat berat")
    print("  [5] Sangat Kritis - Nyawa terancam")
    
    try:
        urgensi = int(input("  Pilihan (1-5): ").strip())
        if urgensi < 1 or urgensi > 5:
            print(" Urgensi harus antara 1-5!")
            return
    except ValueError:
        print(" Urgensi harus berupa angka!")
        return
    
    hospital.addPatient(nama, umur, urgensi)

def call_next_patient():
    menu_header("PANGGIL PASIEN BERIKUTNYA")
    
    hospital.loadFromDB()
    if not hospital.queue:
        print("  Tidak ada pasien dalam antrian.")
        return
    
    print("  Pasien yang akan dipanggil:")
    print(f"  Nama: {hospital.queue[0].nama}")
    print(f"  Umur: {hospital.queue[0].umur}")
    print(f"  Urgensi: {hospital.queue[0].tingkat_urgensi}")
    
    confirm = input("\n  Panggil pasien ini? (y/n): ").strip().lower()
    if confirm == 'y':
        patient = hospital.getNextPatient()
        print(f"\n Pasien {patient.nama} telah dipanggil!")
        print(f"     Urgensi: {patient.tingkat_urgensi} | Umur: {patient.umur}")
    else:
        print(" Pemanggilan dibatalkan.")

def display_queue():
    menu_header("DAFTAR ANTRIAN PASIEN")
    hospital.displayQueue()

def display_history():
    menu_header("RIWAYAT SEMUA PASIEN")
    history = hospital.getHistory()
    
    if not history:
        print("  Belum ada data pasien.")
        return
    
    print(f"  {'Nama':<15} {'Umur':<6} {'Urg':<5} {'Status':<12} {'Waktu Masuk':<20} {'Waktu Dipanggil'}")
    print("  " + "-" * 85)
    for row in history:
        waktu_dipanggil = row[5] if row[5] else "-"
        print(f"  {row[0]:<15} {row[1]:<6} {row[2]:<5} {row[3]:<12} {row[4]:<20} {waktu_dipanggil}")

def clear_history():
    menu_header("BERSIHKAN RIWAYAT")
    confirm = input("  Hapus semua pasien yang sudah selesai? (y/n): ").strip().lower()
    if confirm == 'y':
        hospital.clearCompleted()
    else:
        print(" Dibatalkan.")

def search_patient():
    menu_header("CARI PASIEN")
    nama = input("  Masukkan nama pasien: ").strip()
    
    conn = sqlite3.connect('hospital_queue.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT nama, umur, tingkat_urgensi, status, waktu_masuk, waktu_dipanggil
        FROM patients WHERE nama LIKE ?
    ''', (f'%{nama}%',))
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print(" Pasien tidak ditemukan.")
        return
    
    print(f"\n  {'Nama':<15} {'Umur':<6} {'Urg':<5} {'Status':<12} {'Waktu Masuk':<20}")
    print("  " + "-" * 60)
    for row in rows:
        print(f"  {row[0]:<15} {row[1]:<6} {row[2]:<5} {row[3]:<12} {row[4]:<20}")

def main_menu():
    init_db()
    
    while True:
        print("\n" + "=" * 60)
        print("  HOSPITAL QUEUE SYSTEM - PRIORITY QUEUE")
        print("=" * 60)
        print("  [1] Tambah Pasien Baru")
        print("  [2] Panggil Pasien Berikutnya")
        print("  [3] Lihat Daftar Antrian")
        print("  [4] Lihat Riwayat Semua Pasien")
        print("  [5] Cari Pasien")
        print("  [6] Bersihkan Riwayat Selesai")
        print("  [0] Keluar")
        print("=" * 60)
        
        choice = input("  Pilih menu (0-6): ").strip()
        
        if choice == "1":
            input_patient()
        elif choice == "2":
            call_next_patient()
        elif choice == "3":
            display_queue()
        elif choice == "4":
            display_history()
        elif choice == "5":
            search_patient()
        elif choice == "6":
            clear_history()
        elif choice == "0":
            print("\n  Terima kasih! Program selesai.")
            break
        else:
            print(" Pilihan tidak valid!")

hospital = HospitalQueue()

if __name__ == "__main__":
    main_menu()