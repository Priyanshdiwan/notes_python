"""
r -  open to read[default]
w - open for writing
x - create file if not exsist
a - appends; adds more to file
t - text mode; the fil .txt(as a string)[default mode]
b - binary mode
+ - read+write(update)
"""
f = open("jord.txt", "r")
content = f.read(3)
print(content)

f.close()