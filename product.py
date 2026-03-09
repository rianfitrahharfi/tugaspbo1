class Produk:

    def __init__(self, nama: str, stok: int):
        self.nama = nama
        self.stok = stok

    def beli(self, jumlah: int):
        if jumlah > self.stok:
            return "Stok tidak cukup"
        self.stok -= jumlah
        return "Pembelian berhasil"

    def tambah_stok(self, jumlah: int):
        self.stok += jumlah