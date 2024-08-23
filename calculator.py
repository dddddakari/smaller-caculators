# ADDITION
def add(num1, num2):
    return num1 + num2
 
# SUBSTRACT
def subtract(num1, num2):
    return num1 - num2
 
# MULTIPLY 
def multiply(num1, num2):
    return num1 * num2
 
# DIVIDE 
def divide(num1, num2):
    return num1 / num2
 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 
 
# USER INPUT
select = int(input("Select operations form 1, 2, 3 or 4: "))
 
number_1 = int(input("Please enter your first number: "))
number_2 = int(input("PLease enter your second number: "))

# WHICHEVER IS CHOSEN COMPLETES THE INPUT
 
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
 
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")