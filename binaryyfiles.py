from os import name, times
import pickle as p

# l1=[1,2,3,]
# with open("binaryfilee.bin","wb") as file:
#     p.dump(l1,file)
#     file.close()

# with open("binaryfilee.bin","rb") as file:  
#     print(file.read())
#     file.close()


# input="sussh"
# with open("binaryyfilee.bin","wb+") as f:
#     word=input.encode()
#     f.write(word)
#     f.seek(0)
#     m=f.read()
#     print("binary data is",m)
#     z=m.decode()
#     print(z)

# mylist=["a","b","c","d",]
# with open("binaryyfilee.txt","wb") as f:
#     p.dump(mylist,f)
# with open("binaryyfilee.txt","rb") as f1:
#     sentence=p.load(f1)
#     print(sentence)

with open("binaryyfilee.txt","wb+") as f:
 for i in range(5):
    r1=input("Enter the employee name:")
    p.dump(r1,f)
        
 f.seek(0)       
 search_name=input("enter the name you want to search for")
 for i in range(5):
     n=p.load(f)
     if search_name==n:
         print(f"{n}is a{i}th entry")
    
























