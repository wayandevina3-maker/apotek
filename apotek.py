print("===== DATA OBAT APOTEK =====")

obat = {
    1: ["Paracetamol", 5000, 50],
    2: ["Amoxicillin", 12000, 30],
    3: ["Antasida", 8000, 40],
    4: ["Vitamin C", 10000, 25],
    5: ["CTM", 4000, 35],
    6: ["Ibuprofen", 9000, 20],
    7: ["Oralit", 3000, 45],
    8: ["Loratadine", 11000, 15],
    9: ["OBH", 15000, 20],
    10: ["Zinc", 7000, 30]
}

for nomor, data in obat.items():
    print(nomor, data[0], "- Rp", data[1],
          "- Stok:", data[2])

pilihan = int(input("\nPilih nomor obat       : "))
jumlah = int(input("Masukkan jumlah obat    : "))

if pilihan >= 1 and pilihan <= 10:
    nama = obat[pilihan][0]
    harga = obat[pilihan][1]
    stok = obat[pilihan][2]

    print("\n===== HASIL PERBANDINGAN =====")
    print("Nama obat                        :", nama)
    print("Stok tersedia                    :", stok)
    print("Jumlah pembelian                 :", jumlah)
    print("Stok lebih dari 10               :", stok > 10)
    print("Stok kurang dari 10              :", stok < 10)
    print("Stok sama dengan 10              :", stok == 10)
    print("Jumlah tidak sama dengan stok    :", jumlah != stok)
    print("Pembelian maksimal stok          :", jumlah <= stok)
    print("Pembelian minimal 1              :", jumlah >= 1)

else:
    print("Nomor obat tidak tersedia.")