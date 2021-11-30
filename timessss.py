#  here we are comparing time of a function using time module



import time

# time.time() tick return karta hai like a counter 
# start_time_for=time.time()
# for i in range(45):
#     print(i)
# final_time_forloop= time.time()-start_time_for
# print(f"for loop ran in:{final_time_forloop}")

# start_time_while=time.time()
# k=0
# while(k<45):
#     print(k)
#     k=k+1
# final_time_while=time.time()-start_time_while
# print(f"while loop ran in {final_time_while}")




#  ANOTHER PROGRAM USING TIME
local_time=time.asctime(time.localtime(time.time()))
print(local_time)


#  IF YOU WANT THE CODE TO SLEEP FOR FEW SECONDS AND THEN PRINT USE time.sleep("now many seconds you want him to sleep")
for i in range(10):
    print(f"i am at {time.time()}")
    time.sleep(2)#is line ke baad compiler ko rook dega 2 second ke liye


