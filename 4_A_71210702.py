artikel = input("Masukkan artikel yang ingin dipindai: ")
klub = input("Masukkan nama klub favorit anda: ")
skor = input("Masukkan skor yang ingin dicari: ")

h_klub = klub in artikel
h_skor = skor in artikel

if (h_klub and h_skor):
    print("Hasil pencarian ditemukan")
elif (h_klub and not h_skor):
    print("Hanya kata", klub, "yang ditemukan pada artikel ini")
elif (not h_klub and h_skor):
    print("Hanya skor", skor, "yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian", klub, "dan", skor, "tidak ditemukan")
