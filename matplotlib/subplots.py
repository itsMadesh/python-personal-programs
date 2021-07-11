import matplotlib.pyplot as plt
import numpy as np

#plot-1:
x=np.array(["A","B","C","D","E"])
y=np.array([90,80,70,60,50])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.grid()
plt.title("Grade Method-1")


#plot-2:
x=np.array(["A","B","C","D","E"])
y=np.array([100,90,80,70,60])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.grid()
plt.title("Grade Method-2")
plt.suptitle("Grade Methods")

plt.show()