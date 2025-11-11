import mysql.connector

class crudPengiriman:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbvisual3_2310010002'
        )

    # ============ SIMPAN ============
    def simpanPengiriman(self, idpeng, idpem, tgkirim, jumkir, kendaraan, sopir, status):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute(
            """
            INSERT INTO pengiriman
            (id_pengiriman, id_pemesanan, tanggal_kirim, jumlah_kirim, kendaraan, sopir, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (idpeng, idpem, tgkirim, jumkir, kendaraan, sopir, status)
        )
        self.koneksi.commit()
        aksiCur.close()

    # ============ EDIT ============
    def editPengiriman(self, idpeng, idpem, tgkirim, jumkir, kendaraan, sopir, status):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute(
            """
            UPDATE pengiriman
            SET id_pemesanan=%s, tanggal_kirim=%s, jumlah_kirim=%s, kendaraan=%s, sopir=%s, status=%s
            WHERE id_pengiriman=%s
            """,
            (idpem, tgkirim, jumkir, kendaraan, sopir, status, idpeng)
        )
        self.koneksi.commit()
        aksiCur.close()

    # ============ HAPUS ============
    def hapusPengiriman(self, idpeng):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("DELETE FROM pengiriman WHERE id_pengiriman=%s", (idpeng,))
        self.koneksi.commit()
        aksiCur.close()

    # ============ TAMPIL ============
    def tampilPengiriman(self):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("SELECT * FROM pengiriman")
        hasil = aksiCur.fetchall()
        aksiCur.close()
        return hasil

    # ============ FILTER PENGIRIMAN (berdasarkan nama perusahaan) ============
    def filterPengiriman(self, cari):
        aksiCur = self.koneksi.cursor()
        query = """
            SELECT pg.*
            FROM pengiriman pg
            JOIN pemesanan p ON pg.id_pemesanan = p.id_pemesanan
            JOIN konsumen k ON p.id_konsumen = k.id_konsumen
            WHERE k.nama_perusahaan LIKE %s
        """
        aksiCur.execute(query, (f"%{cari}%",))
        hasil = aksiCur.fetchall()
        aksiCur.close()
        return hasil
