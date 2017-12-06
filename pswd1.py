while True:

    x=input(" Create a PASSWORD :  ")
    if len(x) <= 6 or len(x) >= 10:
        print("ENTER THE PASSWORD LENGTH BETWEEN 6 AND 10")
    else:
        break

while True:
    pswd=input("Please give your password to enter the system:    ")
    if pswd == x:
        print("thanks for entering the password \n Welcome to P Y T H O N  world !!!")


        print("Welcome to the world of Calculation")
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
            division = num_1 / num_2
            print("division", division)
        else:
            print("Invalid Input")
        break
    else:
        print("Invalid Password")
