# 3. Hafta Ödev Cevapları
#1
def mukemmel_sayi_mi(num):
    counter = 0
    for i in range(1, num):
        if num % i == 0:
            counter += i
    return counter == num

#2
for i in range(1,1001):
    if mukemmel_sayi_mi(i):
        print(i)

#3
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
    else:
        continue

#4
import sys
import random

altsinir = int(sys.argv[1])
ustsinir = int(sys.argv[2])

if altsinir > ustsinir:
    print("Alt sınırı üst sınırdan daha büyük girdiniz!")
    sys.exit()

rastgele_sayi = random.randint(altsinir, ustsinir)
deneme_sayisi = 0

while True:
    tahmin_edilen_sayi = int(input("Sayıyı giriniz: "))
    deneme_sayisi += 1
    if tahmin_edilen_sayi == rastgele_sayi:
        print("Doğru tahmin!")
        print("Sayı {} idi".format(tahmin_edilen_sayi))
        sys.exit()
    else:
        print("Yanlış tahmin!")
        
