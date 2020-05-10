def fibSum(num):
    if not isinstance(num,int):
        return  'Invalid input, number must be positive integer'
    if num == 0 :
        return 0
    elif num < 0:
        return "Invalid, number can't be negative"
    elif num > 0:
        pass
    number =0
    a,c=0,1
    while c>=num:
        a,c= c, a+c
        if (c%2) == 0 :
            num+=c
    return num
print(fibSum(10))
print(fibSum(0))
print(fibSum(-3))
print(fibSum('a'))
