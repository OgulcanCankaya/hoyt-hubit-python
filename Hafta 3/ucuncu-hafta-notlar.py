# ********** GELİŞMİŞ FOR LOOP İŞLEMLERİ **********
# Matrisimizi oluşturalım

print("Nested for loop işlemi")
matris = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
for row in matris:
    for col in row:
        print("%d " % col,end="")
    print()
    
# Range fonksiyonumuz ile atlaya atlaya sayılar arasında gezinebiliriz

print("Range atlama işlemleri")
# 2 2 atlar
for i in range(0,20,2):
    print(i)

# 3 3 atlar
for j in range(0,20,3):
    print(j)

# ********** MODÜL IMPORTING İŞLEMİ **********
# Modülleri import keyi ile projemize import ediyoruz
import math

# Math modülü gerekli bazı matematik işlemlerini içerir
print("Modül importing")
num1 = math.pow(10,2)
num2 = math.factorial(10)
print("num1: %d, num2: %d" % (num1, num2)) # Başka bir string formatting biçimi

# Math modülünü mth olarak çağırabiliriz
import math as mth

# Hypot fonksiyonunu math. veya mth. olarak çağırmamıza gerek yok, hatta adını da değiştirdik
from math import hypot as myhypot

# Tüm fonksiyonları import ettik
from math import *


# ********** WHILE DÖNGÜSÜ **********
# For döngüsünün bir değişiği

#num1 = 100'dü
print("While döngüsü")
while num1 > 90:
    print(num1)
    num1 -=1

# num1 sayısı gerekli koşulları sağlamaya devam ettikçe, while döngüsü çalışmaya devam edecek
# Loopları break ile kesebiliriz, continue ile bir yeri atlamasını sağlayabiliriz

print("continue örneği")
a = 0
while a < 10:
    if a == 7:
        a += 1
        continue
    else:
        print(a)
        a += 1

print("break örneği")
b = 0
while b < 10:
    if b == 5:
        break
    else:
        print(b)
        b += 1


# While döngüsü, ona söylediğimiz koşul True olduğu sürece devam eder
# Eğer True verirsek, sonsuza kadar devam eder.
# Peki bunu nasıl durduracağız?

print("break örneği 2")
while True:
    inp = input("Çıkmak için q tuşuna basın, işlemler için 1, 2 veya 3 e basın: ")
    if inp == "q":
        print("Görüşmek üzere!")
        break
    elif inp == "1":
        print("1 e basıldı")
    elif inp == "2":
        print("2 e basıldı")
    elif inp == "3":
        print("3 e basıldı")    

# ********** GELİŞMİŞ LİSTE İŞLEMLERİ **********
# string'lerin türleri liste olmasa da, temelde bunlar karakter içeren listelerdir.
# Liste manipülasyon işlemlerini burada da uygulayabiliriz

print("Gelişmiş liste işlemleri")
belediye = "İstanbul Büyükşehir Belediyesi"
print(belediye[0])
print(belediye[0:8])
print(belediye[0:8:2])
print(belediye[::3])

# Hatta for ile içinde gezinebiliriz
for i in belediye:
    print(i, end="")

# len fonksiyonu ile listenin boyutunu hesaplayabiliriz
diller = ["İngilizce", "Fransızca", "Türkçe", "İtalyanca", "İspanyolca"]
print(len(diller))

# split kullanımı, sonucu liste olacak
isimler = "ahmet mehmet cem"
print(isimler.split())

# ", " aralarını birbirinden ayırabiliyoruz
isimler = "elma, armut, çilek"
print(isimler.split(", "))


# Bu listedeki öğeleri numaralandırmak da mümkün
meyveler = ["elma", "armut", "çilek", "kiraz"]
for öğe_sırası in range(len(meyveler)):
    print("{}. {}".format(öğe_sırası, meyveler[öğe_sırası]))

# veya enumerate() fonksiyonunu kullanarak şöyle bir şey de yazabiliriz
for sıra, öğe in enumerate(meyveler, 1):
    print("{}. {}".format(sıra, öğe))

# listeyi ters çevirebiliriz
print(meyveler[::-1])

# doğal olarak stringi de ters çevirebiliriz
print(belediye[::-1])

# matrisimizi tekrar ele alalım
matris = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

# 2. row 3. columndaki öğeyi printleyelim
print(matris[2-1][3-1]) # -1 olmasının sebebi indexin 0 dan başlaması

# string değiştirelim
deneme_string = "deneme"
deneme_string = "D" + deneme_string[1:]
print(deneme_string)

# Peki listeye nasıl eleman ekleriz?
liste = [2, 4, 5, 7]
liste += [8]
print(liste)

liste.append(9)
print(liste)

# Listedeki tüm elemanları silme
liste2 = [1, 2, 3, 4, 5]
liste2.clear()
print(liste2)

# Listedeki bir elemanın listede kaç tane olduğunu bulmak
liste3 = [1, 2, 3, 4, 5, 5, 6, 7, 8]
print(liste3.count(5))

# Listedeki bir elemanın indexini bulmak
print(liste3.index(2))
print(liste3.index(5)) # İlk karşılaştığı occurence ı bastırır

# Listenin sonundan eleman çıkartmak
print(liste3)
liste3.pop()
print(liste3)

# İki listeyi extend ile birleştirmek
liste1 = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]
liste1.extend(liste2)
print(liste1)

# Listenin belirli indexine eleman eklemek
liste1 = [1, 2, 3, 4]
liste1.insert(2, 'new')
print(liste1)

# Listeden eleman silme
liste1.remove('new')
print(liste1)

# Listeyi reverse ile ters çevirme
liste1.reverse()
print(liste1)


# ********** ARGV İŞLEMLERİ **********
# Program çalışmadan önce bazı argümanları vermeye yarar

import sys

def çık():
    print('Çıkılıyor...')

if len(sys.argv) < 2:
    print('Gerekli parametreleri girmediniz!')
    çık()

elif len(sys.argv) > 2:
    print('Çok fazla parametre girdiniz!')
    çık()

elif sys.argv[1] in ['-v', '-V']:
    print('Program sürümü: 0.8')

else:
    mesaj = 'Girdiğiniz parametre ({}) anlaşılamadı!'
    print(mesaj.format(sys.argv[1]))
    çık()

# ********** İNCELİKLER **********
# Fonksiyon birden fazla şeyi return edebilir

def hesapla(a,b,c):
    return (a + b + c), (a * b * c)

toplam, carpim = hesapla(2,3,4)
print(toplam, carpim)

# string'i for loop ve 1 değişkenle reverse etmek
string = "ters düz edilecek"
new_string = ""
for i in reversed(string):
    new_string += i
print(new_string)

# sayı asal mıdır
def asalmi(num):
    sayi_asal = True
    for i in range(2, num):
        if num % i == 0:
            sayi_asal = False
            break
    if sayi_asal:
        return "Sayı asal bir sayı"
    else:
        return "Sayı asal bir sayı değil"

