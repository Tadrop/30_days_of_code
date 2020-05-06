def unique(L):
    a=[]
    for x in L:
        if x not in a:
            a.append(x)
    print('Sample list:',L)
    print('Unique list:',a)
unique([1,2,3,3,3,3,4,5])
unique([1,2, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 4, 5, 6, 6, 11, 22, 33, 44])
unique([1,2,3,3,3,3,4,5,5,3,3,3,3,4,5,6,6,110,20,19,34])