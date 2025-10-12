from sqlalchemy import select
from db import Session
from sqlalchemy.orm import joinedload
from models import Manufacturer, Product

session = Session()


# p = session.scalar(select(Product).where(Product.name == "ZX Spectrum"))
# print(p)
# print(p.manufacturer)

p=select(Product).options(joinedload(Product.manufacturer))
print(p)