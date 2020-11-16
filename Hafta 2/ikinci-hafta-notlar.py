
a = True
b = False

if (a):
    print ("a doğrudur")
if (b):
    print ("b doğrudur")

#if clouse - eğerli yapılar parantez içerisindeki işlemlerin çıktılarıdan altıkları sonuçlar doğrultusunda belirli kod parçacıklarını harekete geçirirler

if(True):
    print("Bu if bloğu çalışacak")
if(False):
    print("Bu if bloğu çalışmayacaktır.")
if (a == True):
    print ("a doğrudur")
if (b == True):
    print ("b doğrudur")


if(True):
    if(True):
        print("Tabii ki if bloklarını birleştirebiliriz ya daaaaa")

if (a and b):
    print ("Temel mantıksal operatörler ile (and) çalışabilirler")
    
if (a or b):
    print ("Temel mantıksal operatörler ile (or) çalışabilirler")

if (not b):
    print ("b yanlıştır ifadesini kullanırken if içerisine \"not\" önekii koyduğumuza dikkat ediniz")

if((not a and b) or (a and not b)):
    print("Biraz önce XOR işlemini temel operatöler ile oluşturduk")

if(False):
    print("False basar mı ya :) ")
else:
    print("Elimizde tabii ki sadece if yapısı yok")
    print("Else yapısı ise kendinden önce gelen if'e bakar ve eğer if bloğu çalışmaz ise else bloğu çalışır")

if(False):
    print("Nope")
elif(True):
    print("Tabii ki elimizde yine sadece else yok. Elif de var")
    print("Elif ise kendinden önce gelen if bloğu çalışmazsa çalışır ve temel olarak yapısı else'in içindeki if bloğu olarak düşünülebilir")
else:
    print("Acaba bu kime bağlı diye düşünmeyin. Kendinden önce gelen if elif'in if'i.")

print("Kafanız karışmasın. Daha bunlar başlangıç :)")
print("Arkadaşlar bir insan günlük yaşamında ortalama 35,000 karar verir.")
print("Bunların içerisinde yataktan kalkacağınız taraf, diş macununu neresinden tutacağınız, kahvaltıda ne yiyeceğiniz gibi tonlarca şey bulunabilir.")
print("Hal böyleyken kodlarınızda da buna ihtiyacınız olabilir.")
print("İşte if-elif-else size burada yardımcı oalcaktır.")
print("Örnek verelim")


boy = 1.77
kilo = 90
vki=kilo/(boy**2)


print("Verilen değişkenlere göre", boy , "uzunluğunda",kilo,"kilo bir erkeğin vücut kitle endeksi",vki,"dir")
print("Buna göre VKİ yorumları:")
if(vki > 50):
    print("Hayatta kalmak için kilo verin. VKİ 50'den yüksek.")
elif(vki > 45):
    print("Aşırı kilolusunuz")
elif(vki > 35):
    print("Sağlığınızı riske atmamak için kilo veriniz.")
elif(vki > 30):
    print("Kilolusunuz")
elif(vki > 25):
    print("Hafif kilolusunuz")
elif(vki > 20):
    print("Normal sınırlardasınız")
else:
    print("Çok zayıfsınız")

print("Boy yorumları:")

if(boy > 1.75):
    print("Türkiye ortalamasına göre uzunsunuz.")
    if(kilo > 75):
        print("Türkiye ortalamasına göre kilolusunuz.")
    elif(kilo < 67):
        print("Türkiye ortalamasına göre zayıfsınız.")
elif(boy <1.71):
    print("Türkiye ortalamasına göre kısasınız.")
    if(kilo > 75):
        print("Türkiye ortalamasına göre kilolusunuz.")
    elif(kilo < 67):
        print("Türkiye ortalamasına göre zayıfsınız.")

print("Bu veriler ortalama bir erkeğin Türkiye standartlarındak verileridir.")

print("Arkadaşlar verileri teker teker bir değişkene atama zorunluluğumuz yoktu ve asla da olmayacak.")

print("Gelelim liste yapılarının kullanımına")

list=[2,3,5,8,13,21]

print("list=[2,3,5,8,13,21] listesinin type'ı=",type(list),"list[0]=",list[0],"list[1]=",list[1])

print("Index bazlı erişim")
print("liste_adı[index_sayısı]")

print("\nlist[0]=2\n\n") # n = newline  t = tab

print("\t\tİndex bazlı erişim görselleştirmesi\n")
print("   __  __  __  __  __  __  ")
print("  | 2|| 3|| 5|| 8||13||21| ")
print("   --  --  --  --  --  --  ")
print("  |   |   |   |   |   |  |")
print("  0   1   2   3   4   5    ")

print("Liste bastırmaca")
for x in list:
    print(x)

print("Range bastırmaca")
for x in range(5):
    print(x)

print("Kim kimi buldu ?")
for x in list:
    if x==8:
        print("Buldum")
    else:
        print("Bu değil")
#break pass

print("break nedir yenir mi ?")
for i in range(8):
    if i == 5:
        print("Breakpoint")
        break
    else:
        print("Daha break yok")

print("pass nedir içilir mi ?")
for i in range(8):
    if i == 5:
        print("Breakpoint")
        break
    else:
        pass


def funcname(parameter_list):
    """
    docstring
    """
    pass

print("\nBastır Fonksiyonu\n")
def bastır(satir):
    """
    Yorum nedir nasıl yapılır
    """
    print(satir)

print("\En buyuk Fonksiyonu\n")
def en_buyuk (liste):
    temp=0
    for i in liste:
        if temp < i:
            temp = i
    print(temp)

print("\En buyuk return Fonksiyonu\n")
def en_buyuk_return (liste):
    temp=0
    for i in liste:
        if temp < i:
            temp = i
    return (temp)

print("\Kosullu Return Fonksiyonu\n")
def kosullu_return(liste):
    temp=0
    temp_bool = False
    for i in liste:
        if temp < i:
            temp = i
        if i == 4:
            temp_bool = True
    if temp_bool:
        return temp*4
    else:
        return (temp)

print("\nSpoiler Fonksiyonu\n")
def spoiler(bir_sayı):
    if not (bir_sayı.isnumeric()):
        print("Bir sayı girmeniz gerekmekte")
        return 
    if bir_sayı < 2:
        return 1
    else:
        return bir_sayı * spoiler(bir_sayı-1)
