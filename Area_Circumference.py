# Defining the variables as their own #
r = float(input("PLease Insert a radius: "))
C = (2*3.14159*r)
A = (3.14159*r*2)

# Making sure tà avoid having an undefined number inputted #
if r>0:
    # Printing the final Circumference and Area -- Making sure to format it to two numbers after the decimal #
    print(f"The Circumference is {C:.2f}", f"and the Area is {A:.2f}")
# Ending the sequence properly #
else:
    print("Your Number is invaid!")