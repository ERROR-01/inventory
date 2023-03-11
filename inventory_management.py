"""inventory management that can update, search, delete, add, and view all"""
import csv


def open_database():
    with open("inventory.csv", "r") as f:
        reader = csv.DictReader(f)
        full_products = []
        product_names = []
        for i in reader:
            full_products.append(i)
            product_names.append(i["product"])
    return full_products, product_names


def write_database(full_products=[]):
    with open("inventory.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["product", "price", "quantity"])
        writer.writeheader()
        writer.writerows(full_products)


def search():
    full_products, product_names = open_database()
    product_search = input("\nwhat product would you like to find?: ")
    if product_search in product_names:
        for i in full_products:
            if i["product"] == product_search:
                print(f"product: {i['product']}")
                print(f"price: ${float(i['price']):.2f}")
                print(f"quantity: {i['quantity']}")
    else:
        print("product not found!")


def update():
    full_products, product_names = open_database()
    product_search = input("\nwhat product would you like to update?: ")
    if product_search in product_names:
        for index, i in enumerate(full_products):
            if i["product"] == product_search:
                price = input("enter the new price: ")
                quantity = input("enter the new quantity: ")
                full_products[index] = {"product": product_search, "price": price, "quantity": quantity}
                write_database(full_products)
                print("product successfully updated!")
    else:
        print("product not found")


def delete():
    full_products, product_names = open_database()
    product_search = input("\nwhat product would you like to delete?: ")
    if product_search in product_names:
        full_products = [i for index, i in enumerate(full_products) if i["product"] != product_search]
        write_database(full_products)
        print("product successfully deleted!")
    else:
        print("product not found")


def add():
    full_products, product_names = open_database()
    product_to_add = input("\nwhat product would you like to add?: ")
    if product_to_add not in product_names:
        product_price = input("what is the price: ")
        product_quantity = input("what is the quantity amount: ")
        full_products.append({"product": product_to_add, "price": product_price, "quantity": product_quantity})
        write_database(full_products)
        print("product successfully added!")
    else:
        print("product already exists")


def view_all():
    full_products = open_database()[0]
    print("\n========================")
    for i in full_products:
        print(f"Product: {i['product']}")
        print(f"Price: ${i['price']}")
        print(f"Quantity: {i['quantity']}")
        print("========================")


def main():
    print("WELCOME TO THE INVENTORY\n========================")
    for _ in range(100):
        try:
            selection = input("\nSelect an option?\n[1]Search | [2]Add\n[3]Update | [4]Delete\n[5]View All | [6]Exit\n>>>: ")
            if selection == "1":
                search()
            elif selection == "2":
                add()
            elif selection == "3":
                update()
            elif selection == "4":
                delete()
            elif selection == "5":
                view_all()
            elif selection == "6":
                quit()
        except FileNotFoundError as E:
            print("Database not found")
            selectiondb = input("Create Database y/n?: ")
            if selectiondb == "y":
                write_database()
            else:
                quit()
    print("Restart")

main()
