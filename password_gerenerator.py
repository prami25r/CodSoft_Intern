import random
import string

def password_generator(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for i in range(length))
    return password

def main():
    print("Password Generator\n")
    

    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("Length should be a positive integer.")
        
        password =password_generator(length)
        print("Generated Password: ", password)

    except ValueError as c:
        print(f"Error: {c}")
    
if __name__ == "__main__":
    main()
