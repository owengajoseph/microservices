from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Model
from sqlalchemy import ForeignKey
from typing import Optional

# # this is a model as the name suggests it models the database
# # this will be used by the database referenced by engine to create tables
# # engine here stands for the database im im using eg postgres, sql
# class Product(Model):
#     __tablename__ = "products"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(64))
#     manufacturer: Mapped[str] = mapped_column(String(64))
#     year: Mapped[int]
#     country: Mapped[str] = mapped_column(String(32))
#     cpu: Mapped[str] = mapped_column(String(32))

#     def __repr__(self):
#         return f'Product({self.id}, "{self.name}")'


class Product(Model):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey("manufacturers.id"), index=True
    )
    year: Mapped[int] = mapped_column(index=True)
    country: Mapped[Optional[str]] = mapped_column(String(32))
    cpu: Mapped[Optional[str]] = mapped_column(String(32))
    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="products")

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'


class Manufacturer(Model):
    products: Mapped[list["Product"]] = relationship(
        cascade="all, delete-orphan", back_populates="manufacturer"
    )
    __tablename__ = "manufacturers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)

    def __repr__(self):
        return f'Manufacturer({self.id}, "{self.name}")'
