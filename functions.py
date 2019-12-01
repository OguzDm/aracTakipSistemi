from Car import Car_T

erisimListesi = [Car_T() for i in range(1000)]

def ekleme(sayi):          #Erişim listesine kayıt eklemek için oluşturulmuş bir fonksiyon


    erisimListesi[sayi].arac_ureticisi = input("Lütfen Aracınızın markasını giriniz")
    if len(erisimListesi[sayi].arac_ureticisi) > 15:
        erisimListesi[sayi].arac_ureticisi = input("Bu uzunlukta girdi yapamazsınız lütfen yeni bir değer giriniz")

    erisimListesi[sayi].arac_modeli = input("Lütfen Aracınızın modelini giriniz")
    if len(erisimListesi[sayi].arac_modeli)> 15:
        erisimListesi[sayi].arac_modeli = input("Bu uzunlukta girdi yapamazsınız lütfen yeni bir değer giriniz")

    erisimListesi[sayi].renk = input("Lütfen Aracınızın rengini giriniz")
    if len(erisimListesi[sayi].renk)>15:
        erisimListesi[sayi].renk = input("Bu uzunlukta girdi yapamazsınız lütfen yeni bir değer giriniz")

    erisimListesi[sayi].motor_no = int(input("Lütfen Aracınızın motor no'sunu giriniz"))

    erisimListesi[sayi].plaka = input("Lütfen Aracınızın plakasını giriniz")
    if len(erisimListesi[sayi].plaka)>15:
        erisimListesi[sayi].plaka = input("Bu uzunlukta girdi yapamazsınız lütfen yeni bir değer giriniz")

    erisimListesi[sayi].sasi_no = int(input("Lütfen aracınızın sasi numarasını giriniz"))

def dosyaYaz(sayi):
    f = open("testfile.txt","a")            #Dosya ekleme modunda açıldı.
    f.write(str(erisimListesi[sayi].arac_ureticisi) + " ")
    f.write(str(erisimListesi[sayi].arac_modeli) + " ")
    f.write(str(erisimListesi[sayi].renk) + " ")
    f.write(str(erisimListesi[sayi].motor_no))
    f.write(" " + str(erisimListesi[sayi].plaka ) + " ")
    f.write(str(erisimListesi[sayi].sasi_no))
    f.write("\n")
    f.close()



def kayıtArama(sayi):               #Kullanıcı ya da sistem yöneticisinin arama yapması için oluşturulmuş arama fonksiyonu
    k = 0
    while k < len(erisimListesi):
        if erisimListesi[k].sasi_no == sayi:
            #Eğer aranan kayıt bulunduysa kayıdın modeli üreticisi ve plakası yazdırılıyor.
            #Eğer arzu edilirse bütün kayıtta yazdırılabilir.
            print(erisimListesi[k].arac_modeli + " " + erisimListesi[k].arac_ureticisi + " " + erisimListesi[k].plaka)
            break
        k = k + 1
    else:

        print("Kayıt bulunamadı")








