import random
import string

def generate_password(length,complexity):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if complexity == 1:
        char_set = lowercase
    elif complexity == 2:
        char_set = lowercase + uppercase
    elif complexity == 3:
        char_set = lowercase + uppercase + digits

    elif complexity == 4:
        char_set = lowercase + uppercase + digits + symbols
    else:
        raise ValueError("Complexity must be between 1 and 4")
    
    password = ''.join(random.choice(char_set)for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password:"))
    print("Complexity levels:\n1. Lowercase only\n2. Lowercase and Uppercase\n3. Lowercase, Uppercase, and Digits\n4. Lowercase, Uppercase, Digits, and Symbols")
    complexity = int(input("Enter the complexity level (1-4): "))

    if length <= 0:
        print("password length should be a positive integer!!!!....")
        return
    
    if complexity not in [1,2,3,4]:
        print("Invalid complexity level!!.. Please enter a value between 1 and 4..")
        return
    password = generate_password(length,complexity)

    print(f"generated password : {password}")

if __name__ == "__main__":
    main()