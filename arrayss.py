import array as a


# A=a.array("d",[1,2,3,4,5,6,7,8])
# # this array takes 2 arguments first is the type of array and second is the list
# print(list(enumerate(A)))

# A.insert(0,6.9)#first argument is index where we want to add second is the the element we want to add
# print(A.remove(4.0))#REMOVES THE ELEMENT BUT WONT RETURN IT
# print(A.pop(0))#REMOVED ELEMENT SND RETURNS IT
# print(A)
# print(A[::-1])
# A[1]=6.9
# print(A)
# print(A.count(6.9))

# b=a.array("i",[1,8,4,3,7,6,2,5])
# p=a.array("i",sorted(b))
# print(p)

m=a.array("d",[1,2,3,4,5,6,7,8])
n=a.array("d",[1,2,3,4,5,6,7,8])
sums=("d",[])
for i in range(8):
    sums.append(m[i]+n[i])

print(sums)