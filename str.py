x = "priyansh is JORD"
y = "i am jord"

print(x[0:8])
 #kaha se kaha tak ke element print karna hai
 # 0 include hota hai aur 17th element skip isliye 16th element print karne ke liye 17 likhte hai
print(len(x))
 #length mtlb kitna letter hai p=0 d=16 
print(x[0:17:2])
 #advance sclicing the last digit(2) shows ki kitna letter skip karna hai
print(x[-4:-1])
 #-1 = LAST ELEMENT= D
print(x[::-1]) 
 #-1 last mai likhne se ulta kar deta hai 

print(x.isalnum())
 #bullian variable; alphanumeric string nhi hai isliye

print(x.endswith("JORD"))
print(x.count("i"))
print(x.capitalize())
 #first letter string ka capital kar rha hai
print(x.find("p"))
print(x.upper()) #sab capital/lower bhi kar sakte
print(x.replace("is", "always"))# replace karta hai

z = 23.42232332
print(f"{z:.3f}")#.0/1/2f defines how many number after decimal which has to be printed

