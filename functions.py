from Car import Car_T

erisimListesi = [Car_T() for i in range(1000)]

def ekleme(sayi):                                               #Erişim listesine kayıt eklemek için oluşturulmuş bir fonksiyon


    erisimListesi[sayi].arac_ureticisi = input("Lütfen Aracınızın markasını giriniz")
    erisimListesi[sayi].arac_modeli = input("Lütfen Aracınızın modelini giriniz")
    erisimListesi[sayi].renk = input("Lütfen Aracınızın rengini giriniz")
    erisimListesi[sayi].motor_no = int(input("Lütfen Aracınızın motor no'sunu giriniz"))
    erisimListesi[sayi].plaka = input("Lütfen Aracınızın plakasını giriniz")
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






