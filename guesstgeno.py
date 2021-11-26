from typing import Counter


n = 20
number_of_guess= 1
print("you have 9 chances")
while(number_of_guess<=3):
    print("enter a number")
    x=int(input())
    if x>20:
        print("your number is too big")
        continue
    if x<20:
        print("your number is small")
        continue
    elif x==20:
        print("you got it bro")
        break 
if(number_of_guess>3):
    print("fuck off out of chance")

