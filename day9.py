def fibSum(number):
    if not isinstance(number,int):
        return  'Invalid input, number must be positive integer'
    if number == 0 :
        return 0
    elif number < 0:
        return "Invalid, number can't be negative"
    elif number > 0:
        pass
    num =0
    a,c=0,1
    while c>=number:
        a,c= c, a+c
        if (c%2) == 0 :
            number+=c
    return number
print(fibSum(10))
print(fibSum(0))
print(fibSum(-3))
print(fibSum('a'))
