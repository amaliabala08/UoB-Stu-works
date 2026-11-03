#exccercise 1o in workbook 8
my_list = [1, 2, 3, 4, 5]
check = 3 in my_list
print(check)  # Output: True
check = 10 not in my_list
print(check)  # Output: True

a=[1,2]
b=[1,2]

check = a is b
print(check)  # Output: False, because a and b are different objects in memory
check = a == b
print(check)  # Output: True, because a and b have the same content
