"""
1- Saniye Sever
Farz edelim ki elimizde 3 değişkenimiz var.
Bunlar saat, dakika ve saniye.
İstediğim şey sadece bu üç değişkeni kullanarak (başka bir değişken yaratmadan) 
toplam saniye sayısını bastırmanız.
"""
print("*** BİRİNCİ SORU CEVABI ***")
saat, dakika, saniye = 2, 30, 45
print(saat * 3600 + dakika * 60 + saniye)

"""
2- Üçgen alanı hesaplamaca
Farz edelim elimizde bir üçgen var. Ve bu üçgenin alanını hesaplamak istiyoruz.
Üçgende alan bulma formülünün istediğiniz uygulamasını kullanabilirsiniz.
Sizlerden ricam kodunuzun en fazla 3 satır sürmesi.
"""
print("*** İKİNCİ SORU CEVABI ***")
taban_uzunlugu = 5
yukseklik = 6
print(taban_uzunlugu * yukseklik / 2)

"""
3- Bozuk plak
Arkadaşlar adından da anlaşılacağı gibi herşeyi tekrar tekrar söyleyen bir print() methodu istiyorum sizlerden.
Bu konuda tek ricam eğer mümkünse değişken kullanmadan istediğiniz bir kelimeyi 4 defa bastırmanız.
Değişken kullanmadan nasıl yapacağım sorusunun cevabını internette bulabilirsiniz. 
"""
print("*** ÜÇÜNCÜ SORU CEVABI ***")
def print_four(string):
    print("{} ".format(string) * 4) 
print_four("deneme")

"""
4- Dünyanın hacmi 
Arkadaşlar dünyanın şeklinin "Geoit" değil de dümdüz küre olduğunu hayal ederek, 
hacmini hesaplamanızı rica ediyorum sizlerden.
Not: Dünyanın ekvatoral yarıçapı yaklaşık 6300 (6.371) kilometredir.
6300 alabilirsiniz.
Not2: Küre hacmi = 4/3 * pi * r^3
"""
print("*** DÖRDÜNCÜ SORU CEVABI ***")
print((4 / 3) * 3.14 * (6300 ** 3))
