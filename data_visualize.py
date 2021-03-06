
import csv
import matplotlib.pyplot as plt


x=[]
y=[]
with open('data.csv') as file:
	data=csv.reader(file)
	for row in data:
		a=float(row[0])
		b=float(row[1])
		x.append(a)
		y.append(b)


index=[]
for elemnt in y:
	if elemnt<0:
		index.append(y.index(elemnt))
#keeping indexes of negative y values
new_x=[]
new_y=[]
#create new array with only negative values
for elemnt in index:
	new_x.append(x[elemnt])
	new_y.append(y[elemnt])


plt.scatter(x,y,c='g')
#scatter negative values
plt.plot(new_x,new_y,c='r')






plt.axvline(x=0)
plt.axhline(y=0)

plt.xlabel("number of population")
plt.ylabel("profit")

plt.title("Data Visulitation")


plt.show()
