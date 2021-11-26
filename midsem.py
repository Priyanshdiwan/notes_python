#How to print 2 decimal digits
# num=9.6788089080789898
# print("{:.2f}".format(num))

# To Check for leap year or not
# year=int(input("Enter the Year:\n"))
# if year%4==0:
#     print("It is a Leap Year")
# else:
#     print("It is not a leap year")


# generate * output
# n=5
# while(n>1):
#     print(n*"*")
#     n=n-1

# odd number in range 
# for i in range(100,201):
#     for j in range(2,i):
#      if i%j==0:
#         break
#     else:
#         print(i)


# function for fibonnaci
# f1=5
# f2=6
# f3=0
# print(f1)
# print(f2)
# for i in range(100):
#     f3=f2+f1
#     print(f3)
#     f1=f2
#     f2=f3


# print 12345 wala output
# i=1
# while(i<7):
#     if i==1:
#         print(i,end=" ")
#         i=i+1
#     else:
#        m=1
#        while(m<i):
#         print(m,end=" ")
#         m=m+1
#     i=i+1
#     print()

# to check for palindrome 
# word=input(("Please enter a word:\n"))
# def palindrom(n):
#     if n == n[::-1]:
#         print("it is a palindrome")
#     else:
#         print("it is not a palindrome") 

# palindrom(word)

# print output
# m=int(input("Enter a Number"))
# i=1
# while(i<m+1):
#         print(str(i)*(2*i))
#         i=i+1

# 
# num=int(input("Enter a number for which you want to generate a table for"))
# for i in range(1,11):
#         print(num,"*",i,"=", num*i)

# marks=[80,90,99,75,79]
# avg=sum(marks)/5

# if avg in range(91,101):
#         print("your grade is A+")
# if avg in range(81,91):
#         print("your grade is A")
# if avg in range(71,81):
#         print(" your grade is B+")
# if avg in range(61,71):
#         print("your grade is B")
# if avg in range(51,61):
#         print("your grade is C")
# if avg in range(41,51):
#         print("your grade is D")
# if avg in range(0,41):
#         print("your grade is E")

# s=str(input("enter a word"))
# new_str=s[::-1]
# print(new_str)



# to find a sum of cubes of each digit of a number 
# number=input("enter in number")
# l=[]
# for i in number:
#     n=int(i)*int(i)*int(i)
#     l.append(n)

# print(sum(l))
