import hashlib
import getpass

password_manager =()

def create_account():
    username = input('Enter your desired username: ')
    password = getpass.getpass('Enter your desired password: ')
    hashed_password = hashlib.sha3_256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    return "Account created successfully"

def login():
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your desired password: ')
    hashed_password = hashlib.sha3_256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        return "Login successful"
    else:
        return "Invalid username or password"
    
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login and 0 to exit: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '0':
            break
        else:
            return 'Invalid choice' 
               
if __name__ == "__main__":
    main()