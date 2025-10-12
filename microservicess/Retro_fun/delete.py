from db import Session
from models import Product, Manufacturer

session = Session()
m = session.get(Manufacturer, 8)

session.delete(m)
session.commit()
