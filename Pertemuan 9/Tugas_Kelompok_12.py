import os

class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.TahunKeluaran = tahun_keluaran
        self.Nama = nama
        self.Warna = warna
        self.Kecepatan = kecepatan
        self.BahanBakar = bahan_bakar
        self.JumlahRoda = jumlah_roda
        self.KapasitasPenumpang = kapasitas_penumpang

    def info(self):
        print(f"""
<> {self.Nama} ({self.TahunKeluaran})
<> Warna                : {self.Warna}
<> Kecepatan            : {self.Kecepatan} km/h
<> Bahan Bakar          : {self.BahanBakar}
<> Jumlah Roda          : {self.JumlahRoda}
<> Kapasitas Penumpang  : {self.KapasitasPenumpang}""")

class Kereta(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                 gerbong, jumlah_kursi, jenis_layanan_kereta, rute):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.Gerbong = gerbong
        self.JumlahKursi = jumlah_kursi
        self.JenisLayananKereta = jenis_layanan_kereta
        self.rute = rute
    
    def tambahRute(self, new_rute):
        self.rute.append(new_rute)

    def kurangiRute(self, old_rute):
        if old_rute in self.rute:
            self.rute.remove(old_rute)

    def info(self):
        super().info()
        print(f"""<> Gerbong              : {self.Gerbong}
<> Jumlah Kursi         : {self.JumlahKursi} 
<> Jenis Layanan        : {self.JenisLayananKereta}
<> Rute                 : {', '.join(self.rute)}
              """)

class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                 jenis_mobil, arah):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis = jenis_mobil
        self.arah = arah
        self.urutan = [self.arah]
        self.mesin_on = False

    def startEngine(self):
        if not self.mesin_on:
            print("Mesin Dinyalakan")
            print()
            self.mesin_on = True
        else:
            print("Mesin Sudah Dinyalakan")
            print()
            

    def stopEngine(self):
        if self.mesin_on:
            print("Mesin Dimatikan")
            print()
            self.mesin_on = False
            os.system('pause')
        else:
            print("Mesin Sudah Dimatikan")
            print()

    def BelokKanan(self):
        if self.mesin_on:
            if self.arah == "Utara":
                self.arah = "Timur"
            elif self.arah == "Timur":
                self.arah = "Selatan"
            elif self.arah == "Selatan":
                self.arah = "Barat"
            elif self.arah == "Barat":
                self.arah = "Utara"
            
            self.urutan.append(self.arah)
            print(f"Bergerak ke arah {self.arah}")
            print()

            return self.arah
        else:
            print("Mesin Belum Dinyalakan")

    def BelokKiri(self):
        if self.mesin_on:
            if self.arah == "Utara":
                self.arah = "Barat"
            elif self.arah == "Barat":
                self.arah = "Selatan"
            elif self.arah == "Selatan":
                self.arah = "Timur"
            elif self.arah == "Timur":
                self.arah = "Utara"

            self.urutan.append(self.arah)
            print(f"Bergerak ke arah {self.arah}")
            print()

            return self.arah
        else:
            print("Mesin Belum Dinyalakan")

    def Maju(self):
        if self.mesin_on:
            if self.arah == "Utara":
                self.arah_mata_angin = "Utara"
            elif self.arah == "Barat":
                self.arah_mata_angin = "Barat"
            elif self.arah == "Selatan":
                self.arah_mata_angin = "Selatan"
            elif self.arah == "Timur":
                self.arah_mata_angin = "Timur"

            self.urutan.append(self.arah_mata_angin)
            print(f"Bergerak ke arah {self.arah_mata_angin}")
            print()
            return self.arah_mata_angin
        else:
            print("Mesin Belum Dinyalakan")

    def Mundur(self):
        if self.mesin_on:
            if self.arah == "Utara":
                self.arah_mata_angin = "Selatan"
            elif self.arah == "Barat":
                self.arah_mata_angin = "Timur"
            elif self.arah == "Selatan":
                self.arah_mata_angin = "Utara"
            elif self.arah == "Timur":
                self.arah_mata_angin = "Barat"
            
            self.urutan.append(self.arah_mata_angin)
            print(f"Bergerak ke arah {self.arah_mata_angin}")
            print()
            return self.arah_mata_angin
        else:
            print("Mesin Belum Dinyalakan")

    def info_rute(self):
        print('Daftar Rute :')
        for urutan in self.urutan:
            print("Menuju ",urutan)

