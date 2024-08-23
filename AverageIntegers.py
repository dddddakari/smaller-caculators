greaterThan = False

num = 0
while greaterThan == False:
    num = int(input("Input a # greater than 1: "))

    if num>1:
        greaterThan = True
    else:
        print("This # isn't greater than 1!")
sum= 0
for num in range(num + 1):
    sum += num

average= sum/ num
print("The average of these # is",average)

def make_list(*args):
        print(args)
        list1 =[*args]
        list2 = list(args)


        print(list1, list2)

make_list("Mary", "Mike", "Anna")
