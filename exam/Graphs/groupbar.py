import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
year=[2021,2022,2023]
x=[10,20,30]
x1=[40,50,60]
xaxis=np.arange(len(year))
plt.bar(xaxis - 0.2,x,0.4, label='Pencil')
plt.bar(xaxis + 0.2,x1,0.4, label='Pen')
plt.xticks(xaxis, year)
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Atmiya Stationary')
plt.legend()
plt.show()