class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                 jenis_mobil, arah ,front_wing, rear_wing):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                         jenis_mobil, arah)
        self.FrontWing = front_wing
        self.RearWing = rear_wing

    def race(self):
        print("Mobil balap sedang balapan")

    def info(self):
        print(f"""
<> {self.Nama} ({self.TahunKeluaran})
<> Warna                : {self.Warna}
<> Kecepatan            : {self.Kecepatan} km/h
<> Bahan Bakar          : {self.BahanBakar}
<> Jumlah Roda          : {self.JumlahRoda}
<> Kapasitas Penumpang  : {self.KapasitasPenumpang}    
<> {self.FrontWing}
<> {self.RearWing}
              """)

class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                 jenis_mobil, arah ,sunroof_type, shock_breaker):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang,
                         jenis_mobil, arah)
        self.SunroofType = sunroof_type
        self.ShockBreaker = shock_breaker

    def sunroofTerbuka(self):
        return "Sunroof dibuka"

    def sunroofTertutup(self):
        return "Sunroof ditutup"
    
    def info(self, kondisi_sunroof):
        print(f"""
<> {self.Nama} ({self.TahunKeluaran})
<> Warna                : {self.Warna}
<> Kecepatan            : {self.Kecepatan} km/h
<> Bahan Bakar          : {self.BahanBakar}
<> Jumlah Roda          : {self.JumlahRoda}
<> Kapasitas Penumpang  : {self.KapasitasPenumpang}    
<> {self.SunroofType}
<> {self.ShockBreaker}
<> Kondisi Sunroof      : {kondisi_sunroof}
              """)

while True:
    os.system('cls')
    print('-'*50)
    print('WELCOME')
    print('-'*50)
    print('1. Kereta')
    print('2. Mobil')
    print('0. Exit')
    print('-'*50)
    pilih = int(input('Pilihan : '))
    if pilih == 1:
        while True:
            os.system('cls')
            print('Menu Kereta')
            print('-'*50)
            print('1. Isi Data Kereta')
            print('2. Tambah Rute Kereta')
            print('3. Hapus Rute Kereta')
            print('4. Info Kereta')
            print('0. Kembali')
            print('-'*50)
            pilihan = int(input("Masukkan Pilihan Anda : "))

            if pilihan == 1:
                os.system('cls')
                print('Isi Data Kereta')
                print('-'*30)
                bahanbakar = 'Solar'
                jumlahRoda = 12
                JumlahKursi = 50
                tahun_keluaran = int(input("Masukkan Tahun Keluaran Kereta           : "))
                nama = input('Masukkan Nama Kereta                     : ')
                warna = input('Masukkan Warna Kereta                    : ')
                kecepatan = int(input('Masukkan Kecepatan Kereta                : '))
                while True:
                    KapasitasPenumpang = int(input("Masukkan Kapasitas Penumpang             : "))
                    if KapasitasPenumpang > 50: print('Melebihi Batas Kursi')
                    else: break
                JenisGerbong = input("Masukkan Jenis Gerbong                   : ")
                JenisLayanan = input("Jenis Layanan Kereta                     : ")
                rute = input("Masukkan Rute (Pisahkan dengan , (koma)) : ").split(",")
                obj_KA = Kereta(tahun_keluaran, nama, warna, kecepatan, bahanbakar, jumlahRoda, KapasitasPenumpang, JenisGerbong, JumlahKursi, JenisLayanan, rute)

