
import csv
import matplotlib.pyplot as plt
import tkinter as tk

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
	i=0
	while i<1500:
		i+=1

		sum=0
		for j in range(len(y)):

			h=t0+t1*x[j]
			sum=sum+(h-y[j])
		tempt0=t0-a*(1.0/m)*sum
		sum=0
		for j in range(len(y)):

			h=t0+t1*x[j]
			sum=sum+((h-y[j])*x[j])
		tempt1=t1-a*(1.0/m)*sum

		t0=tempt0
		t1=tempt1
		tarr=[t0,t1]
	return tarr
	

def cost():
	sum=0
	t0=gradient_decent()[0]
	t1=gradient_decent()[1]
	for i in range(len(x)):
		h=t0+t1*x[i]
		sum=sum+((h-y[i])*(h-y[i]))
	cost=(1.0/(2*m))*sum
	return cost

def predict():
	#input some number
	user_in=user_input
	print(user_in)
	a=float(user_in)
	t0=gradient_decent()[0]
	t1=gradient_decent()[1]
	y=t0+t1*a
	return y


def graphLine():

	t0=gradient_decent()[0]
	t1=gradient_decent()[1]

	y_plot=[]
	for i in range(len(x)):
		y_plot.append(t0+t1*x[i])

	plt.plot(x,y_plot,c='r')	
	plt.scatter(x,y,c='g')
	plt.show()
def gui():
	window=tk.Tk()

	E=tk.Entry(window)
	E.place(x=10,y=10)
	
	def predict():
	#input some number
		user_input=E.get()
		iput=float(user_input)
		t0=gradient_decent()[0]
		t1=gradient_decent()[1]
		y=(t0+t1*iput)
		L=tk.Label(window,text=y)
		L.place(x=40,y=70)

	B=tk.Button(window,text='Predict',command=predict)
	B.place(x=40,y=40,width=70,height=20)




	window.mainloop()

graphLine()
gui()
