import random
import string

while True:
    password = ""
    print("1. Only numbers")
    print("2. Only letters")
    print("3. letters + numbers")
    print("4. numbers + letters + symbols")
    choice = input("Enter your choice :").lower()

    if choice == "1" or choice == "very easy":
        characters = string.digits
    elif choice == "2" or choice == "easy":
        characters = string.ascii_letters
    elif choice == "3" or choice == "hard":
        characters = string.ascii_letters + string.digits
    elif choice == "4" or choice == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("invalid choice")
        continue

    l = int(input("Enter password length :"))
    if l <= 0:
        print("Password lenght must be greater than 0:")
        continue

    for i in range(0, l):
        char = random.choice(characters)
        password += char

    print(f"Here is you password = {password}")

    print("hey,Do you want to genrate another password Y/N")

    again = input("generate another password").lower()

    if again == "y":
        continue
    elif again == "n":
        print("Thank you for using password generator!")
        break
    else:
        print("invalid choice")
        break