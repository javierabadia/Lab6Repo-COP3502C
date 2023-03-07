def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")


def encode(password):
    encoded_password = ""
    for number in password:
        if int(number) >= 7:
            encoded_password += str((int(number) + 3) - 10)
        else:
            encoded_password += str(int(number) + 3)
    return encoded_password


def main():
    option = 0
    while option != 3:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter a password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}\n")


if __name__ == '__main__':
    main()
