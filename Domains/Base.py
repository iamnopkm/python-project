import sqlite3
debase = sqlite3.connect('contacts.db')
debase.execute('create table if not exists' + ' contact(name text,contact text)')
cur=debase.cursor()

def welcome():
    inn = input("--------------------------------\n1. All\n2. New\n3. Edit\n4. Search\n5. Delete\n6. Exit\n--------------------------------\nSelect your option: ")
    return inn.lower()
def check(sname):
    print('--------------------------------')
    cur.execute(f'Select name from contact where name="{sname}"')
    return bool(obj := cur.fetchone())
def valid_no(sname):
    while True:
        scontact = input(f"Enter {sname}'s phone no: ")
        if len(scontact) in {10, 8}:
            return scontact
        else:
            print("Number is invalid.")

def delete():
    print('--------------------------------')
    sname = input('Enter the name to be deleted: ')
    sname = sname.title()
    if check(sname):
        cur.execute(f"Delete from contact where name='{sname}'")
        print("Delete successful")
    else:
        print(f"No contact exist named '{sname}'")
    debase.commit()
def new():
    print('--------------------------------')
    sname = input("Enter new contact name: ")
    sname = sname.title()
    contact=valid_no(sname)
    cur.execute('Insert into contact values(?,?)',
                (f'{sname}', f'{contact}'))
    print("New contact added!")
    debase.commit()
def all():
    print('--------------------------------')
    cur.execute('Select * from contact')
    obj = cur.fetchall()
    if obj is None:
        print("No contact exist!")
    for a in obj:
        print('Name: ', a[0], ' Phone: ', a[1])
    debase.commit()


def update_number():
    print('--------------------------------')
    sname = input("Enter the contact name to be updated: ")
    sname = sname.title()
    if check(sname):
        contact = valid_no(sname)
        cur.execute(f'Update contact set contact="{contact}" where name="{sname}"')
        print("Update successful")
    else:
        print(f"No contact exist named {sname}")
    debase.commit()


def update_name():
    print('--------------------------------')
    snum = input("Enter the contact number to be edited: ")
    sname = input("Enter the new contact name: ")
    cur.execute(f'Select name from contact where contact="{snum}"')
    if obj := cur.fetchone():
        cur.execute(f'Update contact set name="{sname.title()}" where contact="{snum}"')
        print("Update successful")
    else:
        print(f"No contact exist which has number: {snum}")
    debase.commit()

def search_number():
    print('--------------------------------')
    snum = input("Enter the contact number to be searched: ")
    cur.execute(f'Select name from contact where contact like "%{snum}%"')
    if obj := cur.fetchone():
        obj = obj[0]
        print("Name: ", obj)
        cur.execute(f'Select contact from contact where name="{obj}"')
        obj = cur.fetchone()
        print("Contact: ", obj[0])
    else:
        print(f"No contact exist which has number: {snum}")
    debase.commit()

def search_name():
    print('--------------------------------')
    sname = input("Enter the contact name to be searched: ")
    cur.execute(f'select name from contact where name like "%{sname}%"')
    if obj := cur.fetchone():
        obj = obj[0]
        print("Name: ",obj)
        cur.execute(f'select contact from contact where name="{obj}"')
        obj=cur.fetchone()
        print("Contact: ",obj[0])
    else:
        print(f"No contact exist which named: {sname}")
    debase.commit()


#main
print("WELCOME to Mobile Contact Management System")
while True:
    inn = welcome()
    if inn=='2':
        new()
    elif inn=='1':
        all()
    elif inn=='3':
        while True:
            i = input("--------------------------\nEdit\n1. Name\n2. Number\nEnter your options: ")
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
            i = input("--------------------------\nSearch\n1. Name\n2. Number\nEnter your options: ")
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

debase.close()



