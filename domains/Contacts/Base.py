from Menu import welcome
from Operations import new, all, update_name, update_number, search_name, search_number, delete

print("Welcome to Mobile Contact Management")
while True:
    inn = welcome()
    if inn=='2':
        new()
    elif inn=='1':
        all()
    elif inn=='3':
        while True:
            i = input("--------------------------\nEdit\n1. Name\n2. Number\nEnter your option: ")
            if i == '1':
                update_name()
                break
            elif i == '2':
                update_number()
                break
            else:
                print("Unknown, select your option again")
    elif inn=='4':
        while True:
            i = input("--------------------------\nSearch\n1. Name\n2. Number\nEnter your option: ")
            if i=='1':
                search_name()
                break
            elif i == '2':
                search_number()
                break
            else:
                print("Unknown, select your option again")
    elif inn=='5':
        delete()
    elif inn=='6':
        print('VISIT AGAIN!!')
        break