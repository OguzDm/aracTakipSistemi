from Car import Car_T                   #Kullanılmayan import
#Kullanılan importlar
import os
import sys
from functions import ekleme
from functions import dosyaYaz
from functions import erisimListesi
from functions import kayıtArama

mevcutEleman = [0]
ilk_erisim_listesi = []



try:                               #Eğer dosya yok ise oluşturuyoruz.Zaten olan bir dosya ise hata veriyor.
    f = open("testfile.txt", "x")  #Bu hatayı except ile yakalıyoruz.
    for i in range(1000):
        print(
            "-----------------Araç Takip Sistemine Hoş Geldiniz--------------------- \n"  # Kullanıcıya bilgi verme ekranı.
            "Lütfen Yapmak İstediğiniz İşlemi Seçiniz...\n"
            "1-Yeni Kayıt\n"
            "2-Arama\n"
            "3-Silme\n"
            "4-Güncelleme\n"
            "5-Çıkış")

        secim = int(input("Lütfen seçiminizi yapınız"))

        if secim == 1:
            j = 0
            print("Eklemeyi seçtiniz işleminiz gerçekleştiriliyor...\n")
            ekleme(i)               #İçeriği functions.pyde mevcut
            mevcutEleman[0] = mevcutEleman[0] + 1

            while j < i:
                if erisimListesi[j].sasi_no == erisimListesi[i].sasi_no:  # Burada primary key olarak saşi no kullanılıyor.
                    print(
                        "Zaten mevcut olan bir kayıt girmeye çalışıyorsunuz!\n")  # Çünkü şasi no her kayıt için unique bir değerdir.
                    print("Lütfen yeni bir kayıt giriniz\n")
                    ekleme(i)                   #İçeriği functions.pyde mevcut  Kayıt için yeni bir değer alınıyor.
                    break

                j = j + 1

            dosyaYaz(i)                     #İçeriği functions.pyde mevcut


        elif secim == 2:

            print("Aramayı Seçtiniz İşleminiz Gerekleştiriliyor...\n")
            aranan = int(input("Aramak istediğiniz şasi numarasını giriniz"))
            kayıtArama(aranan)                  #İçeriği functions.pyde mevcut



        elif secim == 3:

            print("Silmeyi Seçtiniz İşleminiz Gerçekleştiriliyor...\n")
            silinecek_sasi_no = int(input("Silmek istediğiniz kaydın şasi numarasını giriniz"))
            index = 0
            while index < len(ilk_erisim_listesi):
                if ilk_erisim_listesi[index].sasi_no == silinecek_sasi_no:
                    # Kayidi erisim listesinden sil
                    try:
                        erisimListesi.remove(ilk_erisim_listesi[index])
                    except:
                        print("\nSilmeye calistiginiz arac kayitlarimizda bulunmamaktadir.\n")
                        break

                    with open("testfile.txt", "r") as file:
                        lines = file.readlines()

                    # Silinecek olan arac basina '@' isareti konularak isaretlendi
                    if len(lines) > index:
                        # lines[index] = "".join((lines[index], " @"))
                        lines[index] = lines[index].replace("\n", " @\n")

                    # Dosyaya isaretli sekilde kaydediliyor. Cikis yapilirken '@' isaretine sahip olunanlar silinecek
                    with open("testfile.txt", "w") as file:
                        file.writelines(lines)

                    break
                index += 1
            if index.__eq__(len(ilk_erisim_listesi)):
                print("\nVerdigin sasi numarasındaki arac kayitlarimizda bulunmamaktadir.\n")





        elif secim == 4:

            k = 0
            l = 0
            print("Güncellemeyi Seçtiniz İşleminiz Gerekleştiriliyor...\n")

            aranan = int(input("Güncellemek istediğiniz kaydın şasi numarasını giriniz"))
            while k < len(erisimListesi):
                if erisimListesi[k].sasi_no == aranan:
                    ekleme(k)                             #Bulduğumuz kayıdı güncelliyoruz.
                    f = open("testfile.txt", "w")               #Dosyanın içeriğini,
                    f.close()                                   #temizliyoruz.
                    while l < mevcutEleman[0]: #Dosyanın içeriğini güncellenmiş kayıt ile tekrar erişim listesinden yazıyoruz.
                        dosyaYaz(l)                     #İçeriği functions.pyde mevcut
                        l = l + 1
                    break
                k = k + 1

            else:
                print("Kayıt bulunamadı")
        elif secim == 5:
            print("Programdan çıkılıyor...")

            # Programdan cikiliyor
            # '@' ile isaretli olan araclari sil
            with open("testfile.txt", "r") as file:
                lines = file.readlines()

            # İsaretli olmayan satirlari bul ve result listesine ekle
            result = []
            for line in lines:
                if not line.__contains__('@'):
                    result.append(line)

            # result listesini dosyaya yazdir
            with open("testfile.txt", "w") as file:
                file.writelines(result)

            exit(1)
        #os.execl(sys.executable, sys.executable, *sys.argv)  # Program eğer  çıkış yapmadan biterse.
        # Yeniden başlatılıyor.

            

