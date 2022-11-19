import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,100)
def f(x):
    return np.cos(x)+1
y= f(x)
plt.plot(x,y,"r*")
plt.show()