# Batas ss

            elif pilihan == 2:
                os.system('cls')
                print('Tambah Rute Kereta')
                print('-'*30)
                rute = input("Masukkan Rute Tambahan : ")
                obj_KA.tambahRute(rute)
                print(f'Rute {rute}, berhasil ditambahkan')
                os.system('pause')

            elif pilihan == 3:
                os.system('cls')
                print('Hapus Rute Kereta')
                print('-'*30)
                rute = input("Masukkan Rute yang Dihapus : ")
                obj_KA.kurangiRute(rute)
                print(f'Rute {rute}, berhasil dihapus')
                os.system('pause')

            elif pilihan == 4:
                os.system('cls')
                print('Info Data Kereta')
                print('-'*30)
                obj_KA.info()
                os.system('pause')

            elif pilihan == 0:
                os.system('cls')
                break

            else:
                print('Kode Error')
                os.system('pause')
# Batas ss

    elif pilih == 2:
        while True:
            os.system('cls')
            print("Menu Mobil")
            print('-'*50)
            print('1. Mobil Balap')
            print('2. Mobil CrossRoad')
            print('0. Kembali')
            print('-'*50)
            pilihan = int(input("Masukkan Pilihan Anda : "))

            if pilihan == 0:
                os.system('cls')
                break

# Batas ss

            elif pilihan == 1:
                while True:
                    os.system('cls')
                    print('\nMobil Balap')
                    print('-'*50)
                    print('1. Isi Data mobil')
                    print('2. Lihat Info mobil')
                    print('3. Masuk Mode Balap')
                    print('0. Kembali')
                    print('-'*50)
                    pilih = int(input('Silakan memilih menu: '))

# Batas

                    if pilih == 1:
                        os.system('cls')
                        print('Mobil Balap')
                        print('-'*50)
                        jumlahRoda = 4
                        tahun_keluaran = int(input("Masukkan Tahun Keluaran mobil           : "))
                        nama = input('Masukkan Nama mobil                     : ')
                        warna = input('Masukkan Warna mobil                    : ')
                        bahanbakar = input('Masukkan Bahan Bakar mobil              : ')
                        kecepatan = int(input('Masukkan Kecepatan mobil                : '))
                        KapasitasPenumpang = int(input("Masukkan Kapasitas Penumpang            : "))
                        jenis =("Mobil Balap ")

                        fornt_Wing = input('Mau menggunakan fornt_Wing? (Y/N)       : ')
                        if fornt_Wing == 'Y':
                            fornt_Wing = 'Mobil menggunakan Fornt Wing'
                        else:
                            fornt_Wing = 'Mobil tidak menggunakan Fornt Wing'
                        
                        rear_Wing = input('Mau menggunakan rear_Wing? (Y/N)        : ')
                        if rear_Wing == 'Y':
                            rear_Wing ='Mobil menggunakan Rear Wing'
                        else:
                            rear_Wing ='Mobil tidak menggunakan Rear wing'
                        
                        arah = input('Masukkan Arah Anda (U/S/T/B)            : ')
                        if arah == 'U':
                            arah = "Utara"
                        elif arah == 'T':
                            arah = 'Timur'
                        elif arah == 'S':
                            arah = 'Selatan'
                        elif arah == 'B':
                            arah = 'Barat'
                        os.system('pause')
                        obj_Mobil = MobilBalap(tahun_keluaran, nama, warna, kecepatan, bahanbakar, jumlahRoda, KapasitasPenumpang, jenis, arah, fornt_Wing, rear_Wing)

