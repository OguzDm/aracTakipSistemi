from Car import Car_T

erisimListesi = [Car_T() for i in range(3)]                   #Car_T classından bir obje listesi erişim listesi olarak oluşturuldu.

def ekleme(sayi):                                               #Erişim listesine kayıt eklemek için oluşturulmuş bir fonksiyon


    erisimListesi[sayi].arac_ureticisi = input("Lütfen Aracınızın markasını giriniz")
    erisimListesi[sayi].arac_modeli = input("Lütfen Aracınızın modelini giriniz")
    erisimListesi[sayi].renk = input("Lütfen Aracınızın rengini giriniz")
    erisimListesi[sayi].motor_no = int(input("Lütfen Aracınızın motor no'sunu giriniz"))
    erisimListesi[sayi].plaka = input("Lütfen Aracınızın plakasını giriniz")
    erisimListesi[sayi].sasi_no = int(input("Lütfen aracınızın sasi numarasını giriniz"))

def dosyaYaz(sayi):
    f.write(str(sayi + 1) + "-)")
    f.write(erisimListesi[sayi].arac_ureticisi + " ")
    f.write(erisimListesi[sayi].arac_modeli + " ")
    f.write(erisimListesi[sayi].renk + " ")
    f.write(str(erisimListesi[sayi].motor_no))
    f.write(" " + erisimListesi[sayi].plaka + " ")
    f.write(str(erisimListesi[sayi].sasi_no))
    f.write("\n")




f = open("testfile.txt",'w')                                    #Dosya yazma modunda açıldı.




while 1 :

    for i in range (3):
        print("-----------------Araç Takip Sistemine Hoş Geldiniz--------------------- \n"      #Kullanıcıya bilgi verme ekranı.
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
                 if erisimListesi[j].sasi_no == erisimListesi[i].sasi_no:                   #Burada primary key olarak saşi no kullanılıyor.
                     print("Zaten mevcut olan bir kayıt girmeye çalışıyorsunuz!\n")         #Çünkü şasi no her kayıt için unique bir değerdir.
                     print("Lütfen yeni bir kayıt giriniz\n")
                     ekleme(i)
                     break

                 j = j + 1

             dosyaYaz(i)



        elif secim == 2:

             print("Aramayı Seçtiniz İşleminiz Gerekleştiriliyor...\n")
             aranan = int(input("Aramak istediğiniz index numarasını giriniz"))


        elif secim == 3 :


             print("Silmeyi Seçtiniz İşleminiz Gerçekleştiriliyor...\n")
             silinecek = int(input("Silmek istediğiniz kaydın index numarasını giriniz"))



        elif secim == 4 :
             print("Programdan çıkılıyor...")
             f.close()
             exit(1)

    break






