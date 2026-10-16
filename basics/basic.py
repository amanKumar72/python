# if else
isTrue = True if 10 != 10 else False
print(isTrue)


# zip -> conbiner the lists for pairs or combine them into list of tuples
# enumerate -> give index of the list element and its value 
items = ['laptop' , 'mouse', 'keyboard']
prices = [30000, 1000, 2000]

# Using zip()
for item, price in zip(items, prices):
    print(f"Item: {item}, Price: {price}")

# Using enumerate()
for index, item in enumerate(items):
    print(f"Index: {index}, Item: {item}")

# loop fallback with else -> else code executes if the loop is not terminated with break 
for i in range(5):
    if i == 3:
        print(i)
else:
    print("Loop completed successfully")


# walrus operator => := (can be used for conditional expressions and in loops also)
a = 10
if (b := a + 5) > 10:
    print(b)

# 
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user['id']} paid {user['total']} and got discount for next visit of rupees {discount}")



# functions

def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet("Aman", "Good Morning")

# default arguments
def ask(question, retries=2):
    answer = input(question)
    while answer.lower() not in ["y", "n"] and retries > 0:
        answer = input(question)
        retries -= 1
    return answer

a = ask("Do you want to continue? ")
print(a)

# *args and **kwargs
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Aman", age=30, city="Delhi")

# lambda function
square = lambda x: x * x
print(square(5))

def apply_func(func, value):
    return func(value)

print(apply_func(square, 5))

# lambda with map, filter, reduce
numbers = [1, 2, 3, 4, 5]

# Using map() with lambda
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

# Using filter() with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using reduce() with lambda
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)


# global and nonlocal
x = 10

def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
        print("inside inner:", x)
    inner()
    print("inside outer:", x)

outer()
print("outside:", x)


