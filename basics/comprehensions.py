# comprehensions
# types of comprehesions

# List

# [exp for item in iterable if condition]
fruits = ["apple", "banana", "cherry", "dates", "elderberry"]
print([fruit for fruit in fruits if len(fruit) > 5])

# Set
# {exp for item in iterable if condition}

numbers = [-1, 1, -2, 3, -4, 5]
print({num * num for num in numbers})

# dictionary
# {key: value for item in iterable if condition}
users = [{"name": "Aman", "age": 10}, {"name": "John", "age": 25}, {"name": "Jane", "age": 28}]
print({user["name"]: user["age"] for user in users if user["age"] > 18})


# generator => used when we want to iterate over a large dataset but want to save memory space
# (exp for item in iterable if condition)
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)