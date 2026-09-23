
# [expression for variable in iterable]
numbers = [i for i in range(1, 6)]
print(numbers)


#doing something
squares = [num ** 2 for num in numbers]


# [expression for variable in iterable if condition]
even = [num for num in numbers if num % 2 == 0]


#combination
result = [num ** 2 for num in numbers if num % 2 == 0]


#string comprehention
result = "".join([char.upper() for char in name])


#dict comprehentions
# {key: value for variable in iterable}

squares = {num: num ** 2 for num in range(1, 6)}


#in case of else
result = [
    "Even" if num % 2 == 0 else "Odd"
    for num in numbers
]


# List
# [expression for item in iterable]
# List + condition
# [expression for item in iterable if condition]
# List + if/else
# [value_if_true if condition else value_if_false for item in iterable]
# Dictionary
# {key: value for item in iterable}
# Dictionary + condition
# {key: value for item in iterable if condition}
# String processing
# "".join([expression for char in string])