# s= set()
x= set([5,6,7,8])
y= set([7,8,9,10])
# print(x)
# print(type(x)) or print(type(x) is set)

# x.add(1)
# x.add({'a','y'})
# x.add(5)
# x.remove(5)
# p = x.union({7,8,9,10}) or print(x|y)
# q = x.intersection(y)  or print(x&y)
# diffrence m=x-y
# print(q)
# # len, min, max also applies 
# print(x.isdisjoint(y))
# print(x.issubset(y))
# SUPERSET
# t=x>y; print(t) #gives bullean variable
# if y is a subset of x, y must iclude all element of x
#  then it compares the number of item and one with  more number of items is larger 

# s1={4,5,6,7,}
# s2={4,6,7,8,9,10}
# print(type(s1))    
# print(s2>s1)

#  set compregation, you can do it with list too if you want ordered and duplicated 
# s={c *4 for c in 'spam'}
# print(s)
# s={c *4 for c in 'spamham'}#set doesnt allow duplicate value 
# print(s)

# POP/REMOVE/DISCARD
# s3={2,3,4,5,6,7,2,1}
# print(s3)
# s3.pop()
# print(s3)
# s3.discard(3)
# print(s3)
# s3.remove(2)#agar discard ka argument set mai nhi hai to vo error de dega
# print(s3)
# s3.discard(2)#agar discard ka argument set mai nhi hai to vo error nhi dega
# print(s3)


# print(x.intersection(y))
# print(x&y)
# print(x.union(y))
# print(x|y)


print(x.difference_update(y))
# ye error de dega kyuki diffrence update mai diffrence/jo y mai hai per x mai nhi hai usko x aurb y ka
#  vo x mai ja ke save ho jayega to print(x command dena padega)
print(x)

# x.symmetric_difference_update(y)
# # # ye error de dega kyuki diffrence update mai union jo hoga x aurb y ka
# # #  vo x mai ja ke save ho jayega to print(x command dena padega)
# print(x)