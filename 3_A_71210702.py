inputan = str(input("Mendatar/Menurun?: "))

if inputan == "Mendatar":
       inputan2 = int(input("Masukkan kolom: "))
       print("#" * inputan2)
elif inputan == "Menurun":
       inputan2 = int(input("Masukkan baris: "))
       print("*\n" * inputan2)
else:
    print("Pola tidak dikenali")
    
