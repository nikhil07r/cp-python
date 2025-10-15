def maketea():
    print("Making tea")
maketea()    

def makecoffe(name):
    print("Making coffee for" , name)
makecoffe("Nikhil")    


def makecoffe(name):
    print("Making coffee for" , name)
makecoffe(1)    

# write a program to print the square of the number take input from user .
num = int(input("Enter a number: "))
def square(num):
    return num * num
print()

# write a function to print square of a number from x to y
def print_squares(x, y):
    for i in range(x, y + 1):
        print(f"The square of {i} is {i * i}")
        