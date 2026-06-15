class Person:
    def __init__(self, nama: str, umur: int):
        self.nama = nama
        self.umur = umur

    def __str__(self) -> str:
        return f"Person[nama={self.nama}, umur={self.umur}]"


class Employee(Person):
    def __init__(self, nama: str, umur: int, id_karyawan: str, gaji_dasar: float):
        super().__init__(nama, umur)
        self.id_karyawan = id_karyawan
        self.gaji_dasar = gaji_dasar

    def __str__(self) -> str:
        return (f"Employee[{super().__str__()}, "
                f"id_karyawan={self.id_karyawan}, gaji_dasar={self.gaji_dasar:,.0f}]")


class Manager(Employee):
    def __init__(self, nama: str, umur: int, id_karyawan: str, gaji_dasar: float, tunjangan: float, departemen: str):
        super().__init__(nama, umur, id_karyawan, gaji_dasar)
        self.tunjangan = tunjangan
        self.departemen = departemen

    def total_salary(self) -> float:
        return self.gaji_dasar + self.tunjangan

    def __str__(self) -> str:
        return (f"Manager[{super().__str__()}, "
                f"tunjangan={self.tunjangan:,.0f}, departemen={self.departemen}]")


class Engineer(Employee):
    def __init__(self, nama: str, umur: int, id_karyawan: str, gaji_dasar: float, bidang_kerja: str):
        super().__init__(nama, umur, id_karyawan, gaji_dasar)
        self.bidang_kerja = bidang_kerja

    def total_salary(self) -> float:
        return self.gaji_dasar

    def __str__(self) -> str:
        return (f"Engineer[{super().__str__()}, "
                f"bidang_kerja={self.bidang_kerja}]")


class SoftwareEngineer(Engineer):
    def __init__(self, nama: str, umur: int, id_karyawan: str, gaji_dasar: float, bidang_kerja: str, level: str):
        super().__init__(nama, umur, id_karyawan, gaji_dasar, bidang_kerja)
        self.level = level

    def total_salary(self) -> float:
        if self.level == "junior":
            return self.gaji_dasar
        elif self.level == "middle":
            return self.gaji_dasar + 2_500_000
        elif self.level == "senior":
            return self.gaji_dasar + 5_000_000
        else:
            return self.gaji_dasar

    def __str__(self) -> str:
        return (f"SoftwareEngineer[{super().__str__()}, "
                f"level={self.level}]")


if __name__ == "__main__":
    print("=" * 60)
    print("TUGAS 3: STRUKTUR KARYAWAN")
    print("=" * 60)

    manager = Manager(
        nama="Budi Santoso",
        umur=45,
        id_karyawan="MGR001",
        gaji_dasar=8_000_000,
        tunjangan=3_000_000,
        departemen="IT"
    )

    software_engineer = SoftwareEngineer(
        nama="Andi Wijaya",
        umur=30,
        id_karyawan="SWE001",
        gaji_dasar=9_000_000,
        bidang_kerja="Backend Development",
        level="senior"
    )

    print("\n--- MANAGER ---")
    print(f"Nama          : {manager.nama}")
    print(f"Umur          : {manager.umur}")
    print(f"ID Karyawan   : {manager.id_karyawan}")
    print(f"Gaji Dasar    : Rp {manager.gaji_dasar:,.0f}")
    print(f"Tunjangan     : Rp {manager.tunjangan:,.0f}")
    print(f"Departemen    : {manager.departemen}")
    print(f"Total Gaji    : Rp {manager.total_salary():,.0f}")
    print(f"String Repr   : {manager}")

    print("\n--- SOFTWARE ENGINEER ---")
    print(f"Nama          : {software_engineer.nama}")
    print(f"Umur          : {software_engineer.umur}")
    print(f"ID Karyawan   : {software_engineer.id_karyawan}")
    print(f"Gaji Dasar    : Rp {software_engineer.gaji_dasar:,.0f}")
    print(f"Bidang Kerja  : {software_engineer.bidang_kerja}")
    print(f"Level         : {software_engineer.level}")
    print(f"Total Gaji    : Rp {software_engineer.total_salary():,.0f}")
    print(f"String Repr   : {software_engineer}")