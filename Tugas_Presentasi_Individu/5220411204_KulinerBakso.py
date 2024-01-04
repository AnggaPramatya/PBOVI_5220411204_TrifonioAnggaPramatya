import os

class Kuliner:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def total(self):
        return self.harga 


class Makanan(Kuliner):
    def __init__(self, nama, harga, rasa):
        super().__init__(nama, harga)
        self.rasa = rasa

    def info_Makanan(self):
        return f"{self.nama} rasanya {self.rasa} dengan harga {self.harga}"


class Minuman(Kuliner):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.ukuran = ukuran
    
    def info_Minuman(self):
        return f"{self.nama} memiliki ukuran {self.ukuran} dengan harga {self.harga}"


class JenisMakanan(Makanan):
    def __init__(self, nama, harga, rasa, jenis):
        super().__init__(nama, harga, rasa)
        self.jenis = jenis

    def tipe_makanan(self):
        if self.jenis == "berkuah":
            return f"{self.nama} adalah makanan berkuah."
        elif self.jenis == "kering":
            return f"{self.nama} adalah makanan kering."

pesanan = []
while True:
    print("""
------------------
|  BAKSO NORMAL  |
------------------
1. Makanan
2. Minuman
3. Struk
0. Exit
------------------
    """)
    pilih = int(input('Silakan masukkan pilihan anda: '))
    os.system('cls')

    if pilih == 1:  # Menu makanan
        while True:
            print('-'* 17)
            print('Menu Bakso')
            print('-'* 17)
            print('1. Bakso Normal   : 10.000')
            print('2. Bakso Kotak    : 14.000')
            print('3. Bakso Jumbo    : 18.000')
            print('0. Kembali')
            print('-'* 17)
            pilihMakan = int(input('Silakan pilih makanan anda: '))

            if pilihMakan in [1, 2, 3]:
                if pilihMakan == 1:
                    bakso = 'Bakso Normal'
                    hargaMakan = 10000
                elif pilihMakan == 2:
                    bakso = 'Bakso Kotak'
                    hargaMakan = 14000
                elif pilihMakan == 3:
                    bakso = 'Bakso Jumbo'
                    hargaMakan = 18000

                print('\nMau pake sambal?')
                print('-'* 17)
                print('1. iya')
                print('2. tidak')
                print('-'* 17)
                pilihSambal = int(input('Silakan pilih: '))
                print('--Pesanan telah ditambahkan--')
                os.system('pause')
                os.system('cls')

                if pilihSambal == 1:
                    sambal = 'Pedas'
                elif pilihSambal == 2:
                    sambal = 'Tidak Pedas'
                else: 
                    print('Pilihan tidak tersedia, silakan pilih lagi')

                pesanan.append({
                    "item": bakso,
                    "harga": hargaMakan,
                    "tambahan": sambal
                })


            elif pilihMakan == 0:
                os.system('cls')
                break

            else: 
                print('KODE ERROR')

    elif pilih == 2:    # Menu minuman
        while True:
            print('-'* 17)
            print('Menu Minuman')
            print('-'* 17)
            print('1. Air Putih   : 1.000')
            print('2. Es Jeruk    : 3.000')
            print('3. Es Teh      : 2.000')
            print('0. Kembali')
            print('-'* 17)
            pilihMinum = int(input('Silakan pilih minuman anda: '))

            if pilihMinum in [1, 2, 3]:
                if pilihMinum == 1:
                    minuman = 'Air Putih'
                    hargaMinum = 1000
                elif pilihMinum == 2:
                    minuman = 'Es Jeruk'
                    hargaMinum = 3000
                elif pilihMinum == 3:
                    minuman = 'Es Teh'
                    hargaMinum = 2000

                print('\nPilih ukuran minuman')
                print('-'* 17)
                print('1. Normal')
                print('2. Jumbo')
                print('-'* 17)
                pilihUkuran = int(input('Silakan pilih: '))
                print('--Pesanan telah ditambahkan--')
                os.system('pause')
                os.system('cls')

                if pilihUkuran == 1:
                    ukuran = 'Normal'
                elif pilihUkuran == 2:
                    ukuran = 'Jumbo'
                else:
                    print('Pilihan tidak tersedia, silakan pilih lagi')


                pesanan.append({
                    "item": minuman,
                    "harga": hargaMinum,
                    "ukuran": ukuran
                })

            elif pilihMinum == 0:
                os.system('cls')
                break

            else:
                print('KODE ERROR')

    elif pilih == 3: # Struk pesanan
        total_harga = 0
        if len(pesanan) == 0:
            print("Belum ada pesanan.")
        else:
            print("\n============== STRUK PEMBELIAN ==============")
            for pesan in pesanan:

                if "ukuran" in pesan:
                    minuman = Minuman(pesan['item'], pesan['harga'], pesan['ukuran'])
                    print(f"""\n
<> {pesan['item']} 
Ukuran  : {pesan['ukuran']}
Harga   : Rp {pesan['harga']}""")
                    print('Deskripsi:')
                    print(f"{minuman.info_Minuman()}")

                else:
                    makanan = Makanan(pesan['item'], pesan['harga'], pesan['tambahan'])
                    print(f"""\n
<> {pesan['item']} 
Harga    : Rp {pesan['harga']} 
Tambahan : {pesan['tambahan']}""")
                    print('Deskripsi:')
                    print(f"{makanan.info_Makanan()}")

                total_harga += pesan['harga']
            print(f"\n~Total: Rp {total_harga}")
            print("\n============== TERIMA KASIH ==============")

            pesanan = []  # Mengosongkan pesanan setelah struk dicetak
            print('')
            os.system('pause')
            os.system('cls')

    elif pilih == 0:
        print('==== TERIMAKASIH ====')
        exit()
    else:
        print('Pilihan tidak tersedia, silakan pilih lagi')
