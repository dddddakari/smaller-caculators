firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

if firstNumber % secondNumber == 0:
    print(firstNumber, "is divisible by", secondNumber)
else:
    print(firstNumber, "is not divisible by", secondNumber)
