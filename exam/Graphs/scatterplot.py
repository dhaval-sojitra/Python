import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(10)
print(x)
y = np.random.randn(10)
print(x)
plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Scatter diagram ")
plt.show()