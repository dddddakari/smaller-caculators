numberOne = int(input("PLease Input your First Number  "))
numberTwo = int(input("PLease Input your Second Number  "))

if numberOne > numberTwo:
    print(numberOne," is Larger than", numberTwo)
elif numberTwo > numberOne:
    print(numberTwo," is Larger than", numberOne)
elif numberOne == numberTwo:
    print("These Integers are equal.")
else:
    print("These numbers are invalid.")
