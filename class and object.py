import unittest

class Produk:
    def __init__(self, nama, stok):
        self.nama = nama
        self.stok = stok

    def beli(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
        else:
            raise ValueError("Stok tidak cukup")


class TestProduk(unittest.TestCase):

    def setUp(self):
        self.p = Produk("Smartphone", 5)

    def test_beli_berhasil(self):
        self.p.beli(2)
        self.assertEqual(self.p.stok, 3)

    def test_beli_gagal(self):
        with self.assertRaises(ValueError):
            self.p.beli(10)


if __name__ == "__main__":
    unittest.main()