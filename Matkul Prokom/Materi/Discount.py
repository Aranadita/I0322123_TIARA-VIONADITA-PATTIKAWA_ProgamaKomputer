print("==================================")
Harga_baju      = int(input("Masukkan harga baju    = "))
Total_harga     = 0
Diskon          = 0
if Harga_baju > 100000:
    Diskon      = Harga_baju * (10/100)
    
Total_harga = Harga_baju - Diskon
    
print("==================================")
print("Nilai pembayaran anda sejumlah   =" , Total_harga)
print("Discount yang anda dapatkan      =" , Diskon )
print("---Terima kasih sudah berbelanja---")