from db import Session
from models import Product
from sqlalchemy import select, func

session = Session()

q = select(Product)
r = session.execute(q)


# print(session.execute(q).all())
# print(session.execute(q).first())

# print(session.scalars(q).all())

# q = select(Product).where(Product.manufacturer == "Commodore")
# print(session.scalars(q).all())


# q = select(Product).where(Product.year >= 1990)
# print(session.scalars(q).all())

# q = select(Product).where(Product.name.like('%Sinclair%'))

# print(session.scalars(q).all())


# q = select(Product.name)
# print(session.scalars(q).all())


# q = select(Product.name, Product.manufacturer)
# print(session.execute(q).all())

q = select(func.min(Product.year), func.max(Product.year))
r = session.execute(q)
print(r.all())