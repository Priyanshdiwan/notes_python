# lambda function and anonyous function
# def add(a,b):
#     return a+b
     

#  or

# add=lambda a, b: a+b
# # upar ke dono cheez ek hi kaam karta hai 
# print(add(3,4))

def a_first(a):
    return a[1]
 
a=[[1, 14],[5,6],[8,23],[55,69,3]]
a.sort(key=a_first)
print(a)

#      OR

a=[[1, 14],[5,6],[8,23],[55,69,3]]
a.sort(key=lambda x:x[1])
print(a)
