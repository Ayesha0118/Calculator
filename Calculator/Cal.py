#   SIMPLE CALCULATOR
while True:
    print("Select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice(1/2/3/4):\n")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the First number:\n"))
        num2 = float(input("Enter the Second number:\n"))

        if choice == '1':
            print(num1 + num2)
        elif choice == '2':
            print(num1 - num2)
        elif choice == '3':
            print(num1 * num2)
        elif choice == '4':
            print(num1 / num2)

        next_calculation = input("Let's do next calculation? (y/n)\n")

        if next_calculation == 'n':
            break

        elif next_calculation == 'y':
           continue

        else:
            print("Invalid input")
            break





