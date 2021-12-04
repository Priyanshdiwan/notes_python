l1=["aaple","pineapple","lichi","banana"]


# to select odd numbered items from the list
# i=1
# for item in l1:
#     if i%2!=0:
#         print(item)
#     i+=1
obj1 = enumerate(l1)
for i,item in enumerate(l1):
    if i%2==0:
        print(f"the {i}th item in the list is {item} ")
# so basically enum

print ("Return type:",type(obj1))
print (list(enumerate(l1)))
 

s1 = "geek"


# creating enumerate objects eith changes index
obj2 = enumerate(s1)
# changing start index to 2 from 0
print (list(enumerate(s1,2)))