username = "angelina"
passwd = 123456789
i = 1
while True:
    getUsername = input("Masukkan username = ")
    if getUsername == username:
        break
    else:
        print("Username tidak sama")
while i <= 3:
    getPasswd = int(input("Masukkan password = "))
    if getPasswd == passwd:
        print("Anda berhasil login")
        break
    else:
        print("Password salah")
    if i == 3:
        print("Username atau password salah, coba lagi nanti")
        break
    i += 1
