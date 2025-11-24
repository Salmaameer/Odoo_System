from base import BaseModel

class Invoice(BaseModel):
    _next_num = 1

    def __init__(self,customer):
        name = "In"+ Invoice._next_num  #customer readable id
        super().__init__(name)
        self.customer = customer
        self.lines = []
        self.total = 0.0


    @property
    def customer(self):
        return self.customer

    @customer.setter
    def customer(self,c):
        if not c:
            raise ValueError
        else:
            self.customer = c


    @property
    def lines(self):
        return self.lines

    @lines.setter
    def lines(self,lns):
        self.lines = lns
        ##update the total & subtotal per line added
        self.calculateTotal()


    @property    #total could only read
    def total(self):
        return self.total


    def addLine(self, ln):
        self.lines.append(ln)
        self.updateInvcTotal(ln)
    
    # private helper functions
    def _calculateTotal(self):
        ttl = 0.0
        for line in self.lines:
            ttl += line.subTotal
        self.total = ttl            #set the total for the first time

    def _updateInvcTotal(self,line):  #update after adding one line
        lnSubttl = line.subtotal
        updatedTtl = lnSubttl + self.total
        self.total = updatedTtl


    #print invoice info
    def __str__(self):
        return (
            f"Invoice #{self.name},"
            f"\nsubtotal: {self.subtotal} EGP"
        )  