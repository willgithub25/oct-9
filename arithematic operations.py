# Read two numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform arithmetic operations
sum_result = a + b
difference_result = a - b
product_result = a * b

# Check if b is not 0 to avoid division by zero
if b != 0:
    division_result = a / b
else:
    division_result = "Cannot divide by zero"

# Print the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")
