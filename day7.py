def averageMultiple(x):
    n1=x
    sum=0
    length=0
    for a in range(1 ,n1):
           if (a%3) ==0 or (a%5)==0:
              sum+=a
              length+=1
    return (sum/length)
print(averageMultiple(10))
print(averageMultiple(20))

