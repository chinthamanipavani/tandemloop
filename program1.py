a,b=map(int,input("enter two numbers: ").split())
operator=input("enter the operator: ")
def operations(a,b):
    if operator=='+':
        return a+b
    elif operator=='-':
        return a-b
    elif operator=='*':
        return a*b
    elif operator=='/':
        return a/b
    else:
        return "invalid operator"
result=operations(a,b)
print("the result is:",result)    


# output

# enter two numbers: 5 10
# enter the operator: +
# the result is: 15
# enter two numbers: 5 10
# enter the operator: -
# the result is: -5
# enter two numbers: 5 10
# enter the operator: *
# the result is: 50
# enter two numbers: 5 10
# enter the operator: /
# the result is: 0.5

