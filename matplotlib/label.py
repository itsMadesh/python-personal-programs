import matplotlib.pyplot as plt
import numpy as np
x=np.array([31,28,31,30,31,30,31,31,30,31,30,31])
y=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
font1={"family":"Times new roman","color":"blue","size":20}
font2={"family":"Times new roman","color":"black","size":10}
plt.title("Month-Days 2021",fontdict=font1,loc="right")
plt.xlabel("Month Days",fontdict=font2)
plt.ylabel("Month",fontdict=font2)
plt.plot(x,y,marker='*',ms=5,mec="green")
plt.grid()
plt.show()

