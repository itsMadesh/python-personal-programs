import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])

plt.plot(x,y,'o--r')
plt.show()
#markersize(ms),(mec) to set the color of the edge of the markers
#Use both the mec and mfc arguments to color of the entire marker: