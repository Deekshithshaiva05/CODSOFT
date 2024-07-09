def add(input1, input2):
    print(f"The ADDITION of {input1} and {input2} is: {input1 + input2}")

def sub(input1, input2):
    print(f"The SUBTRACTION of {input1} and {input2} is: {input1 - input2}")

def mul(input1, input2):
    print(f"The MULTIPLICATION of {input1} and {input2} is: {input1 * input2}")

def div(input1, input2):
    if input2 != 0:
        print(f"The DIVISION of {input1} and {input2} is: {input1 / input2}")
    else:
        print("Error! Division by zero.")

def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))

    if choice == '1':
        add(input1, input2)
    elif choice == '2':
        sub(input1, input2)
    elif choice == '3':
        mul(input1, input2)
    elif choice == '4':
        div(input1, input2)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
