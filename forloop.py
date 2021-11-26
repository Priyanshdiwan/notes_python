
l=["jord","rod","fraud"]
l1=[ ["jord",2],["rod",3],["fraud",3] ]
for item in l:# for printing items in a list
    print(item)

for item, number in l1:# for printing items in a list which is inside a list
    print(item, "are", number )# unpack the list

d=dict(l1)
print(d)

for item, number in d.items():
    print(item, "are", number)

for item in d:
    print(item,"are",number)


for item,number in d.items():#to print an item only if condition is fulfilled
  if number==2:
       print(item,"are",number)


l2=[2,3,4,6,7,8,9,10,11,"a","bold"]
#print only number greater then 6 in this list
for item in l2:
    if type(item) is int and int(item)>6:
        print(item)
"""
if str(item).isnumeric() and item>6:
    print(item)
this can also be used 
"""