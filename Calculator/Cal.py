#Calculator:
operator = input("Enter an operator (+ - * / ): ")
number1 = float(input("Enter the 1st number: "))
number2 = float(input("Enter the 2nd number: "))
if operator == "+":       #comparison operator(==)
 result = number1 + number2
 print(f"Your result is: {result}")
elif operator == "-":
 result = number1 - number2
 print(f"Your result is: {result}")
elif operator == "*":
 result = number1 * number2
 print(f"Your result is: {result}")
elif operator == "/":
 number2 >= 1
 result = number1 / number2
 print(f"Your result is {result}")
else:
 print("Try again later")