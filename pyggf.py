# def validate_pin(pin):
#     pin_number = str(pin)
#     return(len(pin_number) == 4 or len(pin_number) == 6) and pin_number.isdigit()

# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     masked = "#" * (len(cc) - 4) + cc[-4:]
#     return masked

import hashlib


def crack_hash(inputpass):
    try:
        passfile = open('test.txt', 'r')
    except:
        print("Could not find file.")
    
    for passwords in passfile:
        encPass = passwords.encode('utf-8')
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputpass:
            print(f"password Found: {passwords}")

if __name__ == '__main__':
    crack_hash()
    


