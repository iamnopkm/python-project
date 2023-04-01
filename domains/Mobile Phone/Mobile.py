from Store import Store
from Models import MobilePhone

store = Store("My Phone Store")

while True:
    print("-------------------------------")
    print("-----------Options-------------")
    print("1 - Add phone")
    print("2 - Remove phone")
    print("3 - Search phone")
    print("4 - List phones")
    print("5 - Sell phone")
    print("6 - Restock phone")
    print("0 - Exit")
    choice = input("Enter your option: ")
    
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice. Please enter a number.")
        continue

    if choice == 0:
        break
    elif choice == 1:
        print("-------------------------------")
        name = input("Enter phone name: ")
        brand = input("Enter phone brand: ")
        while True:
            
            try:
                price = float(input("Enter phone price: "))
                break
            except ValueError:
                print("Invalid price. Please enter a number.")
        while True:
            try:
                stock = int(input("Enter phone stock: "))
                break
            except ValueError:
                print("Invalid stock. Please enter a number.")
        phone = MobilePhone(name, brand, price, stock)
        store.add_phone(phone)
        print(f"{phone.brand} {phone.name} added to inventory.")
    elif choice == 2:
        print("-------------------------------")
        name = input("Enter phone name: ")
        phone = store.search_phone(name)
        if phone is None:
            print("Phone not found.")
        else:
            store.remove_phone(phone)
            print(f"{phone.brand} {phone.name} removed from inventory.")
    elif choice == 3:
        print("--------------------------------")
        name = input("Enter phone name: ")
        phone = store.search_phone(name)
        if phone is None:
            print("Phone not found.")
        else:
            print(f"{phone.brand} {phone.name} - ${phone.price} ({phone.stock} in stock)")
    elif choice == 4:
        print("-------------------------------")
        store.list_phones()
    elif choice == 5:
        print("-------------------------------")
        name = input("Enter phone name: ")
        store.sell_phone(name)
    elif choice == 6:
        print("-------------------------------")
        name = input("Enter phone name: ")
        while True:
            try:
                amount = int(input("Enter restock amount: "))
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        store.restock_phone(name, amount)
    else:
        print("-------------------------------")
        print("Invalid choice. Please enter a valid option.")