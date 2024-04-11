def menu():
    print("Menu")
    print("---------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(passcode, newpass):
    for i in range(0, len(passcode)):
        newpass += str(int(passcode[i]) + 3)
        print("Your password has been encoded and stored!")
def decode(passcode, newpass):
    for i in range(0, len(passcode)):
        newpass += str(int(passcode[i]) - 3)
        print("The encoded password is " + passcode + ", and the original password is " + newpass + ".")

def main():
    while True:
        menu()
        choice = int(input("Please enter an option: "))

        newpass = ""
        if choice == 1:
            passcode = input("Please enter your password to encode: ")
            encode(passcode, newpass)
        if choice == 2:
            passcode = input("Please enter your password to encode: ")
            decode(passcode, newpass)
        if choice == 3:
            return False

if __name__ == '__main__':
    main()