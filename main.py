from product import Product
from productFactory import ProductFactory
from customer import Customer  # assuming you have a Customer class



products = []
customers = []

def addNewProd():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    desc  = input("Enter product desc: ")
    qnt   = int(input("Enter product quantity: "))
    #append the product to the list
    p = ProductFactory.create(name,price,desc, qnt)
    products.append(p)
    print(p)
    print("Product added successfully!")

def listProducts():
    if not products:
        print("No available products\n\n") 
    else: 
        print("Available products: ")
        for p in products:
            print(p)
            print("\n")

def listCutsomers():
    if not customers:
        print("no Customers on the system") 
    else: 
        print("Customers: \n")
        for c in customers:
            print(c)
            print("\n")

def crtCust():
    name = input("Enter Customer name: ")
    phone = input("Enter Customer phone: ")
    email = input("Enter Customer email: ")
    address = input("Enter Customer address: ")

    # Create a new Customer instance
    new_customer = Customer(name, phone, email, address)

    # Add to the list
    customers.append(new_customer)
    print(f"Customer '{name}' added successfully!\n")

def viewCustDetails(id):
    for c in customers:
        if c.id == id:
            print("Customer found:")
            print(c)
            return  # exit the function after finding
    print(f"No customer found with id {id}")

def crtNewOrder():
    pass


def main():
    # c = Customer("salma","123","das","34343")
    # customers.append(c)
    # viewCustDetails(1)

    while(True):

        print("\n\nWelcome to our OODO system\n\n" \
        "these are our services:\n\n" \
        "1- create customer\n" \
        "2- add new product\n" \
        "3- list all customers\n" \
        "4- list all products\n" \
        "5- view Customer details\n" \
        "6- create new order\n" \
        "7- confirm order\n" \
        "8- cancel order\n" \
        "9- list all invoices\n" \
        "10- exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            crtCust()
        elif choice == "2":
            addNewProd()
        elif choice == "3":
            listCutsomers()  
        elif choice == "4":
            listProducts()      
        elif choice == "5":
            cId = int(input("Enter customer ID: "))
            viewCustDetails(cId)
        elif choice == "6":
            pass  
        elif choice == "7":
            pass  
        elif choice == "8":
            pass  
        elif choice == "9":
            pass  
        elif choice == "10":
            print("Exiting....")
            break
        else:
            print("Invalid choice")




main()            

