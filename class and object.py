# ============================
# FILE: book_testable.py
# ============================

import unittest

# ============================
# 1. CLASS BOOK (Logika Bisnis)
# ============================
class Book:
    def __init__(self, judul, penulis, harga):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga
        self.terpinjam = False
        self.pemilik = None

    def pinjam(self, nama):
        """Pinjam buku. Return True jika berhasil."""
        if self.terpinjam:
            return False
        self.terpinjam = True
        self.pemilik = nama
        return True

    def kembalikan(self):
        """Kembalikan buku. Return True jika berhasil."""
        if not self.terpinjam:
            return False
        self.terpinjam = False
        self.pemilik = None
        return True

    def hitung_harga_pajak(self, pajak):
        """Hitung harga dengan pajak. Return float."""
        if pajak < 0:
            raise ValueError("Pajak tidak boleh negatif")
        return self.harga * (1 + pajak)


# ============================
# 2. UNIT TESTS (Pengecekan)
# ============================
class TestBook(unittest.TestCase):

    def setUp(self):
        # Siapkan buku baru sebelum setiap test
        self.buku = Book("Laskar Pelangi", "Andrea", 50000)

    def test_buku_baru(self):
        # Test: Buku baru harus tersedia
        self.assertFalse(self.buku.terpinjam)
        self.assertIsNone(self.buku.pemilik)

    def test_pinjam_berhasil(self):
        # Test: Pinjam buku yang tersedia
        hasil = self.buku.pinjam("Budi")
        self.assertTrue(hasil)
        self.assertTrue(self.buku.terpinjam)
        self.assertEqual(self.buku.pemilik, "Budi")

    def test_pinjam_gagal(self):
        # Test: Pinjam buku yang sudah dipinjam
        self.buku.pinjam("Budi")
        hasil = self.buku.pinjam("Siti")
        self.assertFalse(hasil)

    def test_kembalikan_berhasil(self):
        # Test: Kembalikan buku yang dipinjam
        self.buku.pinjam("Budi")
        hasil = self.buku.kembalikan()
        self.assertTrue(hasil)
        self.assertFalse(self.buku.terpinjam)

    def test_harga_pajak(self):
        # Test: Hitung harga dengan pajak 10%
        harga = self.buku.hitung_harga_pajak(0.1)
        self.assertEqual(harga, 55000)

    def test_pajak_negatif_error(self):
        # Test: Pajak negatif harus error
        with self.assertRaises(ValueError):
            self.buku.hitung_harga_pajak(-0.1)


# ============================
# 3. JALANKAN TEST
# ============================
if __name__ == '__main__':
    unittest.main()