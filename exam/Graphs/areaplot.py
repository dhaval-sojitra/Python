import numpy as np
import matplotlib.pyplot as plt
x = range(1,6)
y = [1,4,6,2,4]
plt.fill_between(x,y)
plt.title('Area plot')
plt.show()