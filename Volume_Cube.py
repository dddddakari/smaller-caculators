# Making Length a Variable and allowing user to input their own number - even if they only enter 4 #

L = int(input("Please Enter The Length? "))

# Making sure that no invalid numbers have been inputted by making length GREATER THAN 0 #
if L>0:
    V = (L)**3
# Setting V as a variable and also calculating the volume of the given input #
    print("The Volume of this cube is", V, "!")

# Making sure that no invalid numbers have been inputted by making length GREATER THAN 0 #
else:
    print("This Number is not valid!")