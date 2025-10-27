# import all the necessary things and create a session
from models import Product, Customer, Order, OrderItem
from db import Session

session = Session()
# create a new customer
c = Customer(name="Jane Smith")
# create a new order, add it to the customer and to the database session
o = Order()
c.orders.add(o)
session.add(o)
# add the first line item in the order: product #45 for $45.50
p1 = session.get(Product, 45)
print(p1)
o.order_items.append(OrderItem(product=p1, unit_price=45.5, quantity=1))
# add the second line item: 2 of product #82 for $37 each
p2 = session.get(Product, 82)
print(p2)
o.order_items.append(OrderItem(product=p2, unit_price=37, quantity=2))
# write the order (along with the customer and order items) to the database
session.commit()
# check the UUID and the timestamp defaults assigned to the new order
print(o.id)
print(o.timestamp)
