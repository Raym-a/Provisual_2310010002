import mysql.connector

class crudPemesanan:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbvisual3_2310010002'
        )

    # ============ SIMPAN ============
    def simpanPemesanan(self, idpem, idkon, produk, tgl, talhar, sts):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute(
            "INSERT INTO pemesanan (id_pemesanan, id_konsumen, produk_dipesan, tanggal_pemesanan, total_harga, status) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (idpem, idkon, produk, tgl, talhar, sts)
        )
        self.koneksi.commit()
        aksiCur.close()

    # ============ EDIT ============
    def editPemesanan(self, idpem, idkon, produk, tgl, talhar, sts):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute(
            "UPDATE pemesanan SET id_konsumen=%s, produk_dipesan=%s, tanggal_pemesanan=%s, total_harga=%s, status=%s "
            "WHERE id_pemesanan=%s",
            (idkon, produk, tgl, talhar, sts, idpem)
        )
        self.koneksi.commit()
        aksiCur.close()

    # ============ HAPUS ============
    def hapusPemesanan(self, idpem):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute(
            "DELETE FROM pemesanan WHERE id_pemesanan=%s",
            (idpem,)
        )
        self.koneksi.commit()
        aksiCur.close()

    # ============ TAMPIL ============
    def tampilPemesanan(self):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("SELECT * FROM pemesanan")
        hasil = aksiCur.fetchall()
        aksiCur.close()
        return hasil

    ## Untuk Mencari Seluruh nama_perusahaan Pada Table Pemesanan
    # ============ FILTER PEMESANAN ============
    def filterKonsumen(self, cari):
        aksiCur = self.koneksi.cursor()
        query = """
            SELECT p.* FROM pemesanan p
            JOIN konsumen k ON p.id_konsumen = k.id_konsumen
            WHERE k.nama_perusahaan LIKE %s
        """
        aksiCur.execute(query, (f"%{cari}%",))
        hasil = aksiCur.fetchall()
        aksiCur.close()
        return hasil

