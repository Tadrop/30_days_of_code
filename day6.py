def primeSum(x):
    n=x
    sum=0
    for a in range(2,n+1):
        b=1
        for b in range(2,a):
            if (a%b)==0:
                b=a
                break
        if b is not a:
            sum+=a
    return sum
print(primeSum(10))
print(primeSum(20))
print(primeSum(100))