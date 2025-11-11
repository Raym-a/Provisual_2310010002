import mysql.connector


class crudKonsumen:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbvisual3_2310010002'
        )

    # ============ SIMPAN ============
    def simpanKonsumen(self,id,nm,almt,kntk):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("insert into konsumen (id_konsumen,nama_perusahaan,alamat,kontak) value (%s,%s,%s,%s)",
        (id,nm,almt,kntk))
        self.koneksi.commit()
        aksiCur.close()

    # ============ EDIT ============
    def editKonsumen(self,id,nm,almt,kntk):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("update konsumen set nama_perusahaan=%s, alamat=%s, kontak=%s WHERE id_konsumen=%s",
       (nm,almt,kntk,id))
        self.koneksi.commit()
        aksiCur.close()

    # ============ HAPUS ============
    def hapusKonsumen(self, id):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("DELETE FROM konsumen WHERE id_konsumen=%s", (id,))
        self.koneksi.commit()
        aksiCur.close()


    ## Untuk Menampilkan Seluruh Database Pada Table Konsumen
    def tampilKonsumen(self):
        aksiCur = self.koneksi.cursor()
        aksiCur.execute("SELECT * FROM konsumen")
        hasil = aksiCur.fetchall()
        aksiCur.close()
        return hasil

    ## Untuk Mencari Seluruh nama_perusahaan Pada Table Konsumen
    # ============ FILTER KONSUMEN ============
    def filterKonsumen(self, cari):
        try:
            aksiCur = self.koneksi.cursor()
            query = "SELECT * FROM konsumen WHERE nama_perusahaan LIKE %s"
            aksiCur.execute(query, (f"%{cari}%",))
            hasil = aksiCur.fetchall()
            return hasil
        except Exception as e:
            print(f"Terjadi kesalahan saat filter konsumen: {e}")
            return






