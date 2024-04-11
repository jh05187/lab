def menu():
    print("Menu")
    print("---------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(n):
    my_list = []
    new_list = []
    str_out = ''
    for i in n:
        my_list.append(int(i))

    for num in my_list:
        if num < 7:
            new_list.append(num+3)
        else:
            new_list.append((num+3)%10)

    for num in new_list:
        str_out += str(num)

    return str_out
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