# uSER INPUT AND RETURNING IT TO BE CALCULATED
def get_input(): 
    b = int(input("Please enter the width of this rectangle: "))
    c = int(input("Please enter the length of this rectangle:"))
    return b, c 
    
# CACLULATING THE AREA
def calculate_area():
    b, c = get_input() 
    c = b * c
    show_area(c)

# THE FINAL PRINTING
def show_area(c):
    print(f"The area of this rectangle is: {c}")


# BRINGING OUT THE CALCULATION
calculate_area() 