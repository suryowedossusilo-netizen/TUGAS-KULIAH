import sqlite3
from datetime import date

def init_db():
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_member INTEGER DEFAULT 0,
            member_type TEXT DEFAULT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            visit_date TEXT,
            service_expense REAL DEFAULT 0,
            product_expense REAL DEFAULT 0,
            service_discount REAL DEFAULT 0,
            product_discount REAL DEFAULT 0,
            total_expense REAL DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database berhasil diinisialisasi!")

class Customer:
    def __init__(self, name, is_member=False, member_type=None):
        self._name = name
        self._member = is_member
        self._memberType = member_type

    def getName(self):
        return self._name

    def isMember(self):
        return self._member

    def getMemberType(self):
        return self._memberType

    def toString(self):
        status = f"Member ({self._memberType})" if self._member else "Non-Member"
        return f"Customer: {self._name}, Status: {status}"


class DiscountRate:
    _serviceDiscountPremium = 0.20
    _serviceDiscountGold = 0.15
    _serviceDiscountSilver = 0.10
    _productDiscountPremium = 0.10
    _productDiscountGold = 0.10
    _productDiscountSilver = 0.10

    @staticmethod
    def getServiceDiscountRate(type):
        if type == "Premium":
            return DiscountRate._serviceDiscountPremium
        elif type == "Gold":
            return DiscountRate._serviceDiscountGold
        elif type == "Silver":
            return DiscountRate._serviceDiscountSilver
        else:
            return 0.0

    @staticmethod
    def getProductDiscountRate(type):
        if type == "Premium":
            return DiscountRate._productDiscountPremium
        elif type == "Gold":
            return DiscountRate._productDiscountGold
        elif type == "Silver":
            return DiscountRate._productDiscountSilver
        else:
            return 0.0


class Visit:
    def __init__(self, customer_name, visit_date, is_member=False, member_type=None):
        self._customer = Customer(customer_name, is_member, member_type)
        self._date = visit_date
        self._serviceExpense = 0.0
        self._productExpense = 0.0

    def setServiceExpense(self, ex):
        self._serviceExpense = ex

    def setProductExpense(self, ex):
        self._productExpense = ex

    def getTotalExpense(self):
        serviceDiscount = 0.0
        productDiscount = 0.0
        if self._customer.isMember():
            memberType = self._customer.getMemberType()
            serviceDiscount = DiscountRate.getServiceDiscountRate(memberType)
            productDiscount = DiscountRate.getProductDiscountRate(memberType)
        serviceTotal = self._serviceExpense * (1 - serviceDiscount)
        productTotal = self._productExpense * (1 - productDiscount)
        return serviceTotal, productTotal, serviceTotal + productTotal, serviceDiscount, productDiscount

    def toString(self):
        serviceTotal, productTotal, total, serviceDiscount, productDiscount = self.getTotalExpense()
        result = f"\n{'='*50}\n"
        result += f"  STRUK KUNJUNGAN BEAUTY SALON\n"
        result += f"{'='*50}\n"
        result += f"  Tanggal: {self._date}\n"
        result += f"  {self._customer.toString()}\n"
        result += f"{'-'*50}\n"
        result += f"  Biaya Layanan : Rp{self._serviceExpense:,.0f}\n"
        result += f"  Diskon Layanan: {serviceDiscount*100:.0f}%\n"
        result += f"  Total Layanan : Rp{serviceTotal:,.0f}\n"
        result += f"{'-'*50}\n"
        result += f"  Biaya Produk  : Rp{self._productExpense:,.0f}\n"
        result += f"  Diskon Produk : {productDiscount*100:.0f}%\n"
        result += f"  Total Produk  : Rp{productTotal:,.0f}\n"
        result += f"{'='*50}\n"
        result += f"  TOTAL BAYAR   : Rp{total:,.0f}\n"
        result += f"{'='*50}\n"
        return result

def add_customer(name, is_member, member_type):
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO customers (name, is_member, member_type)
        VALUES (?, ?, ?)
    ''', (name, 1 if is_member else 0, member_type))
    customer_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return customer_id

def get_all_customers():
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers ORDER BY id DESC')
    customers = cursor.fetchall()
    conn.close()
    return customers

def get_customer_by_id(customer_id):
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
    customer = cursor.fetchone()
    conn.close()
    return customer

def add_visit(customer_id, visit_date, service_expense, product_expense, service_discount, product_discount, total_expense):
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO visits (customer_id, visit_date, service_expense, product_expense, 
                           service_discount, product_discount, total_expense)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (customer_id, visit_date, service_expense, product_expense, 
          service_discount, product_discount, total_expense))
    visit_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return visit_id

def get_all_visits():
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT v.id, c.name, v.visit_date, v.service_expense, v.product_expense, 
               v.service_discount, v.product_discount, v.total_expense
        FROM visits v
        JOIN customers c ON v.customer_id = c.id
        ORDER BY v.id DESC
    ''')
    visits = cursor.fetchall()
    conn.close()
    return visits

