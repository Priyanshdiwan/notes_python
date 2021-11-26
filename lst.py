
general = [2,5,7,9,"food","drink"]
print(general[5])

number = [2,6,7,8,5,8,9,77,67]
number.sort() #assending order mai arrange kar dega
 #sort ya reverse apne orginial list ko change kar dete hai
print(number)
# number.reverse() ; ulta kar dega

#extended sclicing 

print(number[0:7:2])
 #slicing original list ko change nhi karta
print(number[::-3])
 # ye -3 tab hi kaam karega jab samne ke colon wale value blank(deafault) ho
 # avoid karna hai (-ve) slice skipping karna

print(max(number)) # min aur len bhi use kar sakte

number.append(5)
# number.append("apple"); string bhi append kar sakte hai
print(number)

li=[1,2,3,4,5,6,]
li2=[11,22,33,44]
# li.append(li2) append use karte hai to li2 ko li list ke andar list bana dega 
li.extend(li2)# li1 list ke andar l2 jayega element ban ke  
print(li[6])

#l = [int(input()) for i in range(1,6)]# range for list
#print(l) take input in a list within specified range


number.insert(2,69)
print(number)

number.remove(69)
print(number)


li.pop()# delete last number
# li.clear() deletes the list elements

# mutable = can change (list)
# immutable = cannot change(tupple)

tp = (1,)# 1 element ka tupple banao to comma lagao
print(tp)

"""
interchange karne ke liye
a = 6
b = 5
a, b = b, a
print(a , b)
"""


