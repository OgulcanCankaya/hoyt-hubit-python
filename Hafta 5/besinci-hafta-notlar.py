# Kaynak: python-istihza.yazbel.com

# SÖZLÜKLER (DICTIONARIES)
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

telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                   "mehmet su": "0543 543 42 42",
                   "seda naz" : "0533 533 33 33",
                   "eda ala"  : "0212 212 12 12"}
cevap = "{} adlı kişinin telefon numarası: {}"
kişi="ahmet öz"
print(cevap.format(kişi, telefon_defteri[kişi]))
#"ahmet öz adlı kişinin telefon numarası 0532 532 32 32"

# Sözlükler içinde liste de olabilir
sözlük = {"Ahmet Özkoparan": ["İstanbul", "Öğretmen", 34],
          "Mehmet Yağız"   : ["Adana", "Mühendis", 40],
          "Seda Bayrak"    : ["İskenderun", "Doktor", 30]}

# Sözlükler içinde sözlük de olabilir
kişiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                               "Meslek"  : "Öğretmen",
                               "Yaş"     : 34},

           "Mehmet Yağız"   : {"Memleket": "Adana",
                               "Meslek"  : "Mühendis",
                               "Yaş"     : 40},

           "Seda Bayrak"    : {"Memleket": "İskenderun",
                               "Meslek"  : "Doktor",
                               "Yaş"     : 30}}

print(kişiler["Mehmet Yağız"]["Memleket"])
print(kişiler["Seda Bayrak"]["Yaş"])
print(kişiler["Ahmet Özkoparan"]["Meslek"])

sözlük = {'elma': 'apple',
        'armut': 'pear',
        'çilek': 'strawberry'}
#print(sözlük[0]) # Hata verir.

# Sözlüklerde herhangi bir sıra yoktur. Sıralı sözlük -> OrderedDict
# https://docs.python.org/3/library/collections.html#collections.OrderedDict


sözlük = {}
sözlük["Ahmet"] = "Adana" # Ahmet: Adana key-value pairi eklendi

# Kafana göre ekle, fark etmez (değer (value) kısımları)
sözlük = {}
sözlük = {'a': 1}
sözlük = {'a': (1,2,3)}
sözlük = {'a': 'kardiz'}
sözlük = {'a': [1,2,3]}

"""
Anahtar olarak immutable olmalı, mesela:
Demetler
Sayılar
Karakter Dizileri


Bunlar anahtar olarak kullanılamaz:
Listeler
Sözlükler
"""

notlar = {'Seda': 98, 'Ege': 95, 'Mehmet': 77, 
        'Zeynep': 100, 'Deniz': 95, 'Ahmet': 45}
notlar["Ahmet"] = 65 # 'Ahmet': 65 eklendi


sözlük = {"a": 0,
           "b": 1,
           "c": 2,
           "d": 3}

print(sözlük.keys()) 
# dict_keys(['b', 'c', 'a', 'd'])
liste = list(sözlük.keys())
print(liste) # ['b', 'c', 'a', 'd']

print(sözlük.values()) 
# dict_values([1, 2, 0, 3])
# Aynı üstteki gibi bu values()'in döndüğü şey de liste-demet-string'e dönüşür.

print(sözlük.items())
# dict_items([('a', 0), ('c', 2), ('b', 1)])

# Sözlük üzerinde for ile bu şekilde dönebiliriz
for anahtar, değer in sözlük.items():
    print("{} = {}".format(anahtar, değer))

lig = {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu",
        "üçüncü": "Adana Gençlerbirliği"}

# Sözlük içini bu şekilde boşaltırız
lig.clear()
print(lig)
# {}

elemanlar = "Ahmet", "Mehmet", "Can"
adresler = dict.fromkeys(elemanlar, "Kadıköy")
print(adresler)
# {'Ahmet': 'Kadıköy', 'Mehmet': 'Kadıköy', 'Can': 'Kadıköy'}

sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye"),
"içecekler": ("su", "kola", "ayran")}
sepet.pop("meyveler")
sepet.popitem() # Eklenen son itemi kaldırır

stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}
yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}
stok.update(yeni_stok)
print(stok)
# {'peynir': 8, 'elma': 3, 'sucuk': 6, 'sosis': 4, 'armut': 20}

# SÖZLÜKLER İLE FİLE/IO
# file object = open(file_name, access_mode, buffering_mode_or_size)
# access_mod = r, rb, r+, rb+, w, wb, wb+, a, a+, ab+ ...
# r = read , w = write, a= append, b= bytes, + = more,MORE
# r-> pointer at the begining, w -> overwrites if exists, creates if not found, 
# a -> pointer at the end, creates a file if not found
# Tüm dosyaya erişim kipleri için: https://python-istihza.yazbel.com/temel_dosya_islemleri.html#dosyaya-erisme-kipleri

fo = open("dna","r")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
print ("Softspace flag : ", fo.write_through)

fo.close()

fo=open("yazyazyaz.txt","w+")

fo.write("Ne yazsam ki sana?\n")
fo.close()

ap=open("yazyazyaz.txt","a")
ap.write("sonlara doğru :)")

ap.close()

fo=open("yazyazyaz.txt","r")
satır=fo.readline()
print(satır)

