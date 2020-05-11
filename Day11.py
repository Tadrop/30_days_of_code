def squareSum(number):
    if not isinstance(number,int):
        return 'Invalid'
    if number<0:
        return 'Wrong input'
    save=0
    saves=0
    for number in range(number+1):
        square=(number**2)
        save+=square
    for number in range(number+1):
        saves+=(number)
        sumsquare =(saves**2)
    return sumsquare-save
print(squareSum(10))
print(squareSum('a'))
print(squareSum(-19))

