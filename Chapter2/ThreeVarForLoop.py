import math

def sigmoid(z):
    return 1/(1+math.e**(-z))

def costfunction(y,a):
    return (y-a)**2

x1=[]
x2=[]
x3=[]
y=[]

with open('breast-cancer-train.csv', 'r') as f:
    line=f.readline()
    while line:
        line=line.strip("\r\n")
        line=line.split(',')
        x1.append(int(line[0]))
        x2.append(int(line[1]))
        x3.append(int(line[2]))
        y.append(int(line[3]))
        line=f.readline()

length=len(x1)
w1=0.0
w2=0.0
w3=0.0
b=0.0
J=100
alpha=0.1
accuracy=0.03
print("Calculating, please wait for some time")

while J>accuracy:
    dw1=0.0
    dw2=0.0
    dw3=0.0
    db=0.0
    J=0.0
    for i in range(0,length):
        z=w1*x1[i]+w2*x2[i]+w3*x3[i]+b
        a=sigmoid(z)
        dz=(a-y[i])*2*a*(1-a)/length
        J+=costfunction(y[i],a)/length
        dw1+=dz*x1[i]/length
        dw2+=dz*x2[i]/length
        dw3+=dz*x3[i]/length
        db+=dz/length
    w1=w1-alpha*dw1
    w2=w2-alpha*dw2
    w3=w3-alpha*dw3
    b=b-alpha*db

print(w1,w2,w3,b)
while int(input("Do you want to continue test?:"))==1:
    test1=float(input("Input first para:"))
    test2=float(input("Input second para:"))
    test3=float(input("Input final para:"))
    result=((sigmoid(w1*test1+w2*test2+w3*test3+b)))
    print(result)
