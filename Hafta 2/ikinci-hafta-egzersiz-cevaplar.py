#1a
def carpim_toplam(liste):
    carpim = 1
    for i in liste:
        carpim *= i
    return carpim

#print(carpim_toplam([1,2,3,4]))

#1b
def toplam_toplam(liste):
    toplam = 0
    for i in liste:
        toplam += i
    return toplam
#print(toplam_toplam([1,2,3,4]))

#2
def faktoriyel(num):
    fac = 1
    for i in range(1, num+1):
        fac *= i
    return fac
#print(faktoriyel(5))

#3
def karebastir(num):
    for i in range(num + 1):
        print(i ** 2)
#karebastir(5)

#4
def adbastir(str1, str2):
    bastirilacakad = str1 + " " + str2
    kacdefa = len(str1) * len(str2)

    for i in range(kacdefa):
        print(bastirilacakad)
#adbastir("Mert", "Demir")

#5
def bu_nasıl_ucgen(kenar1,kenar2,kenar3):
    if kenar1 == kenar2 == kenar3:
        print("Eşkenar")
    elif kenar1 == kenar2 != kenar3 or kenar1 == kenar3 != kenar2 or kenar2 == kenar3 != kenar1:
        print("İkizkenar")
    else:
        print("Çeşitkenar")

#bu_nasıl_ucgen(1,3,2)

#6
def carpim_tablosu(num):
    for i in range(1, 11):
        print("{} x {} = {}".format(num,i,num*i))

#carpim_tablosu(10)


