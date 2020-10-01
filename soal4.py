banyak = int(input("Banyak angka? "))
tempat = []
for i in range(banyak):
    tempat.append(int(input("Masukkan angka ke{} = ".format(i+1))))
print("Nilai maksimal = {}".format(max(tempat)))
print("Nilai minimal = {}".format(min(tempat)))
