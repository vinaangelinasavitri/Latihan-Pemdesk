berat = float(input("Masukkan Berat Badan = "))
tinggi = float(input("Masukkan Tinggi Badan = "))
hasil = berat/((tinggi/100)**2)
if hasil < 18.5:
    print("Berat badan anda kurang")
elif 18.5 <= hasil <= 22.9:
    print("Berat badan anda normal")
elif 23 <= hasil <= 29.9:
    print("Berat badan anda berlebih")
elif hasil >= 30:
    print("Anda Obesitas")
else:
    print("Inputan salah")
