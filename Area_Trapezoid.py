# Defining and asking for input of what the parellel sides will be and what the height of the trapezoid is #
a = float(input("Please enter parellel a? "))
b = float(input("Please enter parellel b? "))
h = float(input("Please enter the sum of the height? "))

# Making sure that no negative numbers are inputted because those would be invalid in this formula #
while a>0 and b>0 and a==b and h>0:
    trapezoidArea = ((a+b) * h) / 2
    print("The Area of this trapezoid is ", trapezoidArea)
# To make sure the while statement doesn't loop forever #
    break
# Failsafe incase the parellel sides are not the same length #
else:
    print("Uh Oh! These numbers are invalid, Please Try Again.")



