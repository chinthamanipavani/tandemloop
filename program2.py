a=int(input("enter  a number :"))
def series(a):
    for i in range(1,(2*a)+1):
       if i%2!=0:
           print(i,end=" ")

series(a)



# output

# enter  a number :1
# 1
# enter  a number :2
# 1 3 
# enter  a number :3
# 1 3 5 
# enter  a number :4
# 1 3 5 7
