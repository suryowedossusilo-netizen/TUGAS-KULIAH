class EmailError(Exception):
    """Exception untuk validasi format email"""
    def __init__(self, email, pesan=""):
        self.email = email
        self.pesan = pesan
        super().__init__(self.pesan)

    def __str__(self):
        return f"EmailError: '{self.email}' - {self.pesan}"


def validasi_email(email):
    """
    Validasi format email:
    - Harus mengandung '@'
    - Harus mengandung '.' setelah '@'
    - Tidak boleh ada spasi
    - Domain minimal 2 karakter setelah '.'
    """
    email = email.strip()

    if "@" not in email:
        raise EmailError(email, "Email harus mengandung '@'")

    if " " in email:
        raise EmailError(email, "Email tidak boleh mengandung spasi")

    parts = email.split("@")
    if len(parts) != 2:
        raise EmailError(email, "Email hanya boleh memiliki satu '@'")

    username, domain = parts

    if len(username) == 0:
        raise EmailError(email, "Bagian sebelum '@' tidak boleh kosong")

    if "." not in domain:
        raise EmailError(email, "Domain harus mengandung '.' (contoh: gmail.com)")

    domain_parts = domain.split(".")
    if len(domain_parts[-1]) < 2:
        raise EmailError(email, "Ekstensi domain minimal 2 karakter (contoh: .com, .id)")

    return True

print("\n" + "=" * 60)
print("TUGAS 3 - CONTOH 2: EmailError")
print("=" * 60)

daftar_email = [
    "andi@gmail.com",
    "andi.gmail.com",
    "andi@gmail",
    "@gmail.com",
    "andi @gmail.com",
    "andi@gmail.c",
    "andi@@gmail.com"
]

for email in daftar_email:
    print(f"\n>>> Validasi: '{email}'")
    try:
        validasi_email(email)
        print(f"Email valid!")
    except EmailError as e:
        print(f"{e}")