# lambda function and anonyous function
# def add(a,b):
#     return a+b
     

#  or

# add=lambda a, b: a+b
# # upar ke dono cheez ek hi kaam karta hai 
# print(add(3,4))

# def a_first(a):
#     return a[1]
 
# a=[[1, 14],[5,6],[8,23],[55,69,3]]
# a.sort(key=a_first)
# print(a)

# #      OR

# a=[[1, 14],[5,6],[8,23],[55,69,3]]
# a.sort(key=lambda x:x[1])
# print(a)

#FILTER
l1=[2,3,4,5,6,7,8,9]
evens=list(filter(lambda a:a%2==0,l1))
print(evens)
# ye filter ek object hai so you have to sign it to a varible
# it takes 2 arguments first is the function on which parameter you wan to filter in this case it is even/odd
# argument 2 is a iretable object

# supose i want ever even number doubled we use
doubled_even=list(map(lambda a:a*a,evens))
print(doubled_even)
#  it takes 2 arguments first is the function which discribes what do you want to do 
# argument 2 is a iretable object
