a=int(input("enter  a number :"))
def series(a):
    if a%2==0:
       n=a-1
    else:
       n=a
    for i in range(1,(2*n),2):
         print(i,end=" ")
series(a)
         
#output
# enter  a number :1
# 1  
# enter  a number :2
# 1
# enter  a number :3
# 1 3 5
# enter  a number :4
# 1 3 5 
#  enter  a number :5
# 1 3 5 7 9 
# enter  a number :6
# 1 3 5 7 9