# Batas ss

                    elif pilih == 2:
                        obj_Mobil.info()
                        os.system('pause')

                    elif pilih == 3:
                            while True:
                                os.system('cls')
                                print('Mode Balap')
                                print('-'*30)
                                print('1. Mulai')
                                print('2. Hasil Rute')
                                print('0. Kembali')
                                print('-'*30)
                                pilihanBalap = int(input("Masukkan Pilihan Anda : "))
                                os.system('cls')

    # Batas ss

                                if pilihanBalap == 1:
                                    while True:
                                        print()
                                        print('Menu:')
                                        print('1. Nyalakan Mesin')
                                        print('2. Belok Kanan')
                                        print('3. Belok Kiri')
                                        print('4. Maju')
                                        print('5. Mundur')
                                        print('6. Stop Engine dan Selesai')
                                        print('0. Kembali')
                                        choice = int(input('Pilih aksi: '))
                                        if choice == 1:
                                            obj_Mobil.startEngine()
                                            os.system('pause')
                                            
                                        elif choice == 2:
                                            obj_Mobil.BelokKanan()
                                            os.system('pause')

                                        elif choice == 3:
                                            obj_Mobil.BelokKiri()
                                            os.system('pause')

                                        elif choice == 4:
                                            obj_Mobil.Maju()
                                            os.system('pause')

                                        elif choice == 5:
                                            obj_Mobil.Mundur()
                                            os.system('pause')

                                        elif choice == 6:
                                            obj_Mobil.stopEngine()
                                        
                                        elif choice == 0:
                                            False
                                            break

                                        else:
                                            print('Kode Error')
                                            os.system('pause')

    # Batas ss

                                elif pilihanBalap == 2:
                                    obj_Mobil.info_rute()
                                    os.system('pause')
                                    continue

                                elif pilihanBalap == 0:
                                    break

                                else:
                                    print('Kode Error')
                                    os.system('pause')

                    elif pilih == 0:
                        break

                    else:
                        print('kode error')
                        os.system('pause')

# Batas ss

            elif pilihan == 2:
                os.system('cls')
                print('\nMobil Crossroad')
                print('-'*50)
                jumlahRoda = 4
                tahun_keluaran = int(input("Masukkan Tahun Keluaran mobil           : "))
                nama = input('Masukkan Nama mobil                     : ')
                warna = input('Masukkan Warna mobil                    : ')
                bahanbakar = input('Masukkan Bahan Bakar mobil              : ')
                kecepatan = int(input('Masukkan Kecepatan mobil                : '))
                KapasitasPenumpang = int(input("Masukkan Kapasitas Penumpang            : "))
                jenis =("Mobil Crossroad ")
                
                print('-'*50)
                print('1. Panoramic Sunroof')
                print('2. Sliding Sunroof')
                print('3. Tilted Sunroof')
                print('-'*50)
                
                sunroofType = int(input('Mau menggunakan Sunroof tipe apa?       : '))
                if sunroofType == 1: 
                    sunroofType = "Panoramic Sunroof"
                elif sunroofType == 2:
                    sunroofType = 'Sliding Sunroof'
                elif sunroofType == 3: 
                    sunroofType = 'Tilted Sunroof'

                shockBreaker = ('Kodisi Shock Breaker : Sangat Bagus ')
                
                arah = input('Masukkan Arah Anda (U/S/T/B)            : ')
                if arah == 'U': arah = "Utara"
                elif arah == 'T': arah = 'Timur'
                elif arah == 'S': arah = 'Selatan'
                elif arah == 'B': arah = 'Barat'
                obj_Mobil = MobilCrossroad(tahun_keluaran, nama, warna, kecepatan, bahanbakar, jumlahRoda, KapasitasPenumpang, jenis, arah, sunroofType, shockBreaker)

                print("""
Masukkan Kondisi Sunroof
1. Terbuka
2. Tertutup
---------------------------
                        """)
                sunroofCondition = int(input("Masukkan Pilihan Anda : "))
                
                if sunroofCondition == 1:
                    condition = obj_Mobil.sunroofTerbuka()
                elif sunroofCondition == 2:
                    condition = obj_Mobil.sunroofTertutup()
                else:
                    print('Error')

                obj_Mobil.info(condition)
                os.system('pause')

            else:
                print('Kode Error')
                os.system('pause')

    elif pilih == 0:
        break

    else:
        print('Kode Error')
        os.system('pause')

print('-'*30)
print('Terimakasih')
print('-'*30)
        
