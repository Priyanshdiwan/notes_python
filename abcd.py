# OUTPUT
# a
# ab
# abc
# ...
# abcdefghijklmnopqrstuvwxyz

alphatbet="abcdefghijklmnopqrstuvwxyz"  
for i in range(26):
   for j in range(i+1):
       if j==27:
           break
       print(alphatbet[j], end=" ")
   print()

