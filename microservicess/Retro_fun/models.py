from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db import Model


# this is a model as the name suggests it models the database
# this will be used by the database refrenced by engine to create tables
# engine here stands for the database im im using eg postgres, sql
class Product(Model):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    manufacturer: Mapped[str] = mapped_column(String(64))
    year: Mapped[int]
    country: Mapped[str] = mapped_column(String(32))
    cpu: Mapped[str] = mapped_column(String(32))

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'
