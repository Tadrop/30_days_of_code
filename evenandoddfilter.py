#Even and Odd Number Filter
def even_odd(num_list):
    string=[x for x in num_list if x %2==0]
    print('Even numbers in the list are ',len(string))
    strings=[y for y in num_list if y%2!=0]
    print( 'Odd numbers in the list are', len(strings))
even_odd([1,2,3,4,5,6,7,8,9,10,18])
even_odd(range(10,15))
