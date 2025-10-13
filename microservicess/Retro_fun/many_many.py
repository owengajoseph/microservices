from db import Session
from models import Product, Manufacturer, Country
from sqlalchemy import select, func

session = Session()

# p = session.scalar(select(Product).where(Product.name == "Timex Sinclair 1000"))
# print(p)

country_count = func.count(Country.id).label(None)
q = (
    select(Product, country_count)
    .join(Product.countries)
    .group_by(Product)
    .having(country_count >= 2)
    .order_by(Product.name)
)
print(session.execute(q).all())
