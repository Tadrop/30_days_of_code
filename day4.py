def string_test(x):
    upper=0
    lower=0
    for y in x:
        if y.isupper():
            upper+=1
        elif y.islower():
            lower+=1
        else:
            pass
    print('Number of Lowercase letters is', lower)
    print('Number of Uppercase letters is', upper)
string_test('The quick Brown Fox')
string_test('My name is Sodiq Agunbiade,I am your tutor for this cohort')
string_test('You are a Student of 30daysofcode')



