def is_perfect_square(x):
    if x % x**0.5 ==0:
        return True
    else:
        return False
print(is_perfect_square(9))
print(is_perfect_square(100))
print(is_perfect_square(225))
print(is_perfect_square(500))