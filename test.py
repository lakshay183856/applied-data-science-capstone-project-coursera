# Input a float value for variable a
a = float(input("First value: "))
# Input a float value for variable b
b = float(input("Second value: "))
# Output the result of addition
print("Addition:", a + b)
# Output the result of subtraction
print("Subtraction:", a - b)
# Output the result of multiplication
print("Multiplication:", a * b)
# Output the result of division (with zero check)
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Error (cannot divide by zero)")
print("\nThat's all, folks!")
