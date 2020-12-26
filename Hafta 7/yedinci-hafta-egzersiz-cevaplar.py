import numpy as np    
import matplotlib.pyplot as plt
np.random.seed(42)


def isNumpyArrayIncludeDuplicate(twodimarr):
    including_list = list()

    for arr in twodimarr:
        for element in arr:
                if element in including_list:
                    return True
                else:
                    including_list.append(element)
    return False

a = None
b = None

while True:
    #assert not (a == np.random.randint(0,10, size=(3,3))).all(), "a aynı çıktı"
    a = np.random.randint(0,10, size=(3,3))
    if isNumpyArrayIncludeDuplicate(a):
        continue
    
    #assert not (b == np.random.randint(0,10, size=(3,3))).all(), "b aynı çıktı"
    b = np.random.randint(0,10, size=(3,3))
    if isNumpyArrayIncludeDuplicate(b):
        continue
    
    break

c = np.dot(a, b)

c = c.reshape(9)

import matplotlib.pyplot as plt 
plt.hist(c)
plt.show()

