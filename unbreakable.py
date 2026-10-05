# unbreakable.py
# Demonstrates robust input validation using try-except blocks.

def get_user_age():
    while True:
        user_input = input("Enter your age: ")
        try:
            age = int(user_input)
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            return age
        except ValueError:
            print("Not a number. Please enter a valid integer.")

if __name__ == "__main__":
    print("Welcome to the unbreakable age checker!")
    valid_age = get_user_age()
    print(f"Success! Your registered age is: {valid_age}")
