import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x=np.linspace(0,5,6)
def f(x):
    return 2*x+1
y= f(x)
plt.subplot(2,1,1)
plt.plot(x,y,"b")
y=[1,3,5,7,9,11]
plt.plot(x,y,"bo")
plt.title("y=2x+1")
plt.xlabel("X1")
plt.ylabel("Y1")

#plot 2:
x=np.linspace(-3,3,100)
def f(x):
    return np.cos(x)+1
y= f(x)
plt.subplot(2,1,2)
plt.plot(x,y,"r*")
plt.title("y=cos(x)+1")
plt.xlabel("X2")
plt.ylabel("Y2")


plt.suptitle("Nguyễn Hữu Hùng")
plt.show()