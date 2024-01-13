from prettytable import from_db_cursor
import mysql.connector
import os

class Buah:
    def __init__(self):
        # Connecting to the database
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password='',
            database='5220411204'
        )
        self.data = self.mydb.cursor()

    def daftarBuah(self):
        self.data.execute("SELECT * FROM Buah")
        p = from_db_cursor(self.data)
        print(p)
        

class BuahCRUD(Buah):
    def tambahBuah(self):
        self.daftarBuah()  
        
        nama = str(input('Masukan nama buah: '))
        harga = int(input('Masukan harga buah: '))

        sql = "INSERT INTO Buah (Nama_buah, Harga_buah) VALUES (%s, %s)"
        value = (nama, harga)
        self.data.execute(sql, value)
        self.mydb.commit()

        print('\n{} data berhasil ditambahkan'.format(self.data.rowcount))
        os.system('pause')
        os.system('cls')

        print('-=-=-=-=-= Daftar Terbaru =-=-=-=-=-')
        self.daftarBuah()
        os.system('pause')
        os.system('cls')

    def updateBuah(self):
        self.daftarBuah()

        id_buah = int(input('Pilih ID buah yang akan diupdate: '))
        nama_baru = str(input('Masukkan nama baru buah: '))
        harga_baru = int(input('Masukkan harga baru buah: '))

        sql = 'UPDATE Buah SET Nama_buah = %s, Harga_buah = %s WHERE ID = %s'
        value = (nama_baru, harga_baru, id_buah)

        self.data.execute(sql, value)
        self.mydb.commit()

        print('\n{} data berhasil diupdate'.format(self.data.rowcount))
        os.system('pause')

        print('-=-=-=-=-= Daftar Terbaru =-=-=-=-=-')
        self.daftarBuah()
        os.system('pause')
        os.system('cls')

    def hapusBuah(self):
        self.daftarBuah()

        id_buah = int(input('Pilih ID buah yang akan dihapus: '))

        cek_sql = 'SELECT * FROM Buah WHERE ID = %s'
        cek_value = (id_buah,)
        self.data.execute(cek_sql, cek_value)
        cek_hasil = self.data.fetchone()

        if cek_hasil:
            hapus_sql = 'DELETE FROM Buah WHERE ID = %s'
            hapus_value = (id_buah,)
            self.data.execute(hapus_sql, hapus_value)
            self.mydb.commit()

            print('Data dengan ID {} berhasil dihapus'.format(id_buah))
            os.system('pause')

            print('-=-=-=-=-= Daftar Terbaru =-=-=-=-=-')
            self.daftarBuah()
            os.system('pause')
            os.system('cls')
        else:
            print('ID buah tidak ditemukan.')

class Pembelian(Buah):
    def beliBuah(self):
        self.daftarBuah()

        pilih = int(input('Pilih Id buah yang mau dibeli: '))
        jum = int(input('Masukan jumlah buah: '))

        sql = 'SELECT Harga_buah, Nama_buah FROM Buah WHERE ID=%s'
        value = (pilih,)
        self.data.execute(sql, value)
        hasil = self.data.fetchone()

        if hasil:
            harga, nama_buah = hasil

            t = harga * jum
            print('Total Harga: ', t)

            uang = int(input('\nMasukan Uang anda: '))
            kembalian = uang - t

            os.system('pause')
            os.system('cls')

            print("=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("      STRUK BELANJA")
            print('=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('Jenis Buah   : ', nama_buah)
            print('Jumlah Buah  : ', jum)
            print('Total Harga  : ', t)
            print('Total Uang   : ', uang)
            print('Kembalian    : ', kembalian)
            print("=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("      TERIMA  KASIH")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=")
            os.system('pause')
            os.system('cls')

        else:
            print('ID buah tidak ditemukan.')
            os.system('pause')
            os.system('cls')


while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("      MENU  BELANJA")
    print('=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('1. Melihat daftar buah')
    print('2. Membeli buah')
    print('3. Menambah buah')
    print('4. Menghapus buah')
    print('5. Mengupdate daftar buah')
    print('0. Exit')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=')
    plh = input('Pilih menu (0-5): ')

    if plh == '1':
        os.system('cls')
        buah_gud = Buah()
        buah_gud.daftarBuah()
        os.system('pause')
        os.system('cls')

    elif plh == '2':
        os.system('cls')
        pembelian_gud = Pembelian()
        pembelian_gud.beliBuah()

    elif plh == '3':
        os.system('cls')
        buah_crud_gud = BuahCRUD()
        buah_crud_gud.tambahBuah()

    elif plh == '4':
        os.system('cls')
        buah_crud_gud = BuahCRUD()
        buah_crud_gud.hapusBuah()

    elif plh == '5':
        os.system('cls')
        buah_crud_gud = BuahCRUD()
        buah_crud_gud.updateBuah()
        
    elif plh == '0':
        os.system('cls')
        print("\nProgram selesai")
        break

    else:
        print("Pilihan tidak ada, silakan pilih lagi antara 0 dan 5")
