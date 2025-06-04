import os 
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as r:
        while True:
            data = r.read(65536)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def check_integrity(directory):
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f'Diretory {directory} does not exist')
        return 

    for root, dirs, files in os.walk(directory):
        for file_name in files: 
            file_path = os.path.join(root, file_name) 
            calculated_hash = calculate_sha256(file_path)
            print(f"File: {file_path}\nSHA-256 Hash: {calculated_hash}\n ")

if __name__ == "__main__":
    directory_to_check =  input("Enter the directory path to check integrity: ")
    check_integrity(directory_to_check)