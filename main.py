from product import Product
from productFactory import ProductFactory
from customer import Customer
from sale_order import SaleOrder
from sale_order_line import SaleOrderLine
from invoice import Invoice

products = []
customers = []
orders = []
invoices = []

def addNewProd():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    desc  = input("Enter product desc: ")
    qnt   = int(input("Enter product quantity: "))
    p = ProductFactory.create(name, price, desc, qnt)
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

def listCustomers():
    if not customers:
        print("No customers on the system") 
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
    new_customer = Customer(name, phone, email, address)
    customers.append(new_customer)
    print(f"Customer '{name}' added successfully!\n")

def viewCustDetails():
    cId = int(input("Enter customer ID: "))
    for c in customers:
        if c.id == cId:
            print("Customer found:")
            print(c)
            return
    print(f"No customer found with id {cId}")

def crtNewOrder():
    cId = int(input("Enter customer ID for the order: "))
    customer = None
    for c in customers:
        if c.id == cId:
            customer = c
            break
    if not customer:
        print("Customer not found!")
        return

    order_name = f"SO-{len(orders)+1}"
    new_order = SaleOrder(order_name, customer)

    while True:
        listProducts()
        prod_id = int(input("Enter product ID to add to order (0 to finish): "))
        if prod_id == 0:
            break
        qty = int(input("Enter quantity: "))
        # check for the quantity before 
        product = next((p for p in products if p.id == prod_id), None)
        if not product:
            print("Product not found!")
            continue
        if product.quantity < qty:
            print("Not available stock, choose lower quantity!")
            continue
       
        new_order.add_line(product, qty)
    
    orders.append(new_order)
    customer.add_order(new_order)
    print(f"Order '{order_name}' created successfully!")
    print(new_order)

def confirmOrder():
    order_id = int(input("Enter order ID to confirm: "))
    order = next((o for o in orders if o.id == order_id), None)
    if not order:
        print("Order not found!")
        return
    try:
        order.confirm()
        invoices.append(order.invoice)
        print(f"Order {order.id} confirmed! Invoice created: {order.invoice}")
    except Exception as e:
        print(f"Error confirming order: {e}")

def cancelOrder():
    order_id = int(input("Enter order ID to cancel: "))
    order = next((o for o in orders if o.id == order_id), None)
    if not order:
        print("Order not found!")
        return
    if order.state == "confirmed":
        print("Cannot cancel a confirmed order")
        return
    orders.remove(order)
    order.customer._orders.remove(order)
    print(f"Order {order_id} canceled successfully")

def listInvoices():
    if not invoices:
        print("No invoices yet")
        return
    for inv in invoices:
        print(inv)
        print("\n")


def main():
    while True:
        print("\nWelcome to our OODO system\n")
        print("1- Create customer")
        print("2- Add new product")
        print("3- List all customers")
        print("4- List all products")
        print("5- View customer details")
        print("6- Create new order")
        print("7- Confirm order")
        print("8- Cancel order")
        print("9- List all invoices")
        print("10- Exit\n")

        choice = input("Enter your choice: ")
        if choice == "1":
            crtCust()
        elif choice == "2":
            addNewProd()
        elif choice == "3":
            listCustomers()  
        elif choice == "4":
            listProducts()      
        elif choice == "5":
            viewCustDetails()
        elif choice == "6":
            crtNewOrder()
        elif choice == "7":
            confirmOrder()
        elif choice == "8":
            cancelOrder()
        elif choice == "9":
            listInvoices()
        elif choice == "10":
            print("Exiting....")
            break
        else:
            print("Invalid choice")

main()