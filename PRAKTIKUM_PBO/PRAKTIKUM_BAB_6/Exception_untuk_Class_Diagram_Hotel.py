class InvalidHotelDataError(Exception):
    """Exception custom untuk validasi data hotel"""
    pass


class Hotel:
    def __init__(self, address="", numberOfRooms=0, minFloor=0, maxFloor=0):
        self._address = address
        self._numberOfRooms = numberOfRooms
        self._minFloor = minFloor
        self._maxFloor = maxFloor

    def setNumberOfRooms(self, value):
        if value <= 0:
            raise InvalidHotelDataError(f"Jumlah kamar tidak boleh <= 0! (Input: {value})")
        self._numberOfRooms = value

    def setMinFloor(self, value):
        if value < 0:
            raise InvalidHotelDataError(f"Lantai minimum tidak boleh < 0! (Input: {value})")
        self._minFloor = value

    def setMaxFloor(self, value):
        if value > 30:
            raise InvalidHotelDataError(f"Lantai maksimum tidak boleh > 30! (Input: {value})")
        self._maxFloor = value

    def getAddress(self):
        return self._address

    def getNumberOfRooms(self):
        return self._numberOfRooms

    def getMinFloor(self):
        return self._minFloor

    def getMaxFloor(self):
        return self._maxFloor

    def __str__(self):
        return (f"  Alamat Hotel   : {self._address}\n"
                f"  Jumlah Kamar   : {self._numberOfRooms}\n"
                f"  Lantai Minimum : {self._minFloor}\n"
                f"  Lantai Maksimum: {self._maxFloor}")

def menu_header(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def input_hotel_data():
    menu_header("INPUT DATA HOTEL BARU")
    
    hotel = Hotel()
    address = input("  Alamat Hotel: ").strip()
    hotel._address = address

    while True:
        try:
            rooms_input = input("  Jumlah Kamar: ").strip()
            rooms = int(rooms_input)
            hotel.setNumberOfRooms(rooms)
            print(f" umlah kamar {rooms} valid!")
            break
        except ValueError:
            print(" input harus berupa angka! Coba lagi.")
        except InvalidHotelDataError as e:
            print(f" {e}")
 
    while True:
        try:
            min_input = input("  Lantai Minimum: ").strip()
            min_floor = int(min_input)
            hotel.setMinFloor(min_floor)
            print(f"Lantai minimum {min_floor} valid!")
            break
        except ValueError:
            print(" input harus berupa angka! Coba lagi.")
        except InvalidHotelDataError as e:
            print(f" {e}")

    while True:
        try:
            max_input = input("  Lantai Maksimum: ").strip()
            max_floor = int(max_input)
            hotel.setMaxFloor(max_floor)
            print(f" Lantai maksimum {max_floor} valid!")
            break
        except ValueError:
            print(" input harus berupa angka! Coba lagi.")
        except InvalidHotelDataError as e:
            print(f" {e}")
    
    print(f"\n Data Hotel berhasil disimpan!")
    print(f"\n{hotel}")
    return hotel


def test_setter_individu():
    menu_header("TEST SETTER INDIVIDU")
    
    hotel = Hotel()
    hotel._address = "Jl. Sudirman No. 1"
    
    print("\n  Pilih setter yang ingin diuji:")
    print("  [1] setNumberOfRooms")
    print("  [2] setMinFloor")
    print("  [3] setMaxFloor")
    
    choice = input("  Pilihan (1-3): ").strip()
    
    if choice == "1":
        print("\n  Uji setNumberOfRooms:")
        print("  Syarat: nilai harus > 0")
        while True:
            try:
                val = int(input("  Masukkan jumlah kamar: ").strip())
                hotel.setNumberOfRooms(val)
                print(f"Berhasil! Jumlah kamar = {val}")
                break
            except ValueError:
                print(" Harus angka!")
            except InvalidHotelDataError as e:
                print(f"{e}")
    
    elif choice == "2":
        print("\n  Uji setMinFloor:")
        print("  Syarat: nilai harus >= 0")
        while True:
            try:
                val = int(input("  Masukkan lantai minimum: ").strip())
                hotel.setMinFloor(val)
                print(f"Berhasil! Lantai minimum = {val}")
                break
            except ValueError:
                print("Harus angka!")
            except InvalidHotelDataError as e:
                print(f"{e}")
    
    elif choice == "3":
        print("\n  Uji setMaxFloor:")
        print("  Syarat: nilai harus <= 30")
        while True:
            try:
                val = int(input("  Masukkan lantai maksimum: ").strip())
                hotel.setMaxFloor(val)
                print(f"Berhasil! Lantai maksimum = {val}")
                break
            except ValueError:
                print("Harus angka!")
            except InvalidHotelDataError as e:
                print(f"{e}")
    else:
        print("Pilihan tidak valid!")


def demo_exception():
    menu_header("DEMO EXCEPTION")
    
    hotel = Hotel("Jl. Merdeka No. 10")
    
    print("\n  Demo 1: numberOfRooms = -5 (harus error)")
    try:
        hotel.setNumberOfRooms(-5)
    except InvalidHotelDataError as e:
        print(f"Exception tertangkap: {e}")
    
    print("\n  Demo 2: minFloor = -1 (harus error)")
    try:
        hotel.setMinFloor(-1)
    except InvalidHotelDataError as e:
        print(f"Exception tertangkap: {e}")
    
    print("\n  Demo 3: maxFloor = 35 (harus error)")
    try:
        hotel.setMaxFloor(35)
    except InvalidHotelDataError as e:
        print(f"Exception tertangkap: {e}")
    
    print("\n  Demo 4: Semua data valid")
    try:
        hotel.setNumberOfRooms(100)
        hotel.setMinFloor(1)
        hotel.setMaxFloor(15)
        print(f"Semua data valid!")
        print(f"\n{hotel}")
    except InvalidHotelDataError as e:
        print(f"Exception: {e}")


def main_menu():
    while True:
        print("\n" + "=" * 60)
        print("  TUGAS 1: HOTEL EXCEPTION HANDLING")
        print("=" * 60)
        print("  [1] Input Data Hotel Baru")
        print("  [2] Test Setter Individu")
        print("  [3] Demo Exception (Contoh Error)")
        print("  [0] Keluar")
        print("=" * 60)
        
        choice = input("  Pilih menu (0-3): ").strip()
        
        if choice == "1":
            input_hotel_data()
        elif choice == "2":
            test_setter_individu()
        elif choice == "3":
            demo_exception()
        elif choice == "0":
            print("\n  Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main_menu()