import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,25,50,50,50])
y=["Suzuki","Ford","Benz","Audi","BMW"]
z=[0,0,0.2,0,0]
plt.pie(x,labels=y,explode=z,shadow=True)
plt.legend(title="CAR BRAND")
plt.show()