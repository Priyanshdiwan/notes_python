"""
a =7 
b= 5 
z = sum((a, b)) # built in 
"""

def f1(a,b):
    
 sum= a+b
 return sum

v= f1(9,7)
print(v)


#try exception handling
#even if try wala statment na chle per aage code chale 
print("enter number 1")
x=input()
print("enter second 2")
y=input()
try:
     print("the sum is", 
      int(x)+int(y))
except Exception as rr:
    print (rr)

print("listen! fuck off this was madatory")
