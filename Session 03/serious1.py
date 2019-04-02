inventory=["T-shirt","Sweater"]

for i in inventory:
    n = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    if n == "R":
        print("Our items: ",inventory)
    elif n == "C":
        a = input("Enter new items: ")
        inventory.append(a)
        print("Our items:", inventory)
    elif n == "U":
        b = int(input("Update position: "))
        c = input("New item? ")
        inventory[b-1]=c
        print("Our items:", inventory)
    elif n == "D":
        d = int(input("Delete position? "))
        del inventory[d-1]
        print("Our items:", inventory)

