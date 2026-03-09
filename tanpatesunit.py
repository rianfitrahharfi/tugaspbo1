class Produk:
    def __init__(self, nama, stok):
        self.nama = nama
        self.stok = stok

    def beli(self, jumlah):
        self.stok -= jumlah   # tidak ada pengecekan stok

p = Produk("Smartphone", 5)

p.beli(10)   # membeli lebih dari stok
print("Sisa stok:", p.stok)