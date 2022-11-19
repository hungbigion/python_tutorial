import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([17, 18, 19, 20, 21, 22, 23, 24])
y = np.array([18, 19, 20, 21, 22, 23, 24, 25])
plt.subplot(1, 3, 1)
plt.plot(x,y,'ro', label='riding')
plt.title("RIDDING")
plt.xlabel('Age')
plt.ylabel('Hours')

#plot 2:
x = np.array([19, 20, 21, 22, 23, 24, 25, 26])
y = np.array([19, 20, 21, 22, 23, 24, 25, 26])
plt.subplot(1, 3, 2)
plt.plot(x,y, 'g^', label='swimming')
plt.title("SWIMMING")
plt.xlabel('Age')
plt.ylabel('Hours')

#plot 3:
x = np.array([12, 14, 10, 25, 21, 20, 19, 18])
y = np.array([13, 25, 24, 26, 29, 28, 24, 23])
plt.subplot(1, 3, 3)
plt.plot(x,y, 'b*', label='sailing')
plt.title("SAILING")
plt.xlabel('Age')
plt.ylabel('Hours')


plt.suptitle("Activities Scatter Graph")
plt.legend()
plt.show()