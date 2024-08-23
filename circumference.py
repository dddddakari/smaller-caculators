
def main():
   # USER INPUT
   radius = int(input("What is the radius of this circle: "))
   # DEFINING 
   pi = 3.14159
   r = radius
   c = 2*pi*r
   # PRINTING THE C
   print(2*pi*r)
   a = pi*r*r
    # PRINTING THE R
   print(pi*r*r)
   return( c / a)

# PRINTING THE FINAL EQUATION
ratio = main()
print("the ratio of the circumference to the area is",ratio)    