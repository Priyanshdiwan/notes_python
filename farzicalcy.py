print("choose your operator +,-,*,/")
x=input()
print("enter first number")
y=int(input())
print("enter second number")
z=int(input())

if x=="*" and y==45 and z==3:
    print("555")
elif x=="+" and y==56 and z==9:
    print("77")
elif x=="/" and y==56 and z==4:
    print("4")
elif x=="+":
    answer=z+y
    print(answer)
elif x=="-":
    answer=y-z
    print(answer)
elif x=="*":
    answer=z*y
    print(answer)
elif x=='/':
    answer=y/z
    print(answer)
