def factorial(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    print(fac)
    
x=int(input("enter a number"))
factorial(x)

# for fibonacci
n=int(input("how many fibonacci numbers you want:"))
def fibonacci(m):
    f1=-1
    f2=1
    f3=0
    ouput=[]
    for i in range(m):
        f3=f1+f2
        ouput.append(f3)
        f1=f2
        f2=f3
    print(ouput)

fibonacci(n)