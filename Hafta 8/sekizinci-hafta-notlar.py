# Matplotlib kütüphanesini NumPy ile kullanmak

import matplotlib.pyplot as plt
import numpy as np


# Lineer denklem çizdirmek
x = np.arange(1,11) 
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) # Default olarak düz mavi çizgi
plt.show()

# Şekiller
"""
'-'     Solid line style	
'--'    Dashed line style
'-.'    Dash-dot line style
':'     Dotted line style
'.'     Point marker
','     Pixel marker
'o'     Circle marker
'v'     Triangle_down marker
'^'     Triangle_up marker
'<'     Triangle_left marker
'>'     Triangle_right marker
'1'     Tri_down marker
'2'     Tri_up marker
'3'     Tri_left marker
'4'     Tri_right marker
's'     Square marker
'p'     Pentagon marker	
'*'     Star marker
'h'     Hexagon1 marker
'H'     Hexagon2 marker
'+'     Plus marker
'x'     X marker
'D'     Diamond marker
'd'     Thin_diamond marker
'|'     Vline marker
'_'     Hline marker
"""

# Renkler
"""
'b'     Blue
'g'	    Green
'r'	    Red
'c'	    Cyan
'm'	    Magenta
'y'	    Yellow
'k'	    Black
'w'	    White
"""

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,"ob") # Daire daire, ve mavi gözükecek
plt.show() 

# Sinüs eğrisi çizdirmek
x = np.arange(0, 10, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

plt.plot(x, y, 'r') 
plt.show() 

# Sinüs-kosinüs tek grafikte gösterme
x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
   
# 2 row 1 columnu olan bir subplot oluştur, ilkini aktive et
plt.subplot(2, 1, 1)
   
# ilk plotu çizdir
plt.plot(x, y_sin) 
plt.title('Sine')  
   
# ikinci kısmı aktive et, ikincisini çizdir
plt.subplot(2, 1, 2) 
plt.plot(x, y_cos) 
plt.title('Cosine')  
   
plt.show()

# Bar grafiği
x = [5,8,10] 
y = [12,16,6]  

x2 = [6,9,11] 
y2 = [6,15,7] 

plt.bar(x, y, align = 'center') 
plt.bar(x2, y2, color = 'g', align = 'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  

plt.show()