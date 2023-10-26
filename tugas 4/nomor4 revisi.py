def belahKetupat():
    print("hitung ('1' luas) ('2'keliling)")
    hasilkt = int(input())
    if hasilkt == 1:
        luasKt()
    else:
        if hasilkt == 2:
            kelilingKt()

def jajargenjang():
    print("hitung ('1' luas) ('2'keliling)")
    hasilj = int(input())
    if hasilj == 1:
        jajarGenjangLuas()
    else:
        if hasilj == 2:
            jajarGenjangKeliling()

def jajarGenjangKeliling():
    sisiA = int(input("masukan sisiA : "))
    sisiB = int(input("masukan sisiB : "))
    keliling = 2 * (sisiA + sisiB)
    print("keliling dari jajar genjang adalah = " + str(keliling))

def jajarGenjangLuas():
    alas = int(input("masukan panjang : "))
    tinggi = int(input("masukan lebar : "))
    luas = alas * tinggi
    print("luas jajar genjang adalah = " + str(luas))

def kelilingKt():
    sisi = int(input("masukan sisi : "))
    keliling = 4 * sisi
    print("keliling dari ketupat adalah = " + str(keliling))

def kelilingL():
    r = float(input("masukan r : "))
    hasil = float(2 * 22) / 7 * r
    print(hasil)

def kelilingLayang():
    sisi = int(input("masukan sisi : "))
    keliling = 4 * sisi
    print("keliling dari layang-layang adalah = " + str(keliling))

def kelilingT():
    a = int(input("masukan A : "))
    c = int(input("masukan C :"))
    b = int(input("masukan B :"))
    d = int(input("masukan D :"))
    hasil = a + b + c + d
    print(hasil)

def layang():
    print("hitung ('1' luas) ('2'keliling)")
    hasill = int(input())
    if hasill == 1:
        luasLayang()
    else:
        if hasill == 2:
            kelilingLayang()

def lingkaran():
    print("hitung ('1' luas) ('2'keliling)")
    hasill = int(input())
    if hasill == 1:
        luasL()
    else:
        if hasill == 2:
            kelilingL()

def luasKt():
    sisi = int(input("masukan sisi : "))
    diagonal1 = int(input("masukan diagonal1 : "))
    diagonal2 = int(input("masukan diagonal2 : "))
    luas = float(diagonal1 * diagonal2) / sisi
    print("luas dari ketupat adalah = " + str(luas))

def luasL():
    r = float(input("masukan r : "))
    hasil = float(22) / 7 * (r * r)
    print(hasil)

def luasLayang():
    sisia = int(input("masukan sisia : "))
    sisib = int(input("masukan sisib : "))
    diagonal1 = int(input("masukan diagonal1 : "))
    diagonal2 = int(input("masukan diagonal2 : "))
    luas = float(diagonal1 * diagonal2) / 2
    print("luas dari layang-layang adalah = " + str(luas))

def luasT():
    a = int(input("masukan alasA : "))
    b = int(input("masukan alasB : "))
    t = int(input("masukan tinggi : "))
    hasil = float(1) / 2 * (a + b) * t
    print(hasil)

def persegi():
    print("hitung ('1' luas) ('2'keliling)")
    hasilps = int(input())
    if hasilps == 1:
        persegiLuas()
    else:
        if hasilps == 2:
            persegiKeliling()

def persegiKeliling():
    sisi = int(input("masukan sisi : "))
    keliling = 4 * sisi
    print("keliling dari persegi adalah = " + str(keliling))

def persegiLuas():
    sisi = float(input("masukan sisi : "))
    luas = sisi * sisi
    print("luas dari persegi adalah = " + str(luas))

def persegiPanjang():
    print("hitung ('1' luas) ('2'keliling)")
    hasilp = int(input())
    if hasilp == 1:
        persegiPanjangLuas()
    else:
        if hasilp == 2:
            persegiPanjangKeliling()

def persegiPanjangKeliling():
    panjang = int(input("masukan panjang : "))
    lebar = int(input("masukan lebar : "))
    keliling = 2 * (panjang + lebar)
    print("keliling dari persegi panjang adalah = " + str(keliling))

def persegiPanjangLuas():
    panjang = int(input("masukan panjang : "))
    lebar = int(input("masukan lebar : "))
    luas = panjang * lebar
    print("luas persegi panjang adalah = " + str(luas))

def segitiga():
    print("hitung ('1' luas) ('2'keliling)")
    hasilsg = int(input())
    if hasilsg == 1:
        segitigaLuas()
    else:
        if hasilsg == 2:
            segitigaKeliling()

def segitigaKeliling():
    alas = int(input("masukan alas : "))
    tinggi = int(input("masukan tinggi : "))
    keliling = float(1) / 2 * (alas * tinggi)
    print("keliling dari segitiga adalah = " + str(keliling))

def segitigaLuas():
    sisi = int(input("masukan sisi : "))
    luas = 3 * sisi
    print("keliling dari segitiga adalah = " + str(luas))

def trapesium():
    print("hitung ('1' luas) ('2'keliling)")
    hasil = int(input())
    if hasil == 1:
        luasT()
    else:
        if hasil == 2:
            kelilingT()

def main():
    x = True
    while x:
        print("\n (1)persegiPanjang) \n (2)trapesium) \n (3)jajargenjang) \n (4)persegi) \n (5)lingkaran) \n (6)ketupat) \n (7)layang-layang) \n (8)segitiga) \n ")
        pilihan = int(input("masukan pilihan :"))
        if pilihan == 1:
            print("perhitungan persegi panjang")
            persegiPanjang()
        elif pilihan == 2:
            print("perhitungan trapesium")
            trapesium()
        elif pilihan == 3:
            print("perhitungan jajar genjang")
            jajargenjang()
        elif pilihan == 4:
            print("perhitungan persegi")
            persegi()
        elif pilihan == 5:            
            print("perhitungan lingkaran")
            lingkaran()
        elif pilihan == 6:
            print("perhitungan ketupat")
            belahKetupat()
        elif pilihan == 7:
            print("perhitungan layang-layang")
            layang()
        elif pilihan == 8:
            print("perhitungan segitiga")
            segitiga()
        elif pilihan < 1 and pilihan > 8:
            print("input anda salah")
            
        print("Apakah anda ingin menghitung bangun datar yang lain? 'Ya' 'Tidak'")
        pilihanulang = input()
        if pilihanulang == "Ya":
            x = True
        elif pilihanulang == "Tidak":
            x = False
            print("terima kasih telah menggunakan program kami")
        elif pilihanulang != "Tidak":
            x = False
            print("input salah")

           

main()