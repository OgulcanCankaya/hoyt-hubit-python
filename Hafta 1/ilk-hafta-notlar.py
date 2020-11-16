print("Merhaba Dünya !")

# Değişken tanımlama
x = 5
y = 4

# Temel matematiksel işlemler - integer değerlerde
z = x + y    #Toplama
z = x - y    #Çıkarma
z = x / y    #Bölme
z = x // y   #TAM bölme
z = x ** y   #Üslü işlemi 
z = x % y    #Mod alma öperatörü (17:30 dersinde atlamışım)

# Strings - harf listeleri
a = "Bu bir satırdır."
b = "Bu da diğer satır"

# Arkadaşlar, derste de 1 cümle ile ağzımdan kaçırdığım gibi stringler aslında karakterlerin listesidir
c = a + b
# c = "Bu bir satırdır.Bu da diğer satır"

# Float - devirli sayılar
pi = 3.14
r = 5
daire_alanı = pi * r * r
# Çıkan sonuç aslında float formatına dönüştürülmüş 2 integer'in float bir sayıyla çarpılmasıdır ve ondalıklı sonuç verir

daire_alanı = pi * (r ** 2)
# daire_alanı hesaplamasında yukarıdaki şekil de kullanılabilir

# Değişken tiplerimiz şimdilik int, str ve float şeklinde. 
# Peki bu değişkenleri nasıl birbirine dönüştürürüz ?

#   TYPE   CASTING
z = int("12")
type(z) # <class 'int'>

c = a + str(12)
type(c) # <class 'str'>

z = float(5)
type(z) # <class 'float'>

# BONUS - Yuvarlak hesap
z = round(4.5) # 4.5 ve yukarısını 5'e,  4.49 ve aşağısını 4'e yuvarlar

# Değişken isminde : ; , . / ' # [ ] ! " $ % ^ & * ( ) { } karakterleri ve boşluk karakteri kullanılamaz. Ancak _ kullanılabilir ve
# Değişken isminin ilk karakteri harf olmalıdır

# Python bir programlama dili olarak, her dil gibi belirli kurallar çerçevesinde ilerler.
# Bu kurallardan biri de yukarıdaki gibi değişken isimlerini alakadar eden kurallardır.

#Şimdiye kadar farketmiş olduğunuzu düşündüğüm bir başka kural da değişken atamalarında ve print 
#methodu kullanımlarımızda hep satır başında boşluksuz başlıyoruz. Python indent (boşluk) yapısı ile hareket eden bir programlama dilidir.
