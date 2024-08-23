# Asking for how many numbers will be entered: for this example it is 5 #
num = int(input("How many numbers are you entering ?  "))

# Including a counter so that this sequence doesn't go on continously #
counter = 0
total = 0

# Letting the numbers continue until the 'num' is reached #
while counter<num:
    sum= float(input("Please enter your numbers "))
# Adding the sum to the total and making sure the counter goes up one ever time #
    total +=sum
    counter+=1
# Once it reaches it destined equivalency (counter matching up 'num' at the top) print the average plus the explanation asked for in the word doc #
if counter==num:
    print("Your average is", total / counter, "because the sum of your numbers is", total, "and", total, "divided by the amount of the numbers you entered", total / counter )
# Makinng sure that program will end regardless of what happens #
else:
    print("Uh Oh! Your entry is valid")