# Peki otomatik olarak bütün satırları okumak isteseydik?
fo.close()
fo=open("yazyazyaz.txt","r")
satırlar=fo.readlines()
for i in satırlar:
    print(i.upper())

fo.close()


#EGZERSİZ
#sozluk dosyasında okunması gereken türkçe-ingilizce kelimeler var
#bu dosyayı okuyup var olan kelimeleri sorabileceğiniz bir kod yazın
# çalıştırma: python translate.py kelime

fo = open ("sozluk.txt","r")
ing2tr={}

#sozluk okunup hazırlandı
for i in fo.readlines():
    key = i.split("=")[0]
    value = i.split("=")[1]
    ing2tr[key]=value

aranacak = input("kelime alalım ? :")

if aranacak in ing2tr:
    print(ing2tr[aranacak])
else:
    print("aradığınızı bulamadık :(")

#peki bu sözlüğün ingilizce veya türkçe kelime araması farketmeseydi ?
# tr2ing={v: k for k, v in ing2tr.items()}

tr2ing={}

for k,v in ing2tr.items():
    tr2ing[v]=k

# KÜMELER (SETS)
boş_küme = set()
küme = set(["elma", "armut", "kebap"])

demet = ("elma", "armut", "kebap")
küme = set(demet)

str1 = "Python Programlama Dili"
küme = set(str1)

bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux",
"dağıtım": "Ubuntu GNU/Linux"}
print(set(bilgi))
# {'sistem çekirdeği', 'işletim sistemi', 'dağıtım'}

küme = {'Python', 'C++', 'Ruby', 'PHP'} # Küme oluşur
küme = {} # Sözlük oluşur

str1 = "Python Programlama Dili"
küme = set(str1)
# {'g', 'D', 'a', ' ', 'o', 'n', 'm', 'l', 'i', 'h', 't', 'r', 'P', 'y'}


liste = ["elma", "armut", "elma", "kiraz",
"çilek", "kiraz", "elma", "kebap"]

for i in set(liste):
        print("{} listede {} kez geçiyor!".format(i, liste.count(i)))

"""
kebap listede 1 kez geçiyor!
elma listede 3 kez geçiyor!
kiraz listede 2 kez geçiyor!
armut listede 1 kez geçiyor!
çilek listede 1 kez geçiyor!
"""

# Kümelerde sıra yok, her şey sadece 1 tane
set(liste)[0] # Hata verir, çünkü sıra yok
# Sıralı küme için modül -> https://pypi.org/project/orderedset/

km = set("adana")
for i in km:
        print(i, end=" ")
# d n a

km.clear()
print(km)
# set()

km = set("kahramanmaraş")
yedek = km.copy()
print(yedek)
# {'a', 'r', 'h', 'k', 'm', 'ş', 'n'}
print(km)
# {'a', 'h', 'k', 'm', 'n', 'r', 'ş'}


küme = set(["elma", "armut", "kebap"])
küme.add("çilek")
print(küme)
# {'elma', 'armut', 'kebap', 'çilek'}


"""
Python’daki şu veri tipleri değiştirilemeyen veri tipleridir:
Demetler
Sayılar
Karakter Dizileri

Şu veri tipleri ise değiştirilebilen veri tipleridir:
Listeler
Sözlükler
Kümeler

Dolayısıyla bir kümeye ancak şu veri tiplerini ekleyebiliriz:
Demetler
Sayılar
Karakter Dizileri
"""

k1 = set([1, 2, 3, 5])
k2 = set([3, 4, 2, 10])
print(k1.difference(k2))
# {1, 5}

k2.difference(k1)
# {10, 4}


k1 = set([1, 2, 3])
k2 = set([1, 3, 5])
k1.difference_update(k2)
print(k1)
# {2}
print(k2)
# {1, 3, 5}

hayvanlar = set(["kedi", "köpek", "at", "kuş", "inek", "deve"])
hayvanlar.discard("kedi")
print(hayvanlar)
# {'kuş', 'inek', 'deve', 'köpek', 'at'}

hayvanlar.discard("yılan") # Bulamazsa hata vermez
hayvanlar.remove("köpek") # Bulamazsa hata verir

k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
print(k1.intersection(k2))
# {1, 3}

a = set([1, 2, 3])
b = set([2, 4, 6])
print(a.isdisjoint(b))
# False # Çünkü kesişim kümesi boş değil, ayrık küme değiller

a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])
print(a.issubset(b))
# True # a kümesinin bütün öğeleri b kümesi içinde yer alıyor. Yani a, b’nin alt kümesidir.

a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])
print(a.issubset(b))
# True # Buradan, “a kümesi b kümesinin alt kümesidir,” sonucuna ulaşıyoruz. 
b.issuperset(a)
# True # Burada ise, “b kümesi a kümesini kapsar,” sonucunu elde ediyoruz. 
# Yani b kümesi a kümesinin bütün elemanlarını içinde barındırıyor.

a = set([2, 4, 6, 8])
b = set([1, 3, 5, 7])
print(a.union(b)) # Birleşim
# {1, 2, 3, 4, 5, 6, 7, 8}

küme = set(["elma", "armut", "kebap"])
yeni = [1, 2, 3]
küme.update(yeni)
print(küme)
# {1, 2, 3, 'elma', 'armut', 'kebap'}

a = set(["elma", "armut", "kebap"])
print(a.pop()) # Rastgele bir öge silecek