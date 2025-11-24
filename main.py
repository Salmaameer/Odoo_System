from Customer import Customer
from product import product
from sale_order import SaleOrder

c = Customer("Rahma", "01111111111")
p = product("Milk", 10, "Fresh milk", 5)
so = SaleOrder("SO-1", c)
so.add_line(p, 2)
print(so.lines)
