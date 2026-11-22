# ==========================================
# SISTEM DATA MAHASISWA
# UNIVERSITAS BINA BANGSA
# ==========================================


# CLASS MAHASISWA
class Mahasiswa:

    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.__nilai = 0
        self.nilai = nilai

    # PROPERTY
    @property
    def nilai(self):
        return self.__nilai

    # SETTER
    @nilai.setter
    def nilai(self, angka):
        if 0 <= angka <= 100:
            self.__nilai = angka
        else:
            raise ValueError("Nilai harus 0 sampai 100!")

    # METHOD STATUS KELULUSAN
    def status_lulus(self):
        if self.nilai >= 60:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    # METHOD MENAMPILKAN DATA
    def tampilkan_data(self):
        print("NIM       :", self.nim)
        print("Nama      :", self.nama)
        print("Jurusan   :", self.jurusan)
        print("Nilai     :", self.nilai)
        print("Status    :", self.status_lulus())


# CLASS SISTEM DATA MAHASISWA
class SistemDataMahasiswa:

    nama_kampus = "UNIVERSITAS BINA BANGSA"

    def __init__(self):

        # 15 DATA MAHASISWA AWAL
        self.__daftar_mahasiswa = [

            Mahasiswa("Andi Saputra", "26031001", "Ilmu Komputer", 85),
            Mahasiswa("Siti Nurhaliza", "26031002", "Ilmu Komputer", 90),
            Mahasiswa("Rizky Pratama", "26031003", "Ilmu Komputer", 75),
            Mahasiswa("Dinda Maharani", "26031004", "Ilmu Komputer", 95),
            Mahasiswa("Fajar Ramadhan", "26031005", "Ilmu Komputer", 55),

            Mahasiswa("Nadia Putri", "26031006", "Ilmu Komputer", 88),
            Mahasiswa("Budi Santoso", "26031007", "Ilmu Komputer", 70),
            Mahasiswa("Aulia Rahma", "26031008", "Ilmu Komputer", 92),
            Mahasiswa("Rian Firmansyah", "26031009", "Ilmu Komputer", 65),
            Mahasiswa("Citra Lestari", "26031010", "Ilmu Komputer", 80),

            Mahasiswa("Dimas Prakoso", "26031011", "Ilmu Komputer", 58),
            Mahasiswa("Putri Amelia", "26031012", "Ilmu Komputer", 89),
            Mahasiswa("Agus Setiawan", "26031013", "Ilmu Komputer", 77),
            Mahasiswa("Maya Sari", "26031014", "Ilmu Komputer", 96),
            Mahasiswa("Rafi Akbar", "26031015", "Ilmu Komputer", 50),

        ]

    # PROPERTY
    @property
    def daftar_mahasiswa(self):
        return self.__daftar_mahasiswa.copy()

    # CLASS METHOD
    @classmethod
    def buat_sistem(cls):
        return cls()

    # STATIC METHOD
    @staticmethod
    def validasi_nim(nim):
        return nim.strip() != ""

    # METHOD MENAMBAH MAHASISWA
    def tambah_mahasiswa(self):

        print("\n=== TAMBAH DATA MAHASISWA ===")

        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        jurusan = input("Masukkan Jurusan: ")

        if not self.validasi_nim(nim):
            print("NIM tidak boleh kosong!")
            return

        for mhs in self.__daftar_mahasiswa:
            if mhs.nim == nim:
                print("NIM sudah terdaftar!")
                return

        try:
            nilai = float(input("Masukkan Nilai: "))

            mahasiswa = Mahasiswa(
                nama, nim, jurusan, nilai
            )

            self.__daftar_mahasiswa.append(mahasiswa)

            print("\nData mahasiswa berhasil ditambahkan!")

        except ValueError:
            print("Nilai harus berupa angka 0 sampai 100!")

    # METHOD MENAMPILKAN SEMUA DATA
    def tampilkan_semua(self):

        print("\n========================================")
        print("     DATA MAHASISWA UNIVERSITAS BINA BANGSA")
        print("========================================")

        if not self.__daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return

        for nomor, mhs in enumerate(
            self.__daftar_mahasiswa, start=1
        ):

            print(f"\nMahasiswa ke-{nomor}")
            print("----------------------------------------")

            mhs.tampilkan_data()

        print("\nTotal Mahasiswa:", len(self.__daftar_mahasiswa))

    # METHOD MENCARI MAHASISWA
    def cari_mahasiswa(self):

        print("\n=== CARI DATA MAHASISWA ===")

        nim = input("Masukkan NIM: ")

        for mhs in self.__daftar_mahasiswa:

            if mhs.nim == nim:

                print("\nData mahasiswa ditemukan!")
                print("----------------------------------------")

                mhs.tampilkan_data()
                return

        print("Data mahasiswa tidak ditemukan!")

    # METHOD MENGHAPUS MAHASISWA
    def hapus_mahasiswa(self):

        print("\n=== HAPUS DATA MAHASISWA ===")

        nim = input("Masukkan NIM yang akan dihapus: ")

        for mhs in self.__daftar_mahasiswa:

            if mhs.nim == nim:

                self.__daftar_mahasiswa.remove(mhs)

                print("Data mahasiswa berhasil dihapus!")
                return

        print("Data mahasiswa tidak ditemukan!")


    # METHOD MENU UTAMA
    def jalankan(self):

        while True:

            print("\n========================================")
            print("     UNIVERSITAS BINA BANGSA")
            print("       SISTEM DATA MAHASISWA")
            print("========================================")

            print("1. Tambah Data Mahasiswa")
            print("2. Tampilkan Semua Mahasiswa")
            print("3. Cari Data Mahasiswa")
            print("4. Hapus Data Mahasiswa")
            print("5. Keluar")

            print("========================================")

            pilihan = input("Pilih Menu (1-5): ")

            if pilihan == "1":

                self.tambah_mahasiswa()

            elif pilihan == "2":

                self.tampilkan_semua()

            elif pilihan == "3":

                self.cari_mahasiswa()

            elif pilihan == "4":

                self.hapus_mahasiswa()

            elif pilihan == "5":

                print("\nTerima kasih telah menggunakan program!")
                print("Universitas Bina Bangsa")
                break

            else:

                print("Pilihan tidak tersedia!")


# MEMBUAT OBJECT
if __name__ == "__main__":

    sistem = SistemDataMahasiswa.buat_sistem()

    sistem.jalankan()