# Kaynak: python-istihza.yazbel.com

# TRY-EXCEPT-RAISE-ASSERT
# Python’da hata yakalama işlemleri için try... except... bloklarından yararlanılır.
ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError:
    print("Lütfen sadece sayı girin!")
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!")
except (ValueError, ZeroDivisionError):
    print("Bir hata oluştu!")
except ValueError as hata:
    print(hata)
except (ValueError, ZeroDivisionError) as hata:
    print("Bir hata oluştu!")
    print("orijinal hata mesajı: ", hata)
finally:
    print("Yine de çalıştım")

"""
Try-except genel olarak şu şekilde kullanılır:

try:
    hata verebileceğini bildiğimiz kodlar
except HataAdı1:
    hata durumunda yapılacak işlem
except HataAdı2:
    hata durumunda yapılacak işlem
except HataAdı3:
    hata durumunda yapılacak işlem
...
...
...
finally:
    ...hata olsa da olmasa da yapılması gerekenler...

"""

# Exceptionlar: https://docs.python.org/3/library/exceptions.html

# raise
bölünen = int(input("bölünecek sayı: "))

# Örnek 1
if bölünen == 23:
    # Bölünen 23 e eşitse program hata verecek
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

bölen = int(input("bölen sayı: "))
print(bölünen/bölen)

# Örnek 2
tr_karakter = "şçğüöıİ"
parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass

print("Parola kabul edildi!")

# assert
giriş = input("Merhaba! Adın ne? ")
assert len(giriş) != 0 , "İsim bölümü boş."
print("Hoşgeldiniz.")

# giriş stringinin uzunluğunu 0 olarak iddia ediyoruz.
# assert yanlış çıkarsa program AssertionError verir.


# STRING METODLARI
string1 = "elma"
string1.replace("e", "E")
# string1 = "Elma"

# Cümle cümle bölüyor
metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""

print(metin.splitlines())

# Hepsini küçük yapar
isim = "Deneme Denek"
isim = isim.lower()
# isim = "deneme denek"

# Hepsini büyük yapar
isim = "Deneme Denek"
isim = isim.upper()
# isim = "DENEME DENEK"

şehir = "Ankara"
# şehir.islower() -> False

şehir2 = "uşak"
# şehir2.islower() -> True

şehir3 = "BİNGÖL"
# şehir3.isupper() -> True

şehir4 = "Bursa"
# şehir3.isupper() -> False

meyve1 = "Elma"
# meyve1.endswith("a") -> True
# meyve1.startswith("E") -> True

şehir5 = "ankara"
şehir5 = şehir5.capitalize()
# şehir5 = "Ankara"

belediye = "istanbul büyükşehir belediyesi"
belediye = belediye.title()
# belediye = "Istanbul Büyükşehir Belediyesi"

belediye = "Istanbul Büyükşehir Belediyesi"
belediye = belediye.swapcase()
# belediye = "iSTANBUL bUYUKSEHIR bELEDIYESI"

deneme = "        Deneme      "
deneme = deneme.lstrip()
# deneme = "Deneme      "
deneme = deneme.rstrip()
# deneme = "Deneme"
# *** deneme.lstrip().rstrip() = deneme.strip() ***

bölünmemiş = "Beşiktaş Jimnastik Kulübü"
bölünmüş = bölünmemiş.split()
# bölünmüş = ['Beşiktaş', 'Jimnastik', 'Kulübü']

oluşturulan_bölünmemiş = " ".join(bölünmüş) # " " olan şey birleştirme karakteridir.
# oluşturulan_bölünmemiş = 'Beşiktaş Jimnastik Kulübü'

şehir = "Kahramanmaraş"
# şehir.count("a") = 5
# “Kahramanmaraş” adlı karakter dizisi içinde toplam 5 adet “a” karakteri geçiyor.

pyt = "python"
# pyt.index("p") -> 0
# pyt.index("n") -> 5


şehir = "adana"
# şehir.index("a") -> 0
# şehir.rindex("a") -> 4
# şehir.find("a") -> 0
# şehir.rfind("a") -> 4

"""
index() ve rindex() metotları karakter dizisi içindeki karakteri sorgularken, eğer o 
karakteri bulamazsa bir ValueError hatası verir. Ama find() ve rfind() metotları 
böyle bir durumda -1 çıktısı verir.
"""

a = "mehmet"
# a.isalpha() -> True

b = "k3zb6n"
# b.isalpha() -> False

a = "12345"
# a.isdigit() -> True

b = "123445b"
# b.isdigit() -> False

a = "123abc"
# a.isalnum() -> True

b = "123abc>"
# b.isalnum() -> False

a = "123"
# a.isdecimal() -> True

b = "123.3"
# b.isdecimal() -> False

"12".isnumeric() # True
"dasd".isnumeric() # False

# *** TUPLELAR (DEMETLER) *** 
# Tıpkı listeler gibi, farklı veri tiplerini içinde barındıran kapsayıcı bir veri tipidir.

demet = ("ahmet", "mehmet", 23, 45)
tuple(["ahmet", "mehmet", 34, 45]) # ('ahmet', 'mehmet', 34, 45)
tuple('abcdefg') # ('a', 'b', 'c', 'd', 'e', 'f', 'g')

demet = ('ahmet') # Bu string
demet = ('ahmet',) # Bu tuple

demet = ('elma', 'armut', 'kiraz')
demet[0] # 'elma'
demet[-1] # 'kiraz'
demet[:2] # ('elma', 'armut')

# Tuplelar bir kere tanımlandıktan sonra değiştirilemez.
demet = ('elma', 'armut', 'kiraz')
demet[0] = 'karpuz'
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
"""

demet = ("elma", "armut", "çilek")
demet.index("elma") # 0

demet = ("elma", "armut", "elma", "çilek")
demet.count("elma") # 2


# DICTIONARYLER
sözlük = {}
type(sözlük) # <class 'dict'>

kelimeler = {"kitap": "book", "bilgisayar": "computer"}

sözlük = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming",
          "dil"        : "language",
          "defter"     : "notebook"}

print(sözlük["kitap"]) # "book"
print(sözlük["bilgisayar"]) # "computer"

sözlük["bir meyve"] = "muz" # "bir meyve": "muz" key-value pairini ekledik










