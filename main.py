from password_generator import generate_password

from encryption import generate_key, generate_salt, encrypt_password, decrypt_password




def main():
    print("Welcome to the Secure Password Manager!\n")
    password = generate_password(16) 
    print(f"Generated Password: {password}")
    
    master_password = input("Enter your master password: ")
    salt = generate_salt()
    key = generate_key(master_password, salt)
    secret_password = input("Enter the password you want to encrypt: ")
    encrypted_password = encrypt_password(secret_password, key)
    decrypt_password(encrypted_password, key)
    print(f"Encrypted Password: {encrypted_password}")
    
if __name__ == "__main__": 
    main()