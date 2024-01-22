# module1task
Module 1 assignment principles of programming

### Description
This Python program consists of two parts. In the first part, it prompts the user to input two numbers, performs addition and subtraction on them, and then displays the results. The second part does a similar operation, prompting the user for two numbers, performing multiplication and division, and outputting the corresponding results. The code ensures that division by zero is handled appropriately.

---

## Pseudocode

### Part 1:
1. **Start**
2. Display "Enter the first number:"
3. Read `number1` from user input
4. Display "Enter the second number:"
5. Read `number2` from user input
6. `addition_total` = `number1` + `number2`
7. `subtraction_total` = `number1` - `number2`
8. Display "Addition of `number1` + `number2` is `addition_total`"
9. Display "Subtraction of `number1` - `number2` is `subtraction_total`"
10. **End**

### Part 2:
1. **Start**
2. Display "Enter the first number:"
3. Read `number1` from user input
4. Display "Enter the second number:"
5. Read `number2` from user input
6. `multiplication_total` = `number1` * `number2`
7. If `number2` is not equal to 0:
   - `division_total` = `number1` / `number2`
   - Display "Multiplication of `number1` * `number2` is `multiplication_total`"
   - Display "Division of `number1` / `number2` is `division_total`"
   Else:
   - Display "Cannot divide by zero."
8. **End**
