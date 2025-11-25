from base import BaseModel
class Customer(BaseModel):

    def __init__(self,name,phone, email, address):
        super().__init__(name)
        self._phone=phone
        self._email=email
        self._address=address
        self._orders=[]
        self._invoices=[]
        
    @property
    def phone(self):
        return self._phone
    @property
    def email(self):
        return self._emile
    
    @property
    def orders(self):
        return self._orders
    @property
    def invoices(self):
        return self._invoices
    @property
    def address(self):
        return self._address
    @phone.setter
    def phone (self, value):
        if not value.isdigit() or len(value)!=11:
        
            raise ValueError("invalid phone ")
        self._phone=value

    @email.setter
    def emile(self,value):
        self._email=value
 
    @address.setter
    def address(self,value):
        self._address=value

    def add_order(self,order):
        self._orders.append(order)

    def add_invoice(self, invoice):
        self._invoices.append(invoice)

    def total_spent(self):
        total=0
        for order in self._order:
            if order.state == "confirmed":
                for x in order.lines:
                    total += x.subtotal
                   
        return total
    def total_voices(self):
        total = 0
        for invoice in self._invoices:
            if invoice.state =="posted" :
                for x in invoice.lines:
                    total+=x.subtotal
        return total




    def list_order(self, order):
         return self._orders
    
    def display_info(self):
        print (f"id :{self._id}")
        print (f"name : {self._name}")
        print (f"phone : {self._phone}")
        print (f"emile : {self._emile}")
        print (f"address : {self._address}")
        print(f"Orders count: {len(self._orders)}")
        print(f"Invoices count: {len(self._invoices)}")
    def __str__(self):
        return f"{self.__class__.__name__}(id={self._id}, name={self.name}, phone={self._phone}, emile={self._emile}, address={self._address})"
