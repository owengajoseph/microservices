from db import Session
from models import Product
from sqlalchemy import select, func

session = Session()

# q = select(Product)
# r = session.execute(q)
# print(list(r))


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

# q = select(func.min(Product.year), func.max(Product.year))
# r = session.execute(q)
# print(r.all())

# q = select(Product.manufacturer).order_by(Product.manufacturer)

# q = select(Product.manufacturer).order_by(Product.manufacturer).distinct()
# print(q)

# q = (
#     select(Product.manufacturer)
#     .group_by(Product.manufacturer)
#     .order_by(Product.manufacturer)
# )

# q = (
#     select(
#         Product.manufacturer,
#         func.min(Product.year),
#         func.max(Product.year),
#         func.count(),
#     )
#     .group_by(Product.manufacturer)
#     .order_by(Product.manufacturer)
# )
# print(session.execute(q).all())

q = select(Product).order_by(Product.name).limit(6).offset(3)
print(session.scalars(q).all())
