import matplotlib.pyplot as plt
#Taking the percentage of sales of different products
sales_per=[35,10,25,30]
#Taking the names of the products
prod_name=['Hatch back','Sedan','Premium','Commercial']
#Giving the color to each product category
col=['red','pink','blue','yellow']
#Creating the pie chart (Using pie())
plt.pie(sales_per,labels=prod_name,colors=col,startangle=90)
#Setting upt the titles and legend
plt.title('TATA Motors')
plt.legend()
#Showing the chart
plt.show()