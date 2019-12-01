from functions import kayıtArama
from functions import erisimListesi

f = open("testfile.txt", "r")
line = f.readline()
iter = 0
while line :                                    #Daha önce dosyada mevcut kayıtları erişim listesine getiriyoruz.
         record = line.split()                  #Böylece arama işlemini erişim listesi üzerinden yapıyoruz
         erisimListesi[iter].arac_ureticisi=record[0]
         erisimListesi[iter].arac_modeli = record[1]
         erisimListesi[iter].renk = record[2]
         erisimListesi[iter].motor_no = int(record[3])
         erisimListesi[iter].plaka = record[4]
         erisimListesi[iter].sasi_no = int(record[5])
         line = f.readline()
         iter = iter + 1



while 1 :
    print("-----Araç takip sistemine hoş geldiniz-----\n")
    print("Yapabileceğiniz işlemler :\n"
          "1-Arama\n"
          "2-Çıkış\n")


    sayi = int(input("Lütfen yapmak istediğiniz işlemi seçiniz"))
    if sayi == 1:
        aranan = int(input("Lütfen aramak istediğiniz kaydın şasi numarasını giriniz"))
        kayıtArama(aranan)                  #İçeriği functions.pyde mevcut
    elif sayi == 2:
        print("Programdan çıkılıyor")
        exit(1)
