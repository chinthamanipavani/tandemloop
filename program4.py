l=list(map(int,input("enter list ").split()))
def count(l):
    d={}
    for j in l:
        for i in range(1,10):
            if j%i==0:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
    return d
d=count(l)                
print(d)                    


# output
# enter list 1 2 8 9 12 46 76 82 15 20 30
# {1: 11, 2: 8, 4: 4, 8: 1, 3: 4, 9: 1, 6: 2, 5: 3}