def get_visits_by_customer(customer_id):
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT v.id, c.name, v.visit_date, v.service_expense, v.product_expense, 
               v.service_discount, v.product_discount, v.total_expense
        FROM visits v
        JOIN customers c ON v.customer_id = c.id
        WHERE v.customer_id = ?
        ORDER BY v.id DESC
    ''', (customer_id,))
    visits = cursor.fetchall()
    conn.close()
    return visits

def update_customer(customer_id, name, is_member, member_type):
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE customers 
        SET name = ?, is_member = ?, member_type = ?
        WHERE id = ?
    ''', (name, 1 if is_member else 0, member_type, customer_id))
    conn.commit()
    conn.close()

def delete_customer(customer_id):
    conn = sqlite3.connect('beauty_salon.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM visits WHERE customer_id = ?', (customer_id,))
    cursor.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()

def menu_header(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def input_customer():
    menu_header("INPUT DATA CUSTOMER BARU")
    
    name = input("  Nama Customer: ").strip()
    if not name:
        print(" Nama tidak boleh kosong!")
        return
    
    print("\n  Pilih Status Member:")
    print("  [1] Non-Member")
    print("  [2] Member Premium")
    print("  [3] Member Gold")
    print("  [4] Member Silver")
    
    choice = input("  Pilihan (1-4): ").strip()
    
    is_member = False
    member_type = None
    
    if choice == "2":
        is_member = True
        member_type = "Premium"
    elif choice == "3":
        is_member = True
        member_type = "Gold"
    elif choice == "4":
        is_member = True
        member_type = "Silver"
    elif choice != "1":
        print("  Pilihan tidak valid! Default: Non-Member")
    
    customer_id = add_customer(name, is_member, member_type)
    status = f"Member ({member_type})" if is_member else "Non-Member"
    print(f"\n  Customer berhasil ditambahkan!")
    print(f"  ID: {customer_id}")
    print(f"  Nama: {name}")
    print(f"  Status: {status}")


def list_customers():
    menu_header("DAFTAR SEMUA CUSTOMER")
    customers = get_all_customers()
    
    if not customers:
        print("  Belum ada data customer.")
        return
    
    print(f"  {'ID':<5} {'Nama':<20} {'Status':<20} {'Tanggal Daftar'}")
    print("  " + "-" * 55)
    for c in customers:
        status = f"Member ({c[3]})" if c[2] else "Non-Member"
        print(f"  {c[0]:<5} {c[1]:<20} {status:<20} {c[4]}")


def input_visit():
    menu_header("INPUT TRANSAKSI KUNJUNGAN")
    
    list_customers()
    
    try:
        customer_id = int(input("\n  Masukkan ID Customer: ").strip())
    except ValueError:
        print(" ID harus berupa angka!")
        return
    
    customer = get_customer_by_id(customer_id)
    if not customer:
        print(" Customer tidak ditemukan!")
        return
    
    print(f"\n  Customer: {customer[1]}")
    status = f"Member ({customer[3]})" if customer[2] else "Non-Member"
    print(f"  Status: {status}")
    
    try:
        service = float(input("  Biaya Layanan (Rp): ").strip())
        product = float(input("  Biaya Produk (Rp): ").strip())
    except ValueError:
        print(" Biaya harus berupa angka!")
        return
    
    visit_date = date.today().strftime("%Y-%m-%d")
    
    visit = Visit(customer[1], visit_date, customer[2], customer[3])
    visit.setServiceExpense(service)
    visit.setProductExpense(product)
    
    serviceTotal, productTotal, total, serviceDiscount, productDiscount = visit.getTotalExpense()
    
    print(visit.toString())
    
    confirm = input("  Simpan transaksi? (y/n): ").strip().lower()
    if confirm == 'y':
        add_visit(customer_id, visit_date, service, product, 
                  serviceDiscount, productDiscount, total)
        print(" Transaksi berhasil disimpan!")
    else:
        print(" Transaksi dibatalkan.")


def list_visits():
    menu_header("RIWAYAT SEMUA TRANSAKSI")
    visits = get_all_visits()
    
    if not visits:
        print("  Belum ada data transaksi.")
        return
    
    print(f"  {'ID':<5} {'Nama':<15} {'Tanggal':<12} {'Layanan':<12} {'Produk':<12} {'Total':<15}")
    print("  " + "-" * 75)
    for v in visits:
        print(f"  {v[0]:<5} {v[1]:<15} {v[2]:<12} Rp{v[3]:>10,.0f} Rp{v[4]:>10,.0f} Rp{v[7]:>12,.0f}")


def edit_customer():
    menu_header("EDIT DATA CUSTOMER")
    list_customers()
    
    try:
        customer_id = int(input("\n  Masukkan ID Customer yang akan diedit: ").strip())
    except ValueError:
        print(" ID harus berupa angka!")
        return
    
    customer = get_customer_by_id(customer_id)
    if not customer:
        print(" Customer tidak ditemukan!")
        return
    
    print(f"\n  Data saat ini: {customer[1]} - {'Member' if customer[2] else 'Non-Member'} ({customer[3] or '-'})")
    
    name = input("  Nama baru (kosongkan jika tidak diubah): ").strip()
    if not name:
        name = customer[1]
    
    print("\n  Pilih Status Member Baru:")
    print("  [1] Non-Member")
    print("  [2] Member Premium")
    print("  [3] Member Gold")
    print("  [4] Member Silver")
    print("  [0] Biarkan seperti semula")
    
    choice = input("  Pilihan (0-4): ").strip()
    
    if choice == "0" or choice == "":
        is_member = customer[2]
        member_type = customer[3]
    elif choice == "1":
        is_member = False
        member_type = None
    elif choice == "2":
        is_member = True
        member_type = "Premium"
    elif choice == "3":
        is_member = True
        member_type = "Gold"
    elif choice == "4":
        is_member = True
        member_type = "Silver"
    else:
        is_member = customer[2]
        member_type = customer[3]
    
    update_customer(customer_id, name, is_member, member_type)
    print(f" Data customer berhasil diupdate!")


def delete_customer_menu():
    menu_header("HAPUS DATA CUSTOMER")
    list_customers()
    
    try:
        customer_id = int(input("\n  Masukkan ID Customer yang akan dihapus: ").strip())
    except ValueError:
        print("ID harus berupa angka!")
        return
    
    customer = get_customer_by_id(customer_id)
    if not customer:
        print("Customer tidak ditemukan!")
        return
    
    confirm = input(f"  Yakin hapus {customer[1]}? Semua transaksi ikut terhapus! (y/n): ").strip().lower()
    if confirm == 'y':
        delete_customer(customer_id)
        print("Customer berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")


def customer_history():
    menu_header("RIWAYAT TRANSAKSI CUSTOMER")
    list_customers()
    
    try:
        customer_id = int(input("\n  Masukkan ID Customer: ").strip())
    except ValueError:
        print("ID harus berupa angka!")
        return
    
    customer = get_customer_by_id(customer_id)
    if not customer:
        print("Customer tidak ditemukan!")
        return
    
    visits = get_visits_by_customer(customer_id)
    
    print(f"\n  Riwayat Transaksi: {customer[1]}")
    if not visits:
        print("  Belum ada transaksi.")
        return
    
    total_semua = 0
    print(f"  {'ID':<5} {'Tanggal':<12} {'Layanan':<12} {'Produk':<12} {'Total':<15}")
    print("  " + "-" * 60)
    for v in visits:
        print(f"  {v[0]:<5} {v[2]:<12} Rp{v[3]:>10,.0f} Rp{v[4]:>10,.0f} Rp{v[7]:>12,.0f}")
        total_semua += v[7]
    
    print("  " + "-" * 60)
    print(f"  TOTAL KESELURUHAN: Rp{total_semua:,.0f}")

def main_menu():
    init_db()
    
    while True:
        print("\n" + "=" * 60)
        print("  BEAUTY SALON DISCOUNT SYSTEM - DATABASE")
        print("=" * 60)
        print("  [1] Input Customer Baru")
        print("  [2] Lihat Daftar Customer")
        print("  [3] Input Transaksi Kunjungan")
        print("  [4] Lihat Semua Transaksi")
        print("  [5] Edit Data Customer")
        print("  [6] Hapus Data Customer")
        print("  [7] Riwayat Transaksi per Customer")
        print("  [0] Keluar")
        print("=" * 60)
        
        choice = input("  Pilih menu (0-7): ").strip()
        
        if choice == "1":
            input_customer()
        elif choice == "2":
            list_customers()
        elif choice == "3":
            input_visit()
        elif choice == "4":
            list_visits()
        elif choice == "5":
            edit_customer()
        elif choice == "6":
            delete_customer_menu()
        elif choice == "7":
            customer_history()
        elif choice == "0":
            print("\n  Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main_menu()