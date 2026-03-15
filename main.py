from password_generator import generate_password

def main():
    print("Welcome to the Secure Password Manager!\n")
    password = generate_password(16)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()