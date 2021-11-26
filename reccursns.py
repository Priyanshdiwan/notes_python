# # factorial by itterative
# def factorial_iterative(n):
#     fac=1
#     for i in range(n):
#         fac= fac * (i+1)
#     return(fac)

# num=int(input("Enter the number: "))


# #Factorial by recursion
# function ke andar function: recursion
# def fac_recursive(num):
#   if num==1:
#     return 1 
#   else:
#     return num*fac_recursive(num-1)
  
# print(fac_recursive(5))

# WORKING:
# jab mai num=5 dunga to ye recurssion stack mai retun karega 5*fac_recursive(4)
#  phir ye 5*4*fun_recursive(3) save karega
# phir ye 5*4*3*2*fun_recursive(1)jayega aur finally 120 de dega output


# fibonacci

n=int(input("Enter which fibonachi number you wantr to find: "))
def fibonacci(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
      return fibonacci(m-1)+ fibonacci(m-2)

print(fibonacci(n)) 

    



