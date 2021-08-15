"""
Q3)[PRACTICAL] Write a menu driven program to do the following:-
   a) To create a binary file 'product.dat' in the following format :
    {‘name’ : ‘file’, ‘price’ : 112}, {‘name’ : ‘pen’, ‘price’ : 30}, etc.
   b) To display the above file
   c) Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than 100.
"""


import pickle


def create():
    file = open("product.dat", "wb")
    while input("Do You Want to Enter more values (y/n): ").lower() == "y":
        print()
        pickle.dump({
            "name": input("Enter product name: "),
            "price": float(input("Enter price: "))
        }, file)
    file.close()


def read(file_name):
    try:
        file = open(file_name, "rb")
    except FileNotFoundError:
        print("File does not exist, you need to create it first.")

    lis = []
    try:
        while True:
            lis.append(pickle.load(file))
    except EOFError:
        file.close()


def display():
    sfile = read("product.dat")
    for item in sfile:
        print(f"cost of 1 {item['name']} is {item['price']}")


def transfer():
    new_file = open("new.dat", "wb")
    sfile = read("product.dat")
    for i in sfile:
        if i["price"] < 100:
            pickle.dump(i, new_file)
    new_file.close()


def display_new():
    sfile = read("new.dat")
    for i in sfile:
        print(f"cost of 1 {i['name']} is {i['price']}")



while True:
    print("\n"
            "1: Create File",
            "2: Display File",
            "3: Transfer contents to a new file",
            "4: Display New File",
            "5: Exit", sep="\n")
    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        create()
    elif user_choice == "2":
        display()
    elif user_choice == "3":
        transfer()
    elif user_choice == "4":
        display_new()
    elif user_choice == "5":
        break
    else:
        print("Invalid choice")


