import matplotlib.pyplot as plt
import numpy as np

y = np.array([50, 30, 20, 15])
mylabels = ["Python", "Java", "PHP", "C#"]
colors=["blue","green","yellow","red"]
myexplode = [0.1, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode, colors = colors, shadow = True,startangle=90,counterclock=False,autopct="%1.f%%")
plt.title("Programing Language")
plt.legend()
plt.show()