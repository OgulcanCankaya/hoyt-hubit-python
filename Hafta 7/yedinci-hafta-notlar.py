# Konsola pip install numpy diyerek modülümüzün kurulumunu yapıyoruz
# Sonrasında import ediyoruz

"""
NumPy
=====

Provides
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation
"""

import numpy as np

a = [1,2,3,4]
b = [2,3,4,5]

# Bu iki elementwise çarpmanın yolları
# 1. Klasik yol
ab = []                       
for i in range(0, len(a)):
  ab.append(a[i]*b[i])
print(ab)

# 2. numpy kullanarak
a = np.array(a)
b = np.array(b)
print(a*b)


# NumPy Array'i Oluşturmak
print(np.array([1,2,3,4,5]))
a = np.array([1,2,3,4,5])
print(type(a))
# numpy.ndarray

print(np.array([3.14, 4, 2, 13], dtype = "int"))
# array([ 3,  4,  2, 13])

print(np.zeros(10, dtype = int))
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print(np.ones((3,5), dtype = int))
"""
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
"""

print(np.full((3,5), 3))
"""
array([[3, 3, 3, 3, 3],
       [3, 3, 3, 3, 3],
       [3, 3, 3, 3, 3]])
"""

print(np.arange(0,31, 3))
# array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27, 30])

print(np.linspace(0,1,10))
"""
array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444,
       0.55555556, 0.66666667, 0.77777778, 0.88888889, 1.        ])
"""

print(np.random.normal(10, 4, (3,4)))
"""
array([[ 7.95311755, 18.88626347,  6.68342754,  9.41779354],
       [ 6.56580837,  9.3286982 ,  2.81822871, 11.70010496],
       [15.3764241 ,  8.20890978,  8.67603323,  5.88175198]])
"""

print(np.random.randint(0,10, (3,3)))
"""
array([[9, 0, 2],
       [1, 1, 2],
       [5, 7, 8]])
"""

"""
ndim: boyut sayısı
shape: boyut bilgisi
size: toplam eleman sayısı
dtype: array veri tipi
"""


print(np.random.randint(10, size = 10))
# array([8, 1, 0, 6, 3, 8, 2, 2, 8, 1])


a = np.random.randint(10, size = 10)
print(a.ndim)
# 1

print(a.shape)
# (10,)

print(a.size)
# 10

print(a.dtype)
# dtype('int64')


b = np.random.randint(10, size = (3,5))
print(b)
"""
array([[5, 2, 8, 5, 8],
       [2, 4, 8, 4, 3],
       [9, 0, 2, 0, 2]])
"""

print(b.ndim)
# 2

print(b.shape)
# (3, 5)

print(b.size)
# 15

print(b.dtype)
# dtype('int64)

# Yeniden Şekillendirme (Reshaping)

print(np.arange(1,10))
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(np.arange(1,10).reshape((3,3)))
"""
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
"""

# Array Birlestirme (Concatenation)

x = np.array([1,2,3])
y = np.array([4,5,6])

print(np.concatenate([x, y]))
# array([1, 2, 3, 4, 5, 6])

z = np.array([7,8,9])
print(np.concatenate([x, y, z]))
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])

a = np.array([[1,2,3], 
              [4,5,6]])

print(np.concatenate([a,a]))
"""
array([[1, 2, 3],
       [4, 5, 6],
       [1, 2, 3],
       [4, 5, 6]])
"""

print(np.concatenate([a,a], axis = 1))
"""
array([[1, 2, 3, 1, 2, 3],
       [4, 5, 6, 4, 5, 6]])
"""

# Array Ayırma (Splitting)

x = np.array([1,2,3,99,99,3,2,1])
print(np.split(x, [3,5]))
# [array([1, 2, 3]), array([99, 99]), array([3, 2, 1])]

a,b,c = np.split(x, [3,5])
print(a)
# array([1, 2, 3])
print(b)
# array([99, 99])
print(c)
# array([3, 2, 1])

# iki boyutlu ayırma
m = np.arange(16).reshape(4,4)
print(m)
"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
"""

print(np.vsplit(m, [2]))
"""
[array([[0, 1, 2, 3],
        [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
        [12, 13, 14, 15]])]
"""

ust, alt = np.vsplit(m, [2])
print(ust)
"""
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
"""
print(alt)
"""
array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])
"""
print(m)
"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
"""

print(np.hsplit(m, [2]))
"""
[array([[ 0,  1],
        [ 4,  5],
        [ 8,  9],
        [12, 13]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11],
        [14, 15]])]
"""

sag, sol = np.hsplit(m, [2])
print(sag)
"""
array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]])
"""
print(sol)
"""
array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])
"""

# Array Sıralama (Sorting)

v = np.array([2,1,4,3,5])
np.sort(v)
print(v)
# array([2, 1, 4, 3, 5])

v.sort()
print(v)
# array([1, 2, 3, 4, 5])

# iki boyutlu array siralama
m = np.random.normal(20,5, (3,3))
print(m)
"""
array([[25.45684489, 21.83575476, 26.06913773],
       [17.50480621, 18.65456644, 25.99114299],
       [15.28755765, 21.08674903, 16.10947821]])
"""

print(np.sort(m, axis = 1))
"""
array([[21.83575476, 25.45684489, 26.06913773],
       [17.50480621, 18.65456644, 25.99114299],
       [15.28755765, 16.10947821, 21.08674903]])
"""

