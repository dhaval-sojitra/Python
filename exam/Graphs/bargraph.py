import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('bookstall.xlsx')
print(df)
x=df['Type_of_book']
y=df['Sales']
plt.bar(x,y, label='Category_wise_sales_of_Books',color='Blue')
plt.xlabel('Type_of_Book')
plt.ylabel('Sales')
plt.title('Atmiya Book Shop')
plt.legend()
plt.show()