# aracTakipSistemi
Basit Araç Takip Sistemi

Tanım: Basit araç takip sistemi gerçekleştirilecektir. Kullanıcı bir aracı, marka/model,
renk, plaka numarası, şasi ve motor numarasına göre arayabilecektir. Aynı zamanda
sistem yöneticisi, bir aracın kaydını ekleyebilecek, silebilecek ve günceleyebilecektir.
a) Her bir kayıt 6 alandan oluşacak.
- Araç markası
- Araç modeli
- Araç rengi
- Plaka No
- Motor_No
- Şasi_No
Sabit uzunlukta kayıtlar kullanılacaktır. Örnek bir kaydın yapısı C’de aşağıdaki gibi
olacaktır. Benzeri yapı Python projesi için de oluşturulacaktır.
typedef struct T_Arac {
char arac_ureticisi [x];
char arac_modeli[x];
char renk[x];
int motor_no;
int sasi_no;
char plaka[x];
} Arac;
x: Boyut bilgisi proje ekibi tarafından belirlenecektir.
b) Ekleme, silme ve güncelleme işlemleri gerçekleştirilecek. Bu işlemler sırasında
aşağıdaki şekilde gerçekleştirilecektir :
- Bir kayıt eklerken öncelikle “Erişim Listesine” bakılacak, gerekli düzenlemeler
“Erişim Listesi” üzerinde gerçekleştirilecek ve daha sonra kayıt eklenecektir.
- Eğer eklenecek kayıt daha önceden mevcutsa, bu kayıt dosyaya yazılmayacaktır.
- Kayıt silme işleminde kayıt, hemen fiziksel olarak dosyadan silnmeyecektir. Dosya
üzerine bir belirteç konulacak ve ardından gerekli düzenlemeler “Erişim Listesi”
üzerinde yapıldıktan sonra silme işlemi gerçekleştirilecektir.
- Silinecek kayıt mevcut değilse, ekranda uyarı mesejı görüntülecektir.
