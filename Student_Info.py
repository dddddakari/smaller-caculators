# Defining and asking for an input on all items needed #
fName = str(input("What is your first name? "))
lName = str(input("What is your last name? "))
Age = int(input("What is your age? "))
baby_GAP = float(input("What is your GPA? "))
major = str(input("What is your major? "))
address = str(input("What is your address? "))

# Creating the welcome greeting with its curly brackets and formating it to put what is needed where it needs to be #

welcome = "Welcome {} {}, you are {} years old, majoring in {} with a {} GPA and you live at {} :)!".format(fName ,lName ,Age, major, baby_GAP, address)

# Printing the final greeting #

print(welcome)

# dont worry babe, I'll finish it for you ;) - past derek #