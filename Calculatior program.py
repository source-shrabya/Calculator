"""I am making a Python Calculator"""


operator = input("Enter an operator (+ - * /)")
num1 = float(input ("Enter a number: "))
num2 = float(input("Enter the second number: "))

if operator == "+" :
    result = num1 + num2
    print(round(result))

elif operator == "-" :
    result = num1 - num2
    print(round(result))
      
elif operator == "*" :
    result = num1 + num2
    print(round(result))

elif operator == "/" :
    result = num1 + num2
    print(round(result))

else :
    print(f"{operator} is not an operator ")

    