# f = open("jord.txt", "r")
# # content = f.read()
# # content1= f.read(3)#sirf 3 vharacter hi padhega 
# # for line in content:# line by line le sakte hai
# #     print(line,end="")
# # # print(content)

# # print(f.readline())#line by line padhta hai
# # print(f.readline())


# print(f.readlines())
# f.close()

# f = open("jord2.txt","w")
# f.write("here also priyansh is jord")
# f.close()


# f = open("jord2.txt","a")#append kar deta hai
# f.write("here also priyansh is jord\n")
# f.write("here also priyansh is jord\n")
# f.write("here also priyansh is jord\n")
# a = f.write("here also priyansh is jord")#kitne character likhe hai ye batayega
# print(a)
# f.close()

# handle reaf and write both
f= open("jord2.txt", "r+")

# f.write("priyansh was always jord")# neeche nhi be 1st line of code mai add karta hai
# print(f.readline())
# print(f.tell())# shows file pointer kaha hai
# f.seek(100)
# print(f.readline())#reset your file pointer to given place
# f.close()


#OPEN FILE WITH BLOCK
with open ("jord.txt") as f:
    print(f.read(10))
#close karne ka zarurat nhi hai