#Even and Odd Number Filter
def even_odd(num_list):
    string=[x for x in num_list if x %2==0]
    return 'Even numbers in the list are ',len(string)
print(even_odd([1,2,3,4,5,6,7,8,9,10,18]))
print(even_odd(range(10,15)))
def even_odd(num_list):
    strings=[y for y in num_list if y%2!=0]
    return 'Odd numbers in the list are', len(strings)
print(even_odd([1,2,3,4,5,6,7,8,9,10,18]))
print(even_odd(range(10,15)))

