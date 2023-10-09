# Read two numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Swap the values of a and b using a temporary variable
temp = a
a = b
b = temp

# Print the swapped values
print(f"After swapping, the first number is: {a}")
print(f"After swapping, the second number is: {b}")