except FileExistsError:                     #Eğer dosya mevcut ise except ile yakaladık ve programımız buraya giriyor.
    liste=[0]
    f = open("testfile.txt", "r")
    bosmu = f.read(1)

    if bosmu != "\n":               #Dosya mevcut ancak boş mu diyerek kontrol ediyoruz.
        f = open("testfile.txt", "r+")
        line = f.readline()
        iter = 0
        while line :        #Dosyadaki yazılı olan kayıtları erişim listesine atıyoruz.
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
            mevcutEleman = [liste[0]]
        ilk_erisim_listesi = erisimListesi.copy()



    for i in range(liste[0],1000):
        print(
            "-----------------Araç Takip Sistemine Hoş Geldiniz--------------------- \n"  # Kullanıcıya bilgi verme ekranı.
            "Lütfen Yapmak İstediğiniz İşlemi Seçiniz...\n"
            "1-Yeni Kayıt\n"
            "2-Arama\n"
            "3-Silme\n"
            "4-Güncelleme\n"
            "5-Çıkış\n")

        secim = int(input("Lütfen seçiminizi yapınız"))

        if secim == 1:
            j = 0
            print("Eklemeyi seçtiniz işleminiz gerçekleştiriliyor...\n")
            ekleme(i)                           #İçeriği functions.pyde mevcut
            mevcutEleman[0] = mevcutEleman[0] + 1

            while (j) < (i):
                if erisimListesi[j].sasi_no == erisimListesi[i].sasi_no:  # Burada primary key olarak saşi no kullanılıyor.
                    print(
                        "Zaten mevcut olan bir kayıt girmeye çalışıyorsunuz!\n")  # Çünkü şasi no her kayıt için unique bir değerdir.
                    print("Lütfen yeni bir kayıt giriniz\n")
                    ekleme(i)           #İçeriği functions.pyde mevcut

                    break

                j = j + 1

            dosyaYaz(i)



        elif secim == 2:

            print("Aramayı Seçtiniz İşleminiz Gerekleştiriliyor...\n")
            aranan = int(input("Aramak istediğiniz kaydın şasi numarasını giriniz"))
            kayıtArama(aranan)      #İçeriği functions.pyde mevcut

        elif secim == 3:

            print("Silmeyi Seçtiniz İşleminiz Gerçekleştiriliyor...\n")
            silinecek_sasi_no = int(input("Silmek istediğiniz kaydın şasi numarasını giriniz"))
            index = 0
            while index < len(ilk_erisim_listesi):
                if ilk_erisim_listesi[index].sasi_no == silinecek_sasi_no:
                    # Kayidi erisim listesinden sil
                    try:
                        erisimListesi.remove(ilk_erisim_listesi[index])
                    except:
                        print("\nSilmeye calistiginiz arac kayitlarimizda bulunmamaktadir.\n")
                        break

                    with open("testfile.txt", "r") as file:
                        lines = file.readlines()

                    # Silinecek olan arac basina '@' isareti konularak isaretlendi
                    if len(lines) > index:
                        # lines[index] = "".join((lines[index], " @"))
                        lines[index] = lines[index].replace("\n", " @\n")

                    # Dosyaya isaretli sekilde kaydediliyor. Cikis yapilirken '@' isaretine sahip olunanlar silinecek
                    with open("testfile.txt", "w") as file:
                        file.writelines(lines)

                    break
                index += 1
            if index.__eq__(len(ilk_erisim_listesi)):
                print("\nVerdigin sasi numarasındaki arac kayitlarimizda bulunmamaktadir.\n")


        elif secim == 4:
            k = 0
            l = 0
            print("Güncellemeyi Seçtiniz İşleminiz Gerekleştiriliyor...\n")
            aranan = int(input("Güncellemek istediğiniz kaydın şasi numarasını giriniz"))
            while k < len(erisimListesi):
                if erisimListesi[k].sasi_no == aranan:
                    ekleme(k)           #İçeriği functions.pyde mevcut       Bulduğumuz kayıdı güncelliyoruz.
                    f=open("testfile.txt", "w")                 #Dosyanın içeriğini temizliyoruz.
                    f.close()                                   #''''''''''''''''''''''''''''''''
                    while l < mevcutEleman[0]:
                        dosyaYaz(l)                             #Dosyayı güncellenmiş veri ile birlikte
                        l = l + 1                               #Yeniden oluşturuyoruz.
                    break
                k = k + 1
            else:

                print("Kayıt bulunamadı")



        elif secim == 5:
            print("Programdan çıkılıyor...")

            # Programdan cikiliyor
            # '@' ile isaretli olan araclari sil
            with open("testfile.txt", "r") as file:
                lines = file.readlines()

            # İsaretli olmayan satirlari bul ve result listesine ekle
            result = []
            for line in lines:
                if not line.__contains__('@'):
                    result.append(line)

            # result listesini dosyaya yazdir
            with open("testfile.txt", "w") as file:
                file.writelines(result)

            exit(1)
os.execl(sys.executable, sys.executable, *sys.argv) #Program eğer  çıkış yapmadan biterse.
                                                            #Yeniden başlatılıyor.

