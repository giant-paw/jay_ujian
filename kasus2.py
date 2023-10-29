class giant_bank :
    def __init__(self, nama_pemilik, saldo_awal) :
        self.pemilik = nama_pemilik
        self.saldo = saldo_awal
        
    def setor(self, jumlah_setor) :
        self.saldo += jumlah_setor
        
    def penarikan(self, jumlah_tarik) :
        if jumlah_tarik <= self.saldo :
            self.saldo -= jumlah_tarik
        else:
            print("Saldo tidak cukup!!")
    
    def cek_saldo(self) :
        return self.saldo
    
rekening = giant_bank("Abdur Golkar", 300000)

while True:
    print("\nMenu:")
    print("1. Setoran")
    print("2. Penarikan")
    print("3. Cek Saldo")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        jumlah_setoran = float(input("Masukkan jumlah setoran: "))
        rekening.setor(jumlah_setoran)
        print("Setoran berhasil.")
    elif pilihan == '2':
        jumlah_penarikan = float(input("Masukkan jumlah penarikan: "))
        rekening.penarikan(jumlah_penarikan)
    elif pilihan == '3':
        saldo = rekening.cek_saldo()
        print(f"Saldo rekening {rekening.pemilik} : ${saldo}")
    elif pilihan == '4':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")