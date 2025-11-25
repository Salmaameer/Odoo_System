from product import Product
from productFactory import ProductFactory



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



def crtCust():
     name = input("Enter Customer name: ")



def main():

    while(True):

        print("Welcome to our OODO system\n\n" \
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
            pass
        elif choice == "2":
            addNewProd()
        elif choice == "3":
            pass  
        elif choice == "4":
            listProducts()      
        elif choice == "5":
            pass  
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