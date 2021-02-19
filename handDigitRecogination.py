lis = [1,2,3,4,5,6,7,8,9]

val = [True,False,True,False,True,True,True,False,True]

for i in range (len(val)):
    if val[i] is False:
        print(val[i], i)