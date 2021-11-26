"""
i = 0
while(i<45):
    print(i, end=" ")
    i= i+3
    if(i==9):
        break

# break ka mtlb jab i=9 ho jayega program band ho jayega



i = 1
while(True):
    if 1+1<5:
        i=i+1
        continue
    print(i+1, end=" ")
    if(i==44):
        break
    i=i+1
"""
while(1):
    print("enter your number\n")
    x=int(input())
    if x>100:
        print("good fucking work\n")
        break
    else:
        continue
