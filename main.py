print('''
      ---------------------------------
      Welcome To Maheshwari Electronics
      ---------------------------------
      1. View List
      2. Buy Items
      3. Exit
      ''')

choice = int(input("Enter Your Option = "))
if choice == 1:
    print("-----------------------------------------")
    print("Items Available In Maheshwari Electronics")
    data = open("inventory.txt", "r")
    items = data.readlines()
    print("------------------------------------------")
    for item in items:
        name, price, count = item.split(",")
        print("{0}\t\t{1}\t{2}".format(name, price, count))
        print("--------------------------------------")
elif choice == 2:
    print("Welcome to Buy Items")
else:
    print("Exit")