import random
import string

def generate_password(length: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input(f"Enter your desired password length: "))
    
    if password_length < 1:
        print("password length must be atleast 1 character")
    else:
        generated_password = generate_password(password_length)
        print(f"Generated Password: {generated_password}")