print(np.sort(m, axis = 0))
"""
array([[15.28755765, 18.65456644, 16.10947821],
       [17.50480621, 21.08674903, 25.99114299],
       [25.45684489, 21.83575476, 26.06913773]])
"""

# Index ile Elemanlara Erişmek

a = np.random.randint(10, size = 10)
print(a)
# array([9, 7, 0, 1, 1, 3, 5, 9, 6, 8])
print(a[0])
# 9
print(a[-1])
# 8

a[0] = 100
print(a)
# array([100,   7,   0,   1,   1,   3,   5,   9,   6,   8])

m = np.random.randint(10, size = (3,5))
print(m)
"""
array([[6, 8, 8, 1, 9],
       [5, 3, 6, 5, 9],
       [5, 8, 4, 1, 4]])
"""

print(m[0,0])
# 6

print(m[1,1])
# 3


m[1, 4] = 99
print(m)
"""
array([[ 6,  8,  8,  1,  9],
       [ 5,  3,  6,  5, 99],
       [ 5,  8,  4,  1,  4]])
"""

m[1,4] = 2.2
print(m)
"""
array([[6, 8, 8, 1, 9],
       [5, 3, 6, 5, 2],
       [5, 8, 4, 1, 4]])
"""

# Slicing ile Elemanlara Erişmek (Array Alt Kümesine Erişmek)
a = np.arange(20,30)
print(a)
# array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

print(a[0:3])
# array([20, 21, 22])
 
print(a[:3])
# array([20, 21, 22])

# iki boyutlu slice islemleri

m = np.random.randint(10, size = (5,5))
print(m)
"""
array([[4, 9, 9, 8, 7],
       [0, 4, 7, 4, 5],
       [8, 2, 7, 6, 3],
       [3, 3, 8, 8, 1],
       [6, 4, 0, 5, 0]])
"""

print(m[:,0])
# array([4, 0, 8, 3, 6])

print(m[:,1])
# array([9, 4, 2, 3, 4])

print(m[:,4])
# array([7, 5, 3, 1, 0])

print(m[0:2, 0:3])
"""
array([[4, 9, 9],
       [0, 4, 7]])
"""


m = np.arange(9).reshape((3,3))
print(m)
"""
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
"""

# Fancy Index ile Elemanlara Erişmek

satir = np.array([0,1])
sutun = np.array([1,2])

print(m[satir, sutun])
# array([1, 5])

print(m[0, [1,2]])
# array([1, 2])

print(m[0:, [1,2]])
"""
array([[1, 2],
       [4, 5],
       [7, 8]])
"""

# Koşullu Eleman İşlemleri

v = np.array([1, 2, 3, 4, 5])

print(v < 3)
# array([ True,  True, False, False, False])

print(v[v < 3])
# array([1, 2])

print(v[v > 3])
# array([4, 5])

print(v[v != 3])
# array([1, 2, 4, 5])

print(v * 2)
# array([ 2,  4,  6,  8, 10])

print(v / 5)
# array([0.2, 0.4, 0.6, 0.8, 1. ])

# Matematiksel İşlemler

v = np.array([1, 2, 3, 4, 5])

print(v - 1)
# array([0, 1, 2, 3, 4])

print(v * 5)
# array([ 5, 10, 15, 20, 25])

print(v / 5)
# array([0.2, 0.4, 0.6, 0.8, 1. ])

print(v*5/10 - 1)
# array([-0.5,  0. ,  0.5,  1. ,  1.5])

print(np.subtract(v, 1))
# array([0, 1, 2, 3, 4])

print(np.add(v, 1))
# array([2, 3, 4, 5, 6])

print(np.multiply(v,4))
# array([ 4,  8, 12, 16, 20])

print(np.divide(v, 3))
# array([0.33333333, 0.66666667, 1.        , 1.33333333, 1.66666667])

print(v**3)
# array([  1,   8,  27,  64, 125])

print(np.power(v, 3))
# array([  1,   8,  27,  64, 125])

print(v % 2)
# array([1, 0, 1, 0, 1])

print(np.mod(v, 2))
# array([1, 0, 1, 0, 1])

print(np.absolute(np.array([-3])))
# array([3])

print(np.sin(360))
# 0.9589157234143065

print(np.cos(180))
# -0.5984600690578581

v = np.array([1,2,3])
print(np.log(v))
# array([0.        , 0.69314718, 1.09861229])

print(np.log2(v))
# array([0.       , 1.       , 1.5849625])

print(np.log10(v))
# array([0.        , 0.30103   , 0.47712125])

# İstatistiksel Hesaplamalar

print(np.mean(v))
# 2.0

print(v.sum())
# 6

print(v.min())
# 1

"""
np.mean(arr,axis=0) | Returns mean along specific axis

arr.sum() | Returns sum of arr

arr.min() | Returns minimum value of arr

arr.max(axis=0) | Returns maximum value of specific axis

np.var(arr) | Returns the variance of array

np.std(arr,axis=1) | Returns the standard deviation of specific axis

arr.corrcoef() | Returns correlation coefficient of array
"""

# NumPy ile İki Bilinmeyenli Denklem Çözümü

"""
5 x0 + x1 = 12
x0 + 3 x1 = 10
"""

a = np.array([[5,1], [1,3]])
b = np.array([12,10])
x = np.linalg.solve(a, b)
print(x)
# array([1.85714286, 2.71428571])