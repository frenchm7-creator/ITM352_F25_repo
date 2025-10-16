# Algorithm for multiplying two numbers

def multiply(x, y):
    # Convert inputs to integers in case they are strings
    x = int(x)
    y = int(y)
    product = 0
    for _ in range(y):
        product += x
    return product

first = input("Enter the first number: ")
second = input("Enter the second number: ")
prod = multiply(first, second)

print(f"The product of {first}, {second} is {prod}")

