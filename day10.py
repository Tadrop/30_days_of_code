def fibonacci(number):
    if not isinstance(number,int):
        return 'Invalid'
    elif number <0:
        return 'Wrong input'
    a,b=0,1
    while a<10000000000000000000000000000000000000000000000000000000000000000000000000:
        a,b=b,a+b
        if number == a:
            return True
print(fibonacci(13))
print(fibonacci(-5))
print(fibonacci('a'))
