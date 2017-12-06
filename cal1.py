# Program of simple calculaton;

print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")

choice = input("enter choice :   ")

num_1 = float(input("enter the num_1=  "))
num_2 = float(input("enter the num_2=  "))

if choice == "+":
    addition = num_1 + num_2
    print("addition", addition)
elif choice == "-":
    subtraction = num_1 - num_2
    print("subtraction", subtraction)
elif choice == "*":
    multiplication = num_1 * num_2
    print("multiplication", multiplication)
elif choice == "/":
    division =num_1 / num_2
    print("division", division)
else:
    print("Invalid Input")