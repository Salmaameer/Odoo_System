from base import BaseModel

class Invoice(BaseModel):
    _next_num = 1

    def __init__(self,customer):
        name = "In-" + str(Invoice._next_num)      #customer readable id
        Invoice._next_num += 1

        super().__init__(name)
        self._customer = customer
        self._lines = []
        self._total = 0.0


    @property
    def customer(self):
        return self._customer


    @customer.setter
    def customer(self, value):
        if not value:
            raise ValueError("Customer must not be empty")
        self._customer = value


    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value
        ##update the total & subtotal per line added
        self._recalculate_total()
   
    @property
    def total(self):
        return self._total

    def addLine(self, line):
        self._lines.append(line)
        self._total += line.subtotal

    # Helper to recalc full total
    def _recalculate_total(self):
        self._total = sum(line.subtotal for line in self._lines)

    def __str__(self):
        return f"Invoice #{self.name}, total: {self.total} EGP"