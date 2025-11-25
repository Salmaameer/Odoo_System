class InvoiceLine:
    def __init__(self, product, quantity, unitPrice):
        self._product = product
        self._quantity = quantity
        self._unitPrice = unitPrice
        self._subtotal = quantity * unitPrice   # calculated

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._updateSubtotal()

    @property
    def unitPrice(self):
        return self._unitPrice

    @unitPrice.setter
    def unitPrice(self, value):
        self._unitPrice = value
        self._updateSubtotal()

    
    @property # subtotal is read only
    def subtotal(self):
        return self._subtotal

    # private function to update subtotal 
    def _updateSubtotal(self):
        self._subtotal = self._quantity * self._unitPrice
