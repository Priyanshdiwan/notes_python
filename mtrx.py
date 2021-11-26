# how to Print a matrix

row=int(input("No. of Rows"))
column=int(input("No. of colums"))
matrix=[]
for i in range(row):
    l1=[]
    for j in range (column):
        num=int(input("enter numbers"))
        l1.append(num)
    matrix.append(l1)
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end="")
        
    print()
