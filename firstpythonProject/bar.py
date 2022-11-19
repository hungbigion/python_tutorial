import matplotlib.pyplot as plt
import numpy as np


colors=["blue","green","yellow","red"]
mylabels = ["Python", "Java", "PHP", "C#"]
y = np.array([50, 30, 20, 15])

plt.bar(mylabels,y,color=colors)
plt.show()