# Python'da her şey bir nesnedir!

# Nesneler şu şekilde tanımlanır (Genel nesne tanımı)
class Çalışan_basit():
    def __init__(self):
        self.kabiliyetleri = []
        print(self.kabiliyetleri)

    kabiliyetleri = []
    unvanı = 'işçi'
    maaşı = 1500
    memleketi = ''
    doğum_tarihi = ''

# Nesne nitelikleri şu şekilde bastırılır
print(Çalışan_basit.maaşı)
print(Çalışan_basit.memleketi)
print(Çalışan_basit.doğum_tarihi)

# Şu şekilde yeni özellikler eklenir (Ama bu genel nesne tanımına eklenir)
Çalışan_basit.isim = 'Ahmet'
Çalışan_basit.yaş = 40

# Şurada, mehmet değişkeni yeni bir nesne oldu (Bu bir nesne örneği)
mehmet = Çalışan_basit()

# Birden fazla çalışan oluşturabiliriz
ahmet = Çalışan_basit()
ayşe = Çalışan_basit()

# Bu çalışan nesne tanımını import çalışan diyerek başka yerde import edebiliriz

# mehmetin memleketini değiştirelim
mehmet.memleketi = "Kastamonu"

# ahmete kabiliyet ekleyelim
ahmet.kabiliyetleri.append('prezantabl')

# init fonksiyonu bir çalışan oluşturulduğu anda ilk olarak çağırılır
# init fonksiyonu constructor bir fonksiyondur
# init fonksiyonu oluşturulmazsa boş olarak kendisi otomatik olarak oluşur
# self kelimesi nesnenin kendisini çağırmamıza yarar, mecburidir.

# sınıf niteliğine erişmek için
# sınıf adını kullanıyoruz
print(Çalışan_basit.kabiliyetleri)

# örnek niteliğine erişmek için
# örnek adını kullanıyoruz
ahmet = Çalışan_basit()
print(ahmet.kabiliyetleri)

# fonksiyon dışında selfe ulaşamazsınız
# çünkü self kelimesi ancak ve ancak, 
# içinde geçtiği fonksiyonun parametre listesinde ilk sırada kullanıldığında anlam kazanır.

class Çalışan():
    personel = []

    """
    Bu fonksiyonun özelliği, sınıfın örneklenmesi ile birlikte otomatik olarak 
    çalıştırılacak olmasıdır. Biz burada, self.isim ve self.kabiliyetleri adlı 
    iki adet örnek niteliği tanımladık. Bu örnek niteliklerine sınıfımızın her 
    tarafından erişebileceğiz.
    """
    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()

    """
    Burada, bir sınıf niteliği olan personel değişkenine nasıl eriştiğimize çok 
    dikkat etmenizi istiyorum. Daha önce de söylediğimiz gibi, sınıf niteliklerine 
    sınıf dışındayken örnekler üzerinden erişebiliyoruz. self kelimesi, bir sınıfın 
    örneklerini temsil ettiği için, bir sınıf niteliğine sınıf içinden erişmemiz 
    gerektiğinde self kelimesini kullanabiliriz.

    Ayrıca bu fonksiyonda, bir örnek niteliği olan self.isim değişkenine de erişebiliyor 
    olduğumuza dikkat edin. Unutmayın, self sınıfların çok önemli bir öğesidir. Bu öğeyi 
    kullanarak hem örnek niteliklerine, hem sınıf niteliklerine, hem de örnek metotlarına 
    ulaşabiliyoruz. Tanımladığımız bu personele_ekle() adlı örnek metodunu __init__() 
    fonksiyonu içinden self.personele_ekle() kodu ile (yani yine self kelimesini kullanarak) ,
    çağırdığımızı hatırlıyorsunuz.
    """
    
    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    def personeli_görüntüle(self):
        print('Personel listesi:')
        for kişi in self.personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)


ç1 = Çalışan('Ahmet')
# Ahmet adlı kişi personele eklendi

ç2 = Çalışan('Mehmet')
# Mehmet adlı kişi personele eklendi

ç1.isim
# 'Ahmet'

ç2.isim
# 'Mehmet'

ç1.isim = 'Mahmut'
ç1.personel[0] = 'Mahmut'

# Böylece ilk çalışanın ismini ‘Mahmut’ olarak değiştirdik:

ç1.isim
# 'Mahmut'

ç1.personel
# ['Mahmut', 'Mehmet']

ç1.kabiliyet_ekle('prezantabl')
ç1.kabiliyet_ekle('konuşkan')

ç1.kabiliyetleri_görüntüle()
"""
Mahmut adlı kişinin kabiliyetleri:
prezantabl
konuşkan
"""

ç2.kabiliyet_ekle('girişken')
ç2.kabiliyetleri_görüntüle()
"""
Mehmet adlı kişinin kabiliyetleri:
girişken
"""

"""
Gördüğünüz gibi, bir sınıf örneğine eklediğimiz kabiliyet öteki sınıf örneklerine 
karışmıyor. Bu, örnek niteliklerinin sınıf niteliklerinden önemli bir farkıdır. 
Zira sınıf nitelikleri bir sınıfın bütün örnekleri tarafından paylaşılır. Ama 
örnek nitelikleri her bir örneğe özgüdür.
"""

"""
 Eğer ilgili sınıf niteliği; karakter dizisi, demet ve sayı gibi değiştirilemeyen 
 (immutable) bir veri tipi ise bu sınıf niteliği üzerinde zaten değişiklik yapamazsınız. 
 Yaptığınız şey ancak ilgili sınıf niteliğini yeniden tanımlamak olacaktır. Ancak eğer 
 sınıf niteliği, liste, sözlük ve küme gibi değiştirilebilir (mutable) bir veri tipi ise 
 bu nitelik üzerinde yapacağınız değişiklikler bütün sınıf örneklerine yansıyacaktır. 
 Yazdığınız program açısından bu özellik arzu ettiğiniz bir şey olabilir veya olmayabilir. 
 Önemli olan, sınıf niteliklerinin bu özelliğinin farkında olmanız ve kodlarınızı bu bilgi 
 çerçevesinde yazmanızdır.
"""

"""
Sınıf örneklerimizin herhangi biri üzerinden personel listesine de 
ulaşabileceğimizi biliyoruz:
"""

ç1.personeli_görüntüle()
"""
Personel listesi:
Mahmut
Mehmet
"""

ç2.personeli_görüntüle()
"""
Personel listesi:
Mahmut
Mehmet
"""

"""
Sınıf niteliklerinin özelliği, o sınıfın bütün örnekleri tarafından paylaşılıyor 
olmasıdır. Yani herhangi bir örneğin bu nitelik üzerinde yaptığı değişiklik, 
öteki örneklere de yansıyacaktır. Burada personel, hepsi tarafından paylaşılır.
"""

print(Çalışan.personel)
# ['Mahmut', 'Mehmet']
