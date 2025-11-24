from base import BaseModel
class product(BaseModel):
    _next_id=1
    def __init__ (self,name,price,quantity):
        super().__init__(name)
        self._price=price
        self._quantity=quantity

    @property
    def price(self):
        return self._price
    @property
    def quantity(self):
        return self._quantity
    @price.setter
    def price(self, value):
        if value <=0:
            raise ValueError("Price can't be <= 0")
        self._price=value
    @quantity.setter
    def quantity(self,value):
        if value <=0:
             raise ValueError("quantity can't be <= 0")
        self._quantity=value
        
    def __str__(self):
     return f"{self.__class__.__name__}(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity})"




    
   
