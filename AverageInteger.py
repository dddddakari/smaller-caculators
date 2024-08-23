# DEFINING THE NUMBER AND DIVIDING IT
def sum_average(numby):
    return (numby + 1) / 2


# USER INPUT
numby =int(input("Please Enter a number: "))

# TAKING THE RESULT AND ASSIGNING IT A VARIABLE THEN PRINTING
result=sum_average(numby)
print("The average of all numbers from 1 to {} is {}".format(numby,result))