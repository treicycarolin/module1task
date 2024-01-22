print("Part 1 \n")
number1 = float(input("Enter a first number : "))
number2 = float(input("Enter a second number : "))

addition_total = number1 + number2
print(f"Addition of {number1} + {number2} is {addition_total}")

subtraction_total = number1 - number2
print(f"Subtraction of {number1} - {number2} is {subtraction_total}")

print("\nPart 2 \n")
number1 = float(input("Enter a first number : "))
number2 = float(input("Enter a second number : "))

multiplication_total = number1 * number2
print(f"Multiplication of {number1} * {number2} is {multiplication_total}")

if number2 != 0:
  division_total = number1 / number2
  print(f"Division of {number1} / {number2} is {division_total}")
else:
  print("Cannot divide by zero.")
