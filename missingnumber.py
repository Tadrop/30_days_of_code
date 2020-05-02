def missing_number(num_list):
    return [x for x in range(num_list[0],num_list[-1]+1) if x not in num_list]
print(missing_number([1,2,3,4,6,7,10]))
print(missing_number([10,11,12,14,17]))