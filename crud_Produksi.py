import mysql.connector


class crudProduksi:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbvisual3_2310010002'
        )

    # ============ SIMPAN ============
    def simpanProduksi(self, idpro, idpem, tgpro, jumsi, ket):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute(
            "INSERT INTO produksi (id_produksi, id_pemesanan, tanggal_produksi, jumlah_produksi, keterangan) "
            "VALUES (%s, %s, %s, %s, %s)",
            (idpro, idpem, tgpro, jumsi, ket)
        )
        self.koneksi.commit()
        aksiCur.close()

    # ============ EDIT ============
    def editProduksi(self, idpro, idpem, tgpro, jumsi, ket):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute(
            "UPDATE produksi SET id_pemesanan=%s, tanggal_produksi=%s, jumlah_produksi=%s, keterangan=%s "
            "WHERE id_produksi=%s",
            (idpem, tgpro, jumsi, ket, idpro)
        )
        self.koneksi.commit()
        aksiCur.close()

    # ============ HAPUS ============
    def hapusProduksi(self, idpro):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute(
            "DELETE FROM produksi WHERE id_produksi=%s",
            (idpro,)
        )
        self.koneksi.commit()
        aksiCur.close()

    # ============ TAMPIL ============
    def tampilProduksi(self):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("SELECT * FROM produksi")
        hasil = aksiCur.fetchall()
        aksiCur.close()
        return hasil

    # ============ FILTER PRODUKSI ============
    def filterProduksi(self, cari):
        aksiCur = self.koneksi.cursor()
        query = """
            SELECT pr.* FROM produksi pr
            JOIN pemesanan p ON pr.id_pemesanan = p.id_pemesanan
            JOIN konsumen k ON p.id_konsumen = k.id_konsumen
            WHERE k.nama_perusahaan LIKE %s
        """
        aksiCur.execute(query, (f"%{cari}%",))
        hasil = aksiCur.fetchall()
        aksiCur.close()
        return hasil

