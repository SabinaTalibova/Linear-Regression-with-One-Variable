
import csv

x=[]
y=[]


with open('data.csv','r') as file:
	data=csv.reader(file)
	for row in data:
		a=float(row[0])
		b=float(row[1])
		x.append(a)
		y.append(b)

a=0.01
m=len(x)
def gradient_decent():
	t0=0
	t1=0
	for i in range(len(x)):
		sum=0
		for j in range(len(y)):
			h=t0+t1*x[j]
			sum=sum+(h-y[j])
		tempt0=t0-a*(1.0/m)*sum
		sum=0
		for j in range(len(y)):
			h=t0+t1*x[j]
			sum=sum+(h-y[j])*x[j]
		tempt1=t1-a*(1.0/m)*sum

		t0=tempt0
		t1=tempt1
	print(t0)

gradient_decent()
