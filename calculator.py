#  Scientific calculator
import math
while True:
    print("\n\t\t\tChoose The Math Operations\n\n1 -> Additional\n2 -> Subtraction\n3 -> Multiplication\n4 -> Division\n5 -> Modulus\n6 -> Interger Division\n7 -> Raising To A Power\n8 -> Square Root Of A Number\n9 -> Logarithm\n10 -> Sin\n11 -> Cosine\n12 -> Tangent\n")
    
    # Prompt the user for an operation
    operation = input("Enter your option from the menu: ")

    # Check the users choice/operation
    # Addition
    if operation == "1":
        print("\t\t\tAddition")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
        
    # Subration
    elif operation == "2":
        print("\t\t\tSubtraction")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of {num1} - {num2} is {num1 - num2}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    # Multiplication
    elif operation == "3":
        print("\t\t\tMultiplication")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of {num1} X {num2} is {num1 * num2}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    # Division
    elif operation == "4":
        print("\t\t\tDivision")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of {num1} / {num2} is {num1 / num2}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
        
    # Modulus
    elif operation == "5":
        print("\t\t\tModulus")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of {num1} - {num2} is {num1 - num2}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
        
    # Interger Division
    elif operation == "6":
        print("\t\t\tInterger Division")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of {num1} // {num2} is {num1 // num2}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    # Raising to power
    elif operation == "7":
        print("\t\t\tRaising to power")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result of {num1} ** {num2} is {num1 ** num2}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    # Square root
    elif operation == "8":
        print("\t\t\tSquare root")
        num = float(input("Enter a number to calculate the square root: "))
        print(f"The square root of {num} is {math.sqrt(num)}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    # Logarithm
    elif operation == "9":
        print("\t\t\tLogarithm")
        num = float(input("Enter a number to calculate the Logarithm to base 2: "))
        print(f"The log of of {num} is {math.log(num, 2)}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    # Sin
    elif operation == "10":
        print("\t\t\tSin")
        num = float(input("Enter a number(In Degress) to calculate its Sin: "))
        print(f"The Sin of {num} is {round(math.sin(math.radians(num)))}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    # Cosine
    elif operation == "11":
        print("\t\t\tCosine")
        num = float(input("Enter a number(In Degress) to calculate its Cosine: "))
        print(f"The Cosine of {num} is {round(math.cos(math.radians(num)))}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    # Tangent
    elif operation == "12":
        print("\t\t\tTangent")
        num = float(input("Enter a number(In Degress) to calculate its Tangent: "))
        print(f"The Tangent of {num} is {round(math.tan(math.radians(num)))}")
        
        # Go back to the menu or exit the program
        back = input("\nGo Back To The Main Menu? (y/n): ")
        
        if back.lower() == "y":
            continue
        else:
            break
    else:
        print("\nInvalid choice please try again !!!")
  
    