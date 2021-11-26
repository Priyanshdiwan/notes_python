# # Q1. program for checking if the inpurt is rotation 
# s1 = input("Please enter first string:\n")
# s2 = input("please enter second string:\n")
# howlongiss1 = len(s1)
# i=1
# while(i<howlongiss1):
#     y = s1[0:i]
#     z= s1[i:howlongiss1]
#     i=i+1
#     newstring=(z+y)
#     if newstring==s2:
#         print("TRUE:rotation found when its roatated", (i-1),"times to the right")
#         break
#     if i==howlongiss1:
#         print("False: no rotation found")
    
# # Q2 program to count no. of word in a srtring
# y=input("please enter the sentence:\n")
# words=y.split( )
# cnt=len(words)
# print("the no of word is: " + str(cnt))


#Q make a (1)new list
#sol(1)
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=[]
# l4=[]
# i=0

# while(i<5):
#     y=l1[i]
#     z=l2[i]
#     i=i+1
#     l3.append(y)
#     l3.append(z)
# print(l3)


# Q3 Write a program to remove the duplicate character from string.
# def remDuplicate(str, n):
# 	s = set()
# 	for i in str:
# 		s.add(i)
# 	st = ""
# 	for i in s:
# 		st = st+i
# 	return st
# str = "geeksforgeeks"
# n = len(str)
# print(remDuplicate(list(str), n))



    

# Q4 Write a program to remove the space from given string.
# m=input("Please enter a string:\n")
# y=list(m.split( ))
# z=len(y)
# for i in range(z):
#     print(y[i], end="")
#     i=i+1


# Q5 Write a program to find all the permutations of a string.
# m=str(input("Please enter your string:\n"))
# strlength=len(m)
# i=0
# print("the possible permuatiaon are:")
# for i in range(strlength):
    
#     piece=m[0:i]
#     left=m[i:strlength]
#     newword=left + piece
#     print(newword)

# Q6 Write a program to get details of ten student using list (regno, name, dob, branch,mark1,mark2,mark3) and find total, average and result=pass or fail for each student.
# Namelist=[]
# rollno=[]
# dob=[]
# branch=[]
# m1=[]
# m2=[]
# m3=[]

# def enterdata():
    
#     Namelist.append(input("enter students name\n"))
#     rollno.append(input("Enter roll no.\n"))
#     dob.append(input("Enter dob\n"))
#     branch.append(input("Enter branch\n"))
#     m1.append(input("Enter marks in 1st subject out of 100\n"))
#     m2.append(input("Enter marks in 2nd subject out of 100\n"))
#     m3.append(input("Enter marks in 3rd subject out of 100\n"))
#     print("student details added successfully! Enter other student details below\n\n")
    

# for i in range(2):
#     i=0
#     i=i+1
#     enterdata()


 
# def display_data_st1():
#     total= int(m1[a]) + int(m2[a]) + int(m3[a])
#     print("Name:",Namelist[a])
#     print("Roll No. ",rollno[a])
#     print("Branch of the student is:",branch[a])
#     print("Marks in 1st subject:",m1[a])
#     print("Marks in 2nd subject is:",m2[a])
#     print("Marks in 2nd subject is:",m3[a])
#     print("Total marks obtain by the student is:", total)
#     if total<180:
#         print("FAIL")
#     if total >= 180:
#         print("PASS")
      
        
# a=0  
  
# for a in range(2):
#     display_data_st1()
#     a=a+1
       
# Q7 Write a program for matrix addition using list
A= [[1,2,3],
    [4,5,6],
    [7,8,9]]

B= [[1,2,3],
   [4,5,6],
   [7,8,9]]

m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3],[4,5,6],[7,8,9]]
m1plusm2=[]
for i in range(3):
    t=[]
    for j in range(3):
        x =m1[i][j] + m2[i][j]
        t.append(x) 
    print(t)
    m1plusm2.append(t)

# Q8 Write a program to print min and max value in the list without using built in function

# list1=[2,4,6,5,9,11,22,17]
# len_of_list=len(list1)

# for i in range (0,len_of_list-1):
#     a=0
#     b=1
#     m=list1[a]
#     j=list1[b]
#     if m>j:
#         list1.remove(j)
#     if m<j:
#         list1.remove(m)
#     a=a+1
#     b=b+1

# print("The Largest number is",list1)

#Q9 Write a program to count duplicate value in the list without using built in function
# x=[2,2,1,1,5,5,5,6,6,8,8]
# length_of_x=len(x)
# stng=set(x)
# len_of_str=len(stng)
# number_of_unique=length_of_x - len_of_str
# print("Number of Duplicate values are:",number_of_unique) 

# Q10 Write a program to implement map, enumerator on list data.
# to impliment map 
# l1=[2,3,4,5,6,7,8,9,1]
# def increse10time(n):
#     x=n*10
#     return x
# new_list=map(increse10time,l1)
# print(list(new_list))

# f=enumerate(l1)
# print("enumerated list:\n", list(f))






# Q11 Write a program to create, insert, delete and update a value in the list without using built in function.
# l1=[2,3,1,4,5,6,7,"apple"]

# #to delete a value 
# new_list=[]
# no_to_be_deleted=input("type the value you want to delete in a list:\n")
# for ch in l1:
#     if ch != no_to_be_deleted:
#         new_list.append(ch)
# print(new_list)
        
# to update a value 
# value_to_be_updated=input("enter value to be updated:\n")
# updated_value=input("enter updated value:\n")
# updated_list=l1.copy()
# for ch in l1:
#     if ch == value_to_be_updated:
#         print(ch)
#         updated_list.remove(ch)
#         updated_list.append(updated_value)


# insert a value 
# y=input("enter the value after which you want to insert")
# z=list(y)
# l1.extend(y)
# print(l1)



# Q12 Write a program to sort the list without using built in function.
# l1=[2,3,5,4]
# lengthl1=len(l1)
# sortedlist=[]
# for i in range(lengthl1+1):    
#     ch1=l1[0]
#     for j in range(1,lengthl1) : 
        
#         ch2=l1[j]
#         if ch1<ch2:
#             sortedlist.append(ch1)
#             l1.remove(ch1)
                
# print(sortedlist)

