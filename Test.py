from Car import Car_T
from functions import ekleme
from functions import dosyaYaz
from functions import erisimListesi






try:
    f = open("testfile.txt","x")
    for i in range(1000):
        print(
            "-----------------Araç Takip Sistemine Hoş Geldiniz--------------------- \n"  # Kullanıcıya bilgi verme ekranı.
            "Lütfen Yapmak İstediğiniz İşlemi Seçiniz...\n"
            "1-Yeni Kayıt\n"
            "2-Arama\n"
            "3-Silme\n"
            "4-Çıkış\n")

        secim = int(input("Lütfen seçiminizi yapınız"))

        if secim == 1:
            j = 0
            print("Eklemeyi seçtiniz işleminiz gerçekleştiriliyor...\n")
            ekleme(i)

            while j < i:
                if erisimListesi[j].sasi_no == erisimListesi[i].sasi_no:  # Burada primary key olarak saşi no kullanılıyor.
                    print(
                        "Zaten mevcut olan bir kayıt girmeye çalışıyorsunuz!\n")  # Çünkü şasi no her kayıt için unique bir değerdir.
                    print("Lütfen yeni bir kayıt giriniz\n")
                    ekleme(i)
                    break

                j = j + 1

            dosyaYaz(i)


        elif secim == 2:
            k = 0

            print("Aramayı Seçtiniz İşleminiz Gerekleştiriliyor...\n")
            aranan = int(input("Aramak istediğiniz şasi numarasını giriniz"))
            while k < len(erisimListesi):
                if erisimListesi[k].sasi_no == aranan:
                    print(erisimListesi[k].arac_modeli + " " + erisimListesi[k].arac_ureticisi + " " + erisimListesi[
                        k].plaka)
                    break
                k = k + 1
            else:

                print("Kayıt bulunamadı")


        elif secim == 3:

            print("Silmeyi Seçtiniz İşleminiz Gerçekleştiriliyor...\n")
            silinecek = int(input("Silmek istediğiniz kaydın index numarasını giriniz"))



        elif secim == 4:
            print("Programdan çıkılıyor...")
            exit(1)

except FileExistsError:
    liste=[0]
    f = open("testfile.txt", "r")
    bosmu = f.read(1)

    if bosmu != 0:
        f = open("testfile.txt","r")
        line = f.readline()
        iter = 0
        while line :
            record = line.split()
            erisimListesi[iter].arac_ureticisi=record[0]
            erisimListesi[iter].arac_modeli = record[1]
            erisimListesi[iter].renk = record[2]
            erisimListesi[iter].motor_no = int(record[3])
            erisimListesi[iter].plaka = record[4]
            erisimListesi[iter].sasi_no = int(record[5])
            line = f.readline()
            iter = iter + 1
            liste = [iter]


    for i in range(liste[0],1000):
        print(
            "-----------------Araç Takip Sistemine Hoş Geldiniz--------------------- \n"  # Kullanıcıya bilgi verme ekranı.
            "Lütfen Yapmak İstediğiniz İşlemi Seçiniz...\n"
            "1-Yeni Kayıt\n"
            "2-Arama\n"
            "3-Silme\n"
            "4-Çıkış\n")

        secim = int(input("Lütfen seçiminizi yapınız"))

        if secim == 1:
            j = 0
            print("Eklemeyi seçtiniz işleminiz gerçekleştiriliyor...\n")
            ekleme(i)

            while (j) < (i):
                if erisimListesi[j].sasi_no == erisimListesi[i].sasi_no:  # Burada primary key olarak saşi no kullanılıyor.
                    print(
                        "Zaten mevcut olan bir kayıt girmeye çalışıyorsunuz!\n")  # Çünkü şasi no her kayıt için unique bir değerdir.
                    print("Lütfen yeni bir kayıt giriniz\n")
                    ekleme(i)
                    break

                j = j + 1

            dosyaYaz(i)



        elif secim == 2:
            k = 0

            print("Aramayı Seçtiniz İşleminiz Gerekleştiriliyor...\n")
            aranan = int(input("Aramak istediğiniz şasi numarasını giriniz"))
            while k < len(erisimListesi):
                if erisimListesi[k].sasi_no == aranan:
                    print(erisimListesi[k].arac_modeli + " " + erisimListesi[k].arac_ureticisi + " " +  erisimListesi[k].plaka)
                    break
                k = k + 1
            else:

                print("Kayıt bulunamadı")




        elif secim == 3:

            print("Silmeyi Seçtiniz İşleminiz Gerçekleştiriliyor...\n")
            silinecek = int(input("Silmek istediğiniz kaydın index numarasını giriniz"))



        elif secim == 4:
            print("Programdan çıkılıyor...")
            exit